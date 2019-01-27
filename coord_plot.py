from Tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from mpl_toolkits.mplot3d import Axes3D

#matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class gui:
    def __init__(self,master):
        frames = Frame(master)
        master.geometry("500x500")
        master.title("Test Coord plot")
        master.configure(highlightcolor="black")
        frames.pack()
        self.f = Figure(figsize=(10,10))
        self.canvas = FigureCanvasTkAgg(self.f,frames)
        self.canvas.get_tk_widget().pack(expand=1)
        self.zero = np.zeros(3)
        self.add_wcs([1,2,0],np.array([1,0,0]),np.array([0,1,0])
    def add_wcs(self,pos,v1,v2):
        ax = self.f.add_subplot(111,projection='3d')
        N_v1 = self.noralv(v1)
        N_v2 = self.noralv(v2)
        N_v3 = np.cross(N_v1,N_v2)
        nP1,nP2,nP3 = [(pos + k) for k in [N_v1,N_v2,N_v3]]
        
        print (nP1,nP2,nP3)
        x,y,z = zip(pos,nP1)
        
        print ('(X,Y,Z) = (%4.3f,%4.3f,%4.3f)' % (x,y,z))
        ax.plot(x,y,z,'-r',linewidth=3)
        x,y,z = zip (pos,nP2)
        ax.plot(x,y,z,'-g',linewidth=3)
        x,y,z = zip (pos,nP3)
        ax.plot(x,y,z,'-b',linewidth=3)    
 
        
    def noralv(self,v):
        return v/sqrt((v**2).sum())


root = Tk()
w1 = gui(root)
 

#w1.add_wcs([10,0,-5],np.array([0,1,0]),np.array([1,0,0])
root.mainloop()

