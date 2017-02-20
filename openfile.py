#coding:utf-8
from string import rstrip
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt
#---2017.02.01 ---#
#--- open txt file ---#
# plot the content of the file


filepath='/home/kpchang/Downloads/105.txt'
time,accel_x,accel_y,accel_z=[],[],[],[]

with open(filepath) as fid:
	#lines = [line for line in fid if line.strip()]
	lines = fid.read().splitlines()
	#print lines
	#print len(lines)
	for row in lines:
		data = row.split('\t')
		#print row
		try:
			time.append(float(data[0]))
			accel_x.append(float(data[1]))
			accel_y.append(float(data[2]))
			accel_z.append(float(data[3]))
		except IndexError:
			print 'You have an empty row'
		except ValueError:
			print 'Could not convert string to float'
			print 'pass this item!'
			
#print type(time)
#print time[0:3]

#---- processing ----#
N = len(time)
dt = time[2]-time[1]
f = 1./dt
df = f/N
freq = np.linspace(0,f/2,N/2)
FFT_accel_x = 2.0/N*abs(scipy.fftpack.fft(accel_x)[0:N/2])
FFT_accel_y = 2.0/N*abs(scipy.fftpack.fft(accel_y)[0:N/2])
FFT_accel_z = 2.0/N*abs(scipy.fftpack.fft(accel_z)[0:N/2])

#---plot diagram ---#
plt.figure(1)
plt.subplot(311)
plt.plot(time[1:],accel_x[1:])
plt.grid()
plt.subplot(312)
plt.plot(time[1:],accel_y[1:])
plt.grid()
plt.subplot(313)
plt.plot(time[1:],accel_z[1:])
plt.grid()
plt.figure(2)
plt.subplot(311)
plt.plot(freq,FFT_accel_x)
plt.subplot(312)
plt.plot(freq,FFT_accel_y)
plt.subplot(313)
plt.plot(freq,FFT_accel_z)

plt.show()
