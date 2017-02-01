#coding:utf-8
from string import rstrip
import numpy as np
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
			time.append(data[0])
			accel_x.append(data[1])
			accel_y.append(data[2])
			accel_z.append(data[3])
		except IndexError:
			print 'You have an empty row'

#print type(time)
#print time[0:3]

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
plt.show()
