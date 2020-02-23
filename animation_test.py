import numpy as np
from scipy import pi,sin,cos
import matplotlib.pyplot as plt
from matplotlib import animation 

fig=plt.figure()
ax=plt.axes(xlim=(0,10),ylim=(-2,2))
line,=ax.plot([],[],lw=2)
line2,=ax.plot([],[],'o-',markersize=20,lw=2,color='r')

def init():
	line.set_data([],[])
	line2.set_data([],[])
	return line 

def animate1(i):
	N=2**10
	x=np.linspace(0,4*pi,N)
	marker_x=1.
	y=sin(x-0.1*i)
	marker_y=sin(marker_x-0.1*i)
	line.set_data(x,y)
	line2.set_data(marker_x,marker_y)
	return line,line2

ani=animation.FuncAnimation(fig,animate1,init_func=init,blit=True,frames=200,interval=10)
plt.show()

 
