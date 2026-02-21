#!/usr/bin/env python
from __future__ import print_function
import time
import argparse
import sys
import numpy as np
import progressbar
import timeit
import os
from scipy.integrate import ode
from scipy.signal import argrelmin, argrelmax

#Command line arguments
parser = argparse.ArgumentParser(description='Noisy pendula.')
parser.add_argument("--filebase", type=str, required=True, dest='filebase', help='Base string for file output')
parser.add_argument("--num", type=int, default=32, dest='num', help='Number of pendula')
parser.add_argument("--frequency", type=float, default=3.4, dest='freq', help='Driving frequency')
parser.add_argument("--initfrequency", type=float, default=3.4, dest='freq0', help='Initial driving frequency')
parser.add_argument("--initamplitude", type=float, default=0.05, dest='amp0', help='Driving amplitude')
parser.add_argument("--amplitude", type=float, default=0.05, dest='amp', help='Driving amplitude')
parser.add_argument("--delta", type=float, default=0.5, dest='delta', help='Alternating pendulum length scale')
parser.add_argument("--noise", type=float, default=0.0, dest='sigma', help='Noise intensity')
parser.add_argument("--disorder", type=float, default=0.0, dest='epsilon', help='Pendulum length disorder scale')
parser.add_argument("--cycles", type=float, default=1000, dest='cycles', help='Simulation time in driving cycles')
parser.add_argument("--initcycle", type=float, default=0, dest='initcycle', help='Simulation time in driving cycles')
parser.add_argument("--outcycle", type=float, default=0, dest='outcycle', help='Cycle to start outputting')
parser.add_argument("--average", nargs=2, type=int, default=[50, 100], metavar=('START', 'END'), dest='avg', help='Driving cycles over which to calculate growth rate')
parser.add_argument("--dt", type=float, default=0.05, dest='dt', help='Time between outputs in driving cycles')
parser.add_argument("--noisestep", type=int, default=1, dest='step', help='Noise steps per output timestep')
parser.add_argument("--seed", type=int, default=1, dest='seed', help='Seed for random initial conditions')
parser.add_argument("--damp", type=float, default=0.1, dest='damp', help='Damping coefficient')
parser.add_argument("--spring", type=float, default=1.0, dest='spring', help='Spring coefficient')
parser.add_argument("--init", type=float, default=0.01, dest='init', help='Initial random scale')
parser.add_argument("--rtol", type=float, default=1e-6, dest='rtol', help='Relative error tolerance')
parser.add_argument("--atol", type=float, default=1e-6, dest='atol', help='Absolute error tolerance')
parser.add_argument("--verbose", type=int, default=1, dest='verbose', help='Verbose output')
args = parser.parse_args()

def func(t, y):
		# q=np.mod(y[:N]+np.pi,2*np.pi)-np.pi
		q=y[:N]
		p=y[N:]
		if t < 2*np.pi*args.initcycle:
			amp=args.amp0+t/(2*np.pi*args.initcycle)*(args.amp-args.amp0)
			freq=args.freq0+t/(2*np.pi*args.initcycle)*(args.freq-args.freq0)
		else:
			amp=args.amp
			freq=args.freq

		return np.concatenate( [p/lengths/freq, (-args.damp*p - (1+amp*freq**2*np.cos(t))*np.sin(q) +args.spring*np.roll(lengths,1)*np.sin(np.roll(q,1)-q)+args.spring*np.roll(lengths,-1)*np.sin(np.roll(q,-1)-q)+args.spring*(np.roll(lengths,1)+np.roll(lengths,-1)-2*lengths)*np.sin(q)+noises)/freq] )

start = timeit.default_timer()

N=args.num
np.random.seed(args.seed)

ys=np.zeros((int((args.cycles-args.outcycle)/args.dt),2*N))
y=np.zeros(2*N)
if (os.path.isfile(args.filebase+"ic.npy")):
	# if args.verbose==1:
	print("using initial conditions from file",flush=True)
	y=np.load(args.filebase+"ic.npy")
