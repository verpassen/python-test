import numpy as np
from scipy import sin,cos,pi,arccos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# for given two different positions
# try to find a screw to guide rigid body from pos 1 to pos 2
# and caculate the screw parameters and so as the transformation matrix

# position format(x,y,z,1)
pos1 = np.array([3.,4.,2.,1.])
pos2 =np.array([10.,-2.,0.,1.]) 

s = np.array([0,0,1])
s0 = np.array([0,0,0])
Sp1toPos1 = pos1[0:3]-np.dot(pos1[0:3],s/np.linalg.norm(s))*s
Sp1toPos2 = pos2[0:3]-np.dot(pos2[0:3],s/np.linalg.norm(s))*s
print np.dot(Sp1toPos1,s)
print np.dot(Sp1toPos2,s)
Dist_Sp1toPos1 = np.linalg.norm(Sp1toPos1)
Dist_Sp1toPos2 = np.linalg.norm(Sp1toPos2)

print Dist_Sp1toPos1,Dist_Sp1toPos2
'''
def screw2matrix(s,s0,the,t):
	a11 = (s[0]**2-1)*(1-cos(the))+1
	a12 = s[0]*s[1]*(1-cos(the))-s[2]*sin(the)
	a13 = s[0]*s[2]*(1-cos(the))+s[1]*sin(the)
	a14 = t*s[0]-s0[0]*(a11-1)-s0[1]*a12-s0[2]*a13
	a21 = s[0]*s[1]*(1-cos(the))+s[2]*sin(the)
	a22 = (s[1]**2-1)*(1-cos(the))+1
	a23 = s[1]*s[2]*(1-cos(the))-s[0]*sin(the)
	a24 = t*s[1]-s0[0]*a21-s0[1]*(a22-1)-s0[2]*a23
	a31 = s[2]*s[0]*(1-cos(the))-s[1]*sin(the) 
	a32 = s[1]*s[2]*(1-cos(the))+s[0]*sin(the)
	a33 = (s[2]**2-1)*(1-cos(the))+1
	a34 = t*s[2]-s0[0]*a31-s0[1]*a32-s0[2]*(a33-1)
	a41 = 0
	a42 = 0
	a43 = 0
	a44 = 1
	M = np.array([[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44]])
	return M
'''
class plot_user_defind():
    def __init__(self,fig):
        self.start= -0.05
        self.delta = 0.05
        self.end =2*abs(self.delta)+self.start
        self.coordinate_init()
    def coordinate_init(self):
        ax = fig.add_subplot(111,projection='3d')
        ax.arrow(0,self.start,0,self.end,linewidth=0.4)
        ax.arrow(self.start,0,self.end,0,linewidth=0.4)
        ax.set_xlim([-3,3])
        ax.set_ylim([-3,3])
        ax.set_zlim([-3,3])
        ax.set_xlabel('X axis (mm)')
        ax.set_ylabel('Y axis (mm)')
        ax.set_zlabel('Z axis (mm)')
        #ax.axhline(y=0,color='k')

		
# ===cond. 2 ====#
#given Pos 1 and Transformation matrix 
#find Pos2
#use Transformation matrix find screw parameters S and S0
the = pi/6
M32 = np.array([[cos(the),-sin(the),0,0],[sin(the),cos(the),0,0],[0,0,1,0],[0,0,0,1]])
M21 = np.array([[1,0,0,5],[0,1,0,10],[0,0,1,0],[0,0,0,1]])
M = M32*M21
P2 = np.dot(M,pos1)
print P2
# --- find screw parameters ----#
phi =  arccos((M[0][0]+M[1][1]+M[2][2]-1)/2)
sx = (M[2][1]-M[1][2])/(2*sin(the))
sy = (M[0][2]-M[2][0])/(2*sin(the))
sz = (M[1][0]-M[0][1])/(2*sin(the))
S1 =np.array([sx,sy,sz])
#print S1
#print phi*180/pi # deg 
#print pos1[0],pos1[1],pos1[2]
# --- diagram --- #
fig = plt.figure(1)
plt.plot([pos1[0],P2[0]],[pos1[1],P2[1]],[pos1[2],P2[2]],'x')
plot_user_defind(fig).coordinate_init()
plt.grid()
plt.show()
