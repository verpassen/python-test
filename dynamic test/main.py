#coding: utf-8
import numpy as np 
from scipy import signal
from scipy.io import wavfile
from scipy import pi,cos,sin
from numpy.fft import fft,ifft
import  matplotlib.pyplot as plt
import wavio 
'''
N = 2**12
Fs= 3500.
nyq = Fs/2
dw ,dt = Fs/N , 1./Fs
t = np.linspace(0,dt*N,N)
w = np.linspace(0,nyq,N)
'''
class test(object):
    def __init__(self):
        pass
   
    def gen_sig(self,f,time,Amp,n):
        t_span = np.linspace(0,time,n)
        sig = Amp*cos(2*pi*f*t_span)
        print ('Amplitude',Amp)
        print ('f' ,f )
        print ('time',time)
        
        return t_span,sig
    '''
    @staticmethod
    def subset_sig(sig,fs,Upper_time,Lower_time):
        dt = 1./fs
        n = [int(Upper_time//dt),int(Lower_time//dt)]
        return sig[n[1]:n[0]]
    '''
    def subset_sig(self,sig,fs,Upper_time,Lower_time):
        dt = 1./fs
        n = [int(Upper_time//dt),int(Lower_time//dt)]
        return sig[n[1]:n[0]]

path = '/home/chang/下載/amin9-chord-120bpm.wav'
fs, _,data = wavio.readwav(path)
dt = 1./fs
N = len(data)
time_span = np.linspace(0,dt*N,N)

#=== get part of the_signal ===#
Upper_time,Lower_time = 3.5,0.5
Total_time = (Upper_time-Lower_time)
Sub_sig = test().subset_sig(data,fs,Upper_time,Lower_time)
Sub_time = np.linspace(0,Total_time,Total_time/dt)
#plt.figure(1)
#plt.plot(Sub_time,Sub_sig[:,0],Sub_time,Sub_sig[:,1])
#plt.show()
#===

#=== plot the diagram ===#
#plt.figure(2)
#plt.subplot(211)
#plt.plot(time_span,data[:,0])
#plt.grid()
#plt.subplot(212)
#plt.plot(time_span,data[:,1])
#plt.grid()
#plt.show()
t,f,Sxx = signal.spectrogram(data,fs)
plt.figure(10)
ax1 = plt.gca()
plt.pcolormesh(t,f,Sxx)
plt.xlabel('time[sec]')
plt.ylabel('frequency[Hz]')
ax.set_xlim([0,3])
ax.set_ylim([0,2000])
plt.show()

#====
#A = test()
#t_sptan, sig1 = A.gen_sig(10,3,1,N)
#t_sptan,sig2 = A.gen_sig(300,3,1,N)
#sig s= sig1*sig2
#==== plot diagram ===#
#plt.figure(1)
#plt.plot(t_span,sig)
#plt.grid()
#plt.show()
