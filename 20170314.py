import numpy as np 
from scipy import pi,sin,cos
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
N = 2**6

def fun(N):
	k = np.linspace(0,1,N)
	x = 2*k+3
	y = k
	z = np.zeros(N)
	return np.asarray([x,y,z,np.ones(N)])
def rad2deg(rad):
	return rad*180/pi

def Rot_X_Axis(rot_ang,P):
	ang = rad2deg(rot_ang)
	P2_X = np.outer(P[0,:],np.ones(len(rot_ang)))
	#P2_X = np.outer(np.ones(len(rot_ang)),P[0,:])
	P2_Y = np.outer(P[2,:],sin(ang)) + np.outer(P[1,:],cos(ang))
	P2_Z = np.outer(P[2,:],cos(ang)) + np.outer(P[1,:],-sin(ang))
	return P2_X,P2_Y,P2_Z

def Rot_Y_Axis(rot_ang,P):
	ang = rad2deg(rot_ang)
	P2_X = np.outer(P[2,:],sin(ang)) + np.outer(P[0,:],cos(ang))
	P2_Y = np.outer(P[1,:],np.ones(len(rot_ang)))
	P2_Z = np.outer(P[2,:],cos(ang)) + np.outer(P[0,:],-sin(ang))
	return P2_X,P2_Y,P2_Z


phi = np.linspace(0,2*pi,N)
contour1 = fun(N)
#surface_X, surface_Y,surface_Z= Rot_X_Axis(phi,contour1)
surface_X, surface_Y,surface_Z= Rot_Y_Axis(phi,contour1)

fig = plt.figure(1)
ax = fig.add_subplot(111,projection = '3d')
plt.plot(contour1[0,:],contour1[1,:],contour1[2,:],'r',linewidth = 2)
#ax.plot_surface(surface_X, surface_Y, surface_Z, rstride=1, cstride=1,color = 'b')
ax.set_xlabel('X axis [mm]')
ax.set_ylabel('Y axis [mm]')
ax.set_zlabel('Z axis [mm]')
plt.show()
