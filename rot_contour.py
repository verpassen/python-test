import numpy as np
from scipy import pi,sin,cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def fun(n):
	k = np.linspace(0,1,n)
	x = 2*k+3
	y = 2*k**2+3
	z = np.zeros(n)
	return np.asarray([x,y,z,np.ones(n)])
def fun2(n):
	k = np.linspace(0,1,n)
	x = 10*k-5
	y = np.zeros(n)
	z = 5*k+5
	return np.asarray([x,y,z,np.ones(n)])
def rot_X_axis(rot_ang,P,di):
	rot_ang = rad2deg(rot_ang)
	P2_X = np.outer(np.ones(len(rot_ang)),P[0,:]) + di
	P2_Y = np.outer(cos(rot_ang),P[1,:]) + np.outer(sin(rot_ang),P[2,:])
	P2_Z = np.outer(-sin(rot_ang),P[1,:]) + np.outer(cos(rot_ang),P[2,:])
	return P2_X,P2_Y,P2_Z
def rot_Y_axis(rot_ang,P,di):
	rot_ang = rad2deg(rot_ang)
	P2_X = np.outer(cos(rot_ang),P[0,:]) + np.outer(sin(rot_ang),P[2,:])	
	P2_Y = np.outer(np.ones(len(rot_ang)),P[1,:]) + di
	P2_Z = np.outer(-sin(rot_ang),P[0,:]) + np.outer(cos(rot_ang),P[2,:])
	return P2_X,P2_Y,P2_Z
def rot_Z_axis(rot_ang,P,di):
	rot_ang = rad2deg(rot_ang)
	P2_X = np.outer(cos(rot_ang),P[0,:]) + np.outer(sin(rot_ang),P[1,:])	
	P2_Y = np.outer(-sin(rot_ang),P[0,:]) + np.outer(cos(rot_ang),P[1,:])
	P2_Z = np.outer(np.ones(len(rot_ang)),P[2,:])+di
	return P2_X,P2_Y,P2_Z
def rad2deg(rad):
	return rad*180/pi

N = 2**6
phi = np.linspace(0,2*pi,N)
contour_A = fun(N)
contour_B = fun2(N)
surface_AX,surface_AY,surface_AZ= rot_X_axis(phi,contour_A,0)
surface_AX2,surface_AY2,surface_AZ2= rot_Y_axis(phi,contour_A,0)
surface_BX,surface_BY,surface_BZ= rot_Z_axis(phi,contour_B,0)
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
plt.plot(contour_A[0],contour_A[1],'r')
plt.plot(contour_B[0],contour_B[1],contour_B[2],'r')
#ax.plot_surface(surface_AX,surface_AY,surface_AZ)
#ax.plot_surface(surface_AX2,surface_AY2,surface_AZ2)
ax.plot_surface(surface_BX,surface_BY,surface_BZ)
ax.set_xlabel('X axis [mm]')
ax.set_ylabel('Y axis [mm]')
ax.set_xlim([0,10])
ax.set_ylim([0,10])
plt.grid()
plt.show()
