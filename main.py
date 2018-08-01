import numpy as np 
from scipy import pi,sin,cos
from rigidbody import *

#-------------------------
#E_x0w 
#E_y0w
# WKS to Reference Frame
#T_R2W = np.matrix([[],[],[],[]])

#---------------------#
#---Transformation----#
#---------------------#
class HTH:
    @classmethod
    def R_x(self,ang):
        return np.matrix([[1,0,0,0],[0,cos(ang),-sin(ang),0],[0,sin(ang),cos(ang),0],[0,0,0,1]])
    @classmethod
    def R_y(self,ang):
        return np.matrix([[cos(ang),0,sin(ang),0],[0,1,0,0],[-sin(ang),0,cos(ang),0],[0,0,0,1]])
    @classmethod
    def R_z(self,ang):
        return np.matrix([[cos(ang),-sin(ang),0,0],[sin(ang),cos(ang),0,0],[0,0,1,0],[0,0,0,1]])
    @classmethod
    def T_x(self,d):
        return np.matrix([[1,0,0,d],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    @classmethod
    def T_y(self,d):
        return np.matrix([[1,0,0,0],[0,1,0,d],[0,0,1,0],[0,0,0,1]])
    @classmethod
    def T_z(self,d):
        return  np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,d],[0,0,0,1]])

#--- Workpiece ---#
# WKS to Reference #
err_x = 0.01 
err_y = -0.01
err_zw = 0.00
L_w = 50.
T_w2R = T_x(err_x)*T_y(err_y)*R_z(err_zw)*T_z(L_w)

#--- Tool to Reference ---#
# Tool offset #
T_x,T_z = 20, 100.


# Kinemtics
# 5 axis machine should define the 4th and 5th axis rotary axis
# T type - Head-Head
# P type - Table-Table
# M type - Head-Table
# define the vector of the rotary axis
# rotate respect to the X axis = V : [1,0,0]
# rotate respect to the Y axis = V : [0,1,0]
# rotate respect to the Z axis = V : [0,0,1]
p = np.asarray([0,0,0,1])
v1 =[0,1,0]
v2 =[0,0,1]
B_ang = 80*pi/180

E_B = HTH.R_y(B_ang)
print(E_B)