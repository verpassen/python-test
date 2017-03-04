import numpy as np
from scipy import pi,sin,cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def fun(n):
	k = np.linspace(0,1,n)
	x = 2*k+3
	y = 2*k**2+3
	return np.asarray([x,y,1,1])

def rot_X_axis(rot_ang,P):
	rad_ang = rad2deg(rot_ang)
	M = np.asarray([[cos(rot_ang),-sin(rot_ang),0,0],[sin(rot_ang),cos(rot_ang),0,0],[0,0,1,0],[0,0,0,1]])
	P2 = np.dot(M,P.T)
	return P2
def rad2deg(rad):
	return rad*180/pi

N = 2**8
phi = np.linspace(0,2*pi,N)
contour_A = fun(N)


fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(contour_A[0],contour_A[1])
ax.set_xlabel('X axis [mm]')
ax.set_ylabel('Y axis [mm]')
ax.set_xlim([0,10])
ax.set_ylim([0,10])
plt.grid()
plt.show()
