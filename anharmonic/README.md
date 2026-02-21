# Files in the anharmonic repository
The file pendula.py is a Python script used to numerically integrate the anharmonic time crystal pendulum model using SciPy's Variable-coefficient Ordinary Differential Equation solver.  The file plot.nb is a Mathematica notebook which can be used to plot results.  The folder data contains sample output, which is visualized in plot.nb.
# System requirements
The Python code has been run with Anaconda2 and Anaconda3, which can both be downloaded from the Anaconda website: https://www.anaconda.com/download/#macos.  It requires packages numpy, scipy, and progressbar. To create an environment with these packages, execute `conda create -n anharmonic_env scipy numpy progressbar` and activate it with `source activate anharmonic_env`.  The Mathematica code has been run with Mathematica 12.0.0.0.
# Usage
Running the terminal command `./pendula.py -h` will give a usage message with command line argument descriptions.
```
usage: pendula.py [-h] --filebase FILEBASE [--num NUM] [--frequency FREQ]
                  [--amplitude AMP] [--delta DELTA] [--noise SIGMA]
                  [--disorder EPSILON] [--cycles CYCLES]
                  [--average AVG [AVG ...]] [--dt DT] [--noisestep STEP]
                  [--seed SEED] [--damp DAMP] [--spring SPRING] [--init INIT]
                  [--rtol RTOL]

Noisy pendula.

optional arguments:
  -h, --help            show this help message and exit
  --filebase FILEBASE   Base string for file output
  --num NUM             Number of pendula
  --frequency FREQ      Driving frequency
  --amplitude AMP       Driving amplitude
  --delta DELTA         Alternating pendulum length scale
  --noise SIGMA         Noise intensity
  --disorder EPSILON    Pendulum length disorder scale
  --cycles CYCLES       Simulation time in driving cycles
  --average AVG [AVG ...]
                        Driving cycles to wait before averaging
  --dt DT               Time between outputs in driving cycles
  --noisestep STEP      Noise steps per output timestep
  --seed SEED           Seed for random initial conditions
  --damp DAMP           Damping coefficient
  --spring SPRING       Spring coefficient
  --init INIT           Initial random scale
  --rtol RTOL           Relative error tolerance
```
___
# Output files
The pendula.py program will produce two output files, FILEBASEout.dat and FILEBASEdat.npy, where FILEBASE is a required argument to the script. The file FILEBASEout.dat is a text file containing a single line with the number of pendulum, the driving frequency, the driving amplitude, the output timestep, the damping coefficient, the noise intensity, the random length intensity, the number of cycles run, the random seed, and the number of steps between noise samples. The file FILEBASEdat.npy is a binary file containing the angles for the pendula at each timestep.
