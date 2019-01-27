import numpy as np
from scipy import sin,cos,pi
import  matplotlib.pyplot as plt 
import matplotlib.animation as animation 

fig, ax = plt.subplots()
the,r = 0,1.5
line, = ax.plot([0,r*np.cos(the)],[0,r*np.sin(the)])
f1=lambda k:r*cos(k)
f2=lambda k:r*sin(k)
line,=ax.plot(f1(the),f2(the))
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

def init():
    line.set_data([-15,15],[-15,15])
    plt.axis('equal')
    return line,

def animate(i):
    line.set_data([0,r*cos(the+i/10.0)],[0,r*sin(the+i/10.0)])
    return line,



ani = animation.FuncAnimation(fig,animate,np.arange(1,360),init_func=init,interval = 10, blit=True)
plt.show()
