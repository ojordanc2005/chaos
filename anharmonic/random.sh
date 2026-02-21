#!/bin/bash
#SBATCH -n 8
#SBATCH -a [1-32]
#SBATCH --mem=64gb
#SBATCH --output=outs/%j.out
#SBATCH -p GTX980

module load python/anaconda3.7
source activate my_env
export OMP_NUM_THREADS=1

jid=$((SLURM_ARRAY_TASK_ID-1))
ZGN_init=`bc -l <<< "1.0/32*$jid"`
ZGN_delta=0.35
ZGN_num=4
ZGN_cycles=5000
ZGN_outcycle=4000
ZGN_seeds=128

filebase0=data/random0
mkdir -p $filebase0

ZGN_freq=3.5
ZGN_amp=0.05

#From random initial conditions
for tid in `seq 0 $ZGN_seeds`; do
filebase=${filebase0}/${jid}_${tid}
echo $jid $tid $filebase
if [ ! -f ${filebase}fs.npy ]; then
./pendula.py --verbose 0 --delta $ZGN_delta --num $ZGN_num --init $ZGN_init --cycles $ZGN_cycles --outcycle $ZGN_outcycle --dt 0.5 --amplitude $ZGN_amp  --frequency $ZGN_freq --noisestep 10 --filebase $filebase --seed $tid --rtol 0 --atol 1e-6 &
else
echo "previously completed"
fi
js=`jobs | wc -l`
while [ $js -ge 8 ]; do
sleep 1
js=`jobs | wc -l`;
done
done
wait

rm $filebase0/${jid}*.npy

for tid in `seq 0 $ZGN_seeds`; do tail -n 2 ${filebase0}/${jid}_${tid}out.dat | head -n 1 >> ${filebase0}/${jid}.txt; rm ${filebase0}/${jid}_${tid}out.dat; done;