else:
	# if args.verbose==1:
	print("using random initial contions",flush=True)
	y[:N] = args.init*2*np.pi*(np.random.random(N)-0.5)
	# y[int(N/2):int(N/2)+2] = args.init*2*np.pi*(np.random.random(2)-0.5)
lengths=np.array([1+args.delta*(-1)**i for i in range(N)])+args.epsilon*(np.random.random(N)-0.5)
noises=np.random.normal(0,args.sigma/np.sqrt(args.dt/args.step),size=N)
rode=ode(func).set_integrator('vode', rtol=args.rtol, atol=args.atol, max_step=2*np.pi*args.dt/args.step)
rode.set_initial_value( y, 0 )

if args.verbose==1:
	pbar=progressbar.ProgressBar(widgets=['Integration: ', progressbar.Percentage(), progressbar.Bar(), ' ', progressbar.ETA()], maxval=2*np.pi*(args.cycles+1))
	pbar.start()

for n in range(int(args.cycles/args.dt)):
	for m in range(args.step):
		# t=n*2*np.pi*args.dt+m*2*np.pi*args.dt/args.step
		noises=np.random.normal(0,args.sigma/np.sqrt(2*np.pi*args.dt/args.step),size=N)
		y=rode.integrate(rode.t + 2*np.pi*args.dt/args.step)

	if args.verbose==1:
		pbar.update(rode.t)
	if n >= int(args.outcycle/args.dt):
		# ys[n-int(args.outcycle/args.dt)]=y
		ys[n-int(args.outcycle/args.dt),:N]=np.mod(y[:N]+np.pi,2*np.pi)-np.pi
		ys[n-int(args.outcycle/args.dt),N:]=y[N:]
if args.verbose==1:
	pbar.finish()

order=np.mean((np.mod(ys+np.pi,2*np.pi)-np.pi)[:,:N]**2)
try:
	norms=np.linalg.norm(ys[-100:,:N]-ys[0,:N],axis=1)
	min=np.min(norms)
	N2=np.where(np.linalg.norm(ys[:,:N]-ys[0,:N],axis=1)==min)[0][0]
	dy=np.abs(np.fft.fft(ys[:N2,:N],axis=0))/((2*np.pi*N2)**0.5)
except:
	N2=len(ys)
	dy=np.abs(np.fft.fft(ys[:N2,:N],axis=0))/((2*np.pi*N2)**0.5)
# N2=len(ys)
# dy=np.abs(np.fft.fft((np.mod(ys+np.pi,2*np.pi)-np.pi)[:N2],axis=0))/(N2**0.5)
epsilon=(np.argmax(np.mean(dy,axis=1)))/(N2*args.dt)
epsilon=np.min([epsilon,1-epsilon])
dy2=np.mean(np.abs(np.fft.fft((np.mod(ys+np.pi,2*np.pi)-np.pi)[:N2,:N:2],axis=1))**2+np.abs(np.fft.fft((np.mod(ys+np.pi,2*np.pi)-np.pi)[:N2,1:N:2],axis=1))**2,axis=0)
wavenumber=2*np.pi*np.argmax(dy2)/(N/2-1)

print(order,epsilon,wavenumber)
np.save(args.filebase+"power",np.array([np.arange(N2)/(N2*args.dt),np.mean(dy,axis=1)]))
stop = timeit.default_timer()

file=open(args.filebase+'out.dat','w')
print(*sys.argv,file=file)

print("%i %f %f %f %f %f %f %f"%(args.num, args.dt, args.freq, args.amp, args.epsilon, order, epsilon, wavenumber), file=file)
print('runtime: %f' % (stop - start), file=file)
print('runtime: %f' % (stop - start))
if args.verbose==1:
	np.save(args.filebase+"dat",ys)

np.save(args.filebase+"fs",ys[-1])

file.close()
