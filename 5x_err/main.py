import numpy as np 
from scipy import pi,sin,cos
from rigidbody import *

#-------------------------
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

class machine_1:
    def __init__(self):
        # initialize
        #e_xcz,e_ycz,e_xbs,e_zcz,e_zbs = 0.001, -0.002,0.002, 0.001, 0.001
        #Ang_xcz,Ang_xzt,Ang_xbs,Ang_xbx,Ang_yzt = 0,0,0,0.02,0
        e_xcz,e_ycz,e_xbs,e_zcz,e_zbs = 0.00, 0.00,0.00, 0.00, 0.00
        Ang_xcz,Ang_xzt,Ang_xbs,Ang_xbx,Ang_yzt = 0,0,0,0,0
        Ang_ycz,Ang_yxb,Ang_zxb,Ang_zyx = 0,0,0,0
        self.linear_deviation = [e_xcz,e_ycz,e_xbs,e_zcz,e_zbs]
        self.Angular_deviation = [Ang_xcz,Ang_xbx,Ang_xbs,Ang_xzt,Ang_ycz,Ang_yzt,Ang_yxb,Ang_zyx,Ang_zxb]
    def set_ball_pos(self,_ind,x,y,z):
        #if _ind equal 1, setting of the tool spindle side
        #if _ind equal 2, setting of the work spindle side
        if _ind:
            if _ind == 1: 
                P_T = np.array([x,y,z,1]).reshape(4,1)
                return P_T
            elif _ind == 2:
                P_S = np.array([x,y,z,1]).reshape(4,1)
                return P_S
        else:
            print('Argurments are not sufficient')
        
            
#--- Workpiece ---#
#--- Define the deviation variable
root = machine_1
e_xcz,e_ycz, e_xbs,e_zcz,e_zbs = root().linear_deviation
Ang_xcz,Ang_ycz,Ang_xzt,Ang_yzt, Ang_zyx, Ang_xbx, Ang_yxb,Ang_zxb, Ang_xbs=root().Angular_deviation
#--- Tool to Reference ---#
# Tool offset #
Raz, Rax= 0, 100.

# Kinemtics
# 5 axis machine should define the 4th and 5th axis rotary axis
# T type - Head-Head
# P type - Table-Table
# M type - Head-Table
B_ang = 90*pi/180
C_ang = 30*pi/180
#--- Define transformation matrix ---#
E_B = HTH.R_y(B_ang)
E_C = HTH.R_z(C_ang)
D_alpha_XB = HTH.R_x(Ang_xbs)
D_alpha_BS = HTH.R_x(Ang_xbs)
D_alpha_XB  = HTH.R_x(Ang_xbx)
D_alpha_CZ = HTH.R_x(Ang_xcz)
D_beta_XB = HTH.R_y(Ang_yxb)
D_beta_CZ  = HTH.R_y(Ang_ycz)
D_garma_XB = HTH.R_z(Ang_zxb)

#--- tool spindle side ball ---#
P = np.array([0,0,-Raz,1])
P_SB = D_alpha_BS*P.reshape(4,1)+np.array([e_xbs,0,e_zbs,0]).reshape(4,1)
P_SM = D_garma_XB*D_beta_XB*D_alpha_XB*E_B*P_SB

#--- work spindle side ball ---#
P_T = root().set_ball_pos(1,10,20,30)
P_XTM1 = P_T+ D_garma_XB*D_beta_XB*D_alpha_XB*np.array([0,0,-Raz,0]).reshape(4,1)+np.array([e_xbs,0,e_zbs+Raz,0]).reshape(4,1)
P_XTM2 = P_XTM1 - np.array([e_xcz,e_ycz,0,0]).reshape(4,1)-D_beta_CZ*D_alpha_CZ*P_XTM1-P_XTM1
P_BallT =  D_beta_CZ*D_alpha_CZ*E_C*P_XTM2+np.array([e_xcz,e_ycz,0,0]).reshape(4,1)
    
print 'Ball of tool spindle side :'+ str(P_SM[0:3])
print 'Ball of work spindle side : '+str(P_BallT[0:3])

