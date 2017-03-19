import numpy as np
from scipy import pi,sin,cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def fun(n):
	k = np.linspace(0,1,n)
	x = 2*k+3
	y = 2*k**2+3
	return np.asarray([x,y,np.zeros(n),np.ones(n)])

def rot_X_axis(rot_ang,P):
	rot_ang = rad2deg(rot_ang)
	P2_X = np.outer(np.ones(len(rot_ang)),P[0,:])
	P2_Y = np.outer(cos(rot_ang),P[1,:]) + np.outer(sin(rot_ang),P[2,:])
	P2_Z = np.outer(-sin(rot_ang),P[1,:]) + np.outer(cos(rot_ang),P[2,:])
	return P2_X,P2_Y,P2_Z
def rad2deg(rad):
	return rad*180/pi

N = 2**6
phi = np.linspace(0,2*pi,N)
contour_A = fun(N)
surface_AX,surface_AY,surface_AZ= rot_X_axis(phi,contour_A)
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
plt.plot(contour_A[0],contour_A[1],'r')
ax.plot_surface(surface_AX,surface_AY,surface_AZ)
ax.set_xlabel('X axis [mm]')
ax.set_ylabel('Y axis [mm]')
ax.set_xlim([0,10])
ax.set_ylim([0,10])
plt.grid()
plt.show()
