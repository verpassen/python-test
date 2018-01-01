import numpy as np
from scipy import pi,cos,sin,tan
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
class plot_cone():
    def __init__(self,R,alpha):
        self.R = R
        self.phi = np.linspace(0,360,720)
        self.l = np.linspace(0,self.R/sin(alpha),len(self.phi))
        self.alpha =alpha
        self.r = self.l*sin(alpha)

    def show_diagram(self):
        x = self.r*cos(self.phi)
        y = self.r*sin(self.phi)
        z = np.linspace(0,self.R/tan(self.alpha),len(self.phi))
        #---
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x,y,z)
        ax.axis('equal')
        ax.grid()
        plt.show()
    

A = plot_cone(10,45)
A.show_diagram()
'''
l = np.array([0,0,100])
h = np.array([25,0,210])
#---- axis init value. ---#
alpha = 30. # deg
phi = 0.   # deg

# ---- 
V_l = np.array([l[0],l[1],l[2]])
V_h = np.array([h[0],h[1],h[2]])
V_2nd_To_1st_RotX = np.matrix([[cos(phi),-sin(phi),0,-h[0]],[sin(phi),cos(phi),0,-h[1]],[0,0,1,-h[2]],[0,0,0,1]])
V_tool_To_2nd_RotX = np.matrix([[1,0,0,0],[0,cos(alpha),-sin(alpha),0],[0,sin(alpha),cos(alpha),0],[0,0,0,1]])

R = np.multiply(V_2nd_To_1st_RotX,V_tool_To_2nd_RotX)


Pw = np.multiply(R,np.insert(-V_l,3,1))
Qw = np.multiply(R,np.insert(-V_h,3,1))
print(np.insert(-V_l,3,1))
print (Pw)

#Pm=np.array([Xp,Yp,Zp,Alpha,phi])
#Pw=np.array([Xw,Yw,Zw,1])
