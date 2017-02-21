#coding:utf-8
from string import rstrip
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt
#---2017.02.01 ---#
#--- open txt file ---#
# plot the content of the file
filepath='/home/chang/python/vibration/85.txt'
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
 
#---- processing ----#

N = len(time)
dt = time[2]-time[1]
f = 1./dt
df = f/N
freq = np.linspace(0,f/2,N/2)
#如果不取一半,所畫出來的頻譜只能看一半
#另外一半剛好是對稱
FFT_accel_x = 2.0*abs(scipy.fftpack.fft(accel_x)[0:N/2])/N
FFT_accel_y = 2.0*abs(scipy.fftpack.fft(accel_y)[0:N/2])/N
FFT_accel_z = 2.0*abs(scipy.fftpack.fft(accel_z)[0:N/2])/N


#---plot diagram ---#
class plot_diagram(object):
	def __init__(self,ax,min_y=0.,max_y=0.002):
		self.ax = ax				
		self.ax.set_ylim([min_y,max_y])
	def freq_spec(self):
		pass
#Find the way to pass the data into the class
#for now, the function of class is initiated the format of the diagrams
#but not finish yet

	
fig,ax = plt.subplots()
scope = plot_diagram(ax)

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
ax2_1 = plt.subplot(311)
plt.plot(freq,FFT_accel_x)
ax2_2 = plt.subplot(312)
plt.plot(freq,FFT_accel_y)
ax2_3 = plt.subplot(313)
plt.plot(freq,FFT_accel_z)
ax2_1.set_ylim([0.,0.002])
ax2_2.set_ylim([0.,0.002])
ax2_3.set_ylim([0.,0.002])
plt.show()
