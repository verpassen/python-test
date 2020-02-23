import numpy as np
from scipy import pi,sin,cos,tan
import matplotlib.pyplot as plt
from Tkinter import *


class Mech():
	def __init__(self,L_Tool=130., L=210., ref_ang=0):
	 	self.Tool_tip,self.P_Baxis_pivot,self.P_Spindle_head=[],[],[]
		self.P_Baxis_pivot = np.asarray([600.,0 ,500.,1.])
		self.P_BaxisPivot2SpindleHead = np.asarray([0,0,-L,1])
		self.P_BaxisPivot2TCP = np.asarray([0,0,-L-L_Tool,1])
		M_B2Spindle_head = np.asarray([[1,0,0,0],[0,1,0,0],[0,0,1,-L],[0,0,0,1]])
		M_B2TCP = np.asarray([[1,0,0,0],[0,1,0,0],[0,0,1,-L-L_Tool],[0,0,0,1]])
		self.P_Spindle_head = np.dot(M_B2Spindle_head,self.P_Baxis_pivot.T)
		self.P_Tool_tip = np.dot(M_B2TCP,self.P_Baxis_pivot.T)

	def rad2deg(self,rad):
		return rad*pi/180

	def rot_Yaxis(self,rot_ang):
		rot_ang = self.rad2deg(rot_ang)
		Bx, By, Bz = self.P_Baxis_pivot[0],self.P_Baxis_pivot[1],self.P_Baxis_pivot[2]
		B_TCP_x ,B_TCP_y, B_TCP_z = self.P_BaxisPivot2TCP[0],self.P_BaxisPivot2TCP[1],self.P_BaxisPivot2TCP[2]
		
		M_B_rot_ang = np.asarray([[cos(rot_ang),0,sin(rot_ang),0],[0,1,0,0],[-sin(rot_ang),0,cos(rot_ang),0],
		[0,0,0,1]])
		M_Baxis_pivot2home = np.asarray([[1,0,0,Bx],[0,1,0,By],[0,0,1,Bz],[0,0,0,1]])
		
		tmp = np.dot(M_B_rot_ang,np.asarray([B_TCP_x,B_TCP_y,B_TCP_z,1]))
		self.P_Tool_tip2 = np.dot(M_Baxis_pivot2home,tmp)
		return self.P_Tool_tip2

machine1 = Mech()
print 'Position of spindle head :', machine1.P_Spindle_head
print 'Position of Tool tip:', machine1.P_Tool_tip
print 'Position of Tool tip after B axis rotating 90 deg:',machine1.rot_Yaxis(90.)


# ====== diagram ===== #
def plot_arrow(ax,data,delta,anp,an1,an2,color):
	org_X,org_Y = data[0], data[1]
	delta_X, delta_Y = delta[0],delta[1]
	hw, hl = 20.,20.
	shape = 'full'
	Sc = {'red':'r','green':'g','black':'k','Yellow':'y'}
	An_p={
		'1':[org_X+delta_X,org_Y+0.2*delta_Y,org_X-0.2*delta_X,org_Y+1.5*delta_Y],
		'2':[org_X+delta_X,org_Y-0.2*delta_Y,org_X+0.2*delta_X,org_Y+1.5*delta_Y],
 		'3':[org_X+delta_X,org_Y-0.2*delta_Y,org_X+0.2*delta_X,org_Y+1.5*delta_Y],
		'4':[org_X+delta_X,org_Y+0.2*delta_Y,org_X-0.2*delta_X,org_Y+1.5*delta_Y]
	}
	An_p['1'][0]
	ax.arrow(org_X,org_Y,org_X+delta_X,0,color=Sc[color],head_width=hw,head_length=hl)
	ax.arrow(org_X,org_Y,0,org_Y+delta_Y,color=Sc[color],head_width=hw,head_length=hl)
	ax.annotate(an1,xy = (An_p[anp][0],An_p[anp][1]),xycoords='data')
	ax.annotate(an2,xy = (An_p[anp][2],An_p[anp][3]),xycoords='data')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('Z axis[mm]')
ax.set_ylabel('X axis[mm]')
plt.plot(machine1.P_Baxis_pivot[2],machine1.P_Baxis_pivot[0],marker='o',markersize = 10)
plt.plot(machine1.P_Tool_tip2[2],machine1.P_Tool_tip2[0],marker='x',markersize = 5)
plt.plot(machine1.P_Tool_tip[2],machine1.P_Tool_tip[0],marker='x',markersize = 5,color = 'r')
plot_arrow(ax,[0,0],[150,150],'2','Z axis','X axis','black')
plot_arrow(ax,[machine1.P_Baxis_pivot[2],machine1.P_Baxis_pivot[0]],[150,150],'2','ZB axis','XB axis','green')
plt.grid()
ax.set_xlim([-50,1000])
ax.set_ylim(-50,1000)
plt.show()

'''
class gui:
	def __init__(self,parent):
		top = Toplevel(parent)
		L1 = Label(top,text='rotation angle').pack()
		self.e = Entry(top)
		self.e.pack()
		b1 = Button(top,text = 'OK',command = self.Ok)
	
	def Ok(self):
		print 'Value is' , self.e.get()
		self.top.destroy()


root = Tk()
w1 = gui(root)
root.mainloop()
'''




