import numpy as np
from numpy import sin,cos
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from collections import deque
# matplotlib 動畫測試
# check info
# change these code to animation 
# including a rolling circle and the trace 

def myfun(the,x):
	M = np.array([[cos(the),sin(the),x[1]*the],[-sin(the),cos(the),0],[0,0,1]])
	N = np.dot(M,x.transpose())
	return N[0],N[1]

def draw_Cir(Radius,i):
	the = np.arange(0,2*np.pi,1/100)  
	return Radius*cos(the)+i*Radius,Radius*sin(the)

Dia = 50 
Pt = np.array([0,Dia/2,1])
theta = np.arange(0,6*np.pi,1/100)
x,y=[],[]
for j in theta:
	x.append(myfun(j,Pt)[0])
	y.append(myfun(j,Pt)[1])

fig = plt.figure()
ax = fig.add_subplot(autoscale_on=False,xlim=(-150,1000),ylim=(-50,100))

line, = ax.plot([],[],'g-')
circle, = ax.plot([],[],'r')
trace, = ax.plot([],[],'bx')
ax.set_aspect('equal')
history_x,history_y = deque(maxlen=300),deque(maxlen=300)
def animation(i):
	cir_x = draw_Cir(Dia/2,i)[0]
	cir_y = draw_Cir(Dia/2,i)[1]
	thisx = myfun(i,Pt)[0]
	thisy = myfun(i,Pt)[1]
	barx = [thisx, i*Pt[1]]
	bary = [thisy, 0]
	if i == 0:
		history_x.clear()
		history_y.clear()

	history_x.append(thisx)
	history_y.append(thisy)

	trace.set_data(history_x,history_y)
	circle.set_data(cir_x,cir_y)
	line.set_data(barx,bary)
	return circle,trace,line,

ani = FuncAnimation(fig,animation,frames=100,interval=100,blit=True,cache_frame_data=False,repeat=True)	
plt.show()

