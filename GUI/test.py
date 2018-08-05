#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Jul 08, 2018 08:38:48 PM
import sys
import numpy as np 
from scipy import pi,sin,cos,tan,arcsin,arccos,arctan
 
from math import sqrt
import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.patches as patches

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import test_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    test_support.set_Tk_var()
    top = Polygon_Tool_Path (root)
    test_support.init(root, top)
    root.mainloop()

w = None
'''
def create_Polygon_Tool_Path(root, *args, **kwargs):
    #Starting point when module is imported by another program.
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    test_support.set_Tk_var()
    top = Polygon_Tool_Path (w)
    test_support.init(w, top, *args, **kwargs)
    return (w, top)
'''
def destroy_Polygon_Tool_Path():
    global w
    w.destroy()
    w = None


class Polygon_Tool_Path:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+488+185")
        top.title("Polygon Tool Path")
        top.configure(highlightcolor="black")
        top.bind('<Escape>',quit)
        
        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.03, rely=0.07, relheight=0.57, relwidth=0.49)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=295)
        
        
        self.Lt = Entry(top)
        self.Lt.place(relx=0.58, rely=0.11, relheight=0.04, relwidth=0.24)
        self.Lt.configure(background="white")
        self.Lt.configure(font="TkFixedFont")
        self.Lt.configure(selectbackground="#c4c4c4")
        self.Lt.configure(textvariable=test_support.Lt)
        
        self.Label_Tool_Length = Label(top)
        self.Label_Tool_Length.place(relx=0.58, rely=0.04, height=22, width=97)
        self.Label_Tool_Length.configure(activebackground="#f9f9f9")
        self.Label_Tool_Length.configure(text='''Tool length[mm]''')

        self.Label_Delta_angle = Label(top)
        self.Label_Delta_angle.place(relx=0.58, rely=0.18, height=22, width=117)
        self.Label_Delta_angle.configure(activebackground="#f9f9f9")
        self.Label_Delta_angle.configure(text='''Angle deviation[deg]''')

        self.Ang_delta = Entry(top)
        self.Ang_delta.place(relx=0.58, rely=0.24, relheight=0.04, relwidth=0.24)
        self.Ang_delta.configure(background="white")
        self.Ang_delta.configure(font="TkFixedFont")
        self.Ang_delta.configure(selectbackground="#c4c4c4")
        self.Ang_delta.configure(textvariable=test_support.Ang_delta)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.63, rely=0.91, height=30, width=63)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(command=self.show)
        self.Button1.configure(text='''OK''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.77, rely=0.91, height=30, width=65)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(command=test_support.destroy_window)
        self.Button2.configure(text='''Cancel''')
        self.Button2.bind('<B1-Key>',lambda p:test_support.Button2Click(p))

        self.n = Entry(top)
        self.n.place(relx=0.58, rely=0.38, relheight=0.04, relwidth=0.24)
        self.n.configure(background="white")
        self.n.configure(font="TkFixedFont")
        self.n.configure(selectbackground="#c4c4c4")
        self.n.configure(textvariable=test_support.n)
        
        self.Label_no_of_edge = Label(top)
        self.Label_no_of_edge.place(relx=0.57, rely=0.31, height=22, width=117)
        self.Label_no_of_edge.configure(activebackground="#f9f9f9")
        self.Label_no_of_edge.configure(text='''Number of Edge''')

        self.Label_Rc = Label(top)
        self.Label_Rc.place(relx=0.58, rely=0.47, height=22, width=145)
        self.Label_Rc.configure(activebackground="#f9f9f9")
        self.Label_Rc.configure(text='''Radius of the Circle[mm]''')

        self.Label_Rf = Label(top)
        self.Label_Rf.place(relx=0.58, rely=0.6, height=22, width=139)
        self.Label_Rf.configure(activebackground="#f9f9f9")
        self.Label_Rf.configure(text='''Radius of the fillet[mm]''')

        self.Rc = Entry(top)
        self.Rc.place(relx=0.58, rely=0.51, relheight=0.04, relwidth=0.24)
        self.Rc.configure(background="white")
        self.Rc.configure(font="TkFixedFont")
        self.Rc.configure(selectbackground="#c4c4c4")
        self.Rc.configure(textvariable=test_support.Rc)
        
        self.Rf = Entry(top)
        self.Rf.place(relx=0.58, rely=0.64, relheight=0.04, relwidth=0.24)
        self.Rf.configure(background="white")
        self.Rf.configure(font="TkFixedFont")
        self.Rf.configure(selectbackground="#c4c4c4")
        self.Rf.configure(textvariable=test_support.Rf)
        
        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.03, rely=0.67, relheight=0.05
                , relwidth=0.14)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''Tool Path''')
        self.Checkbutton1.configure(textvariable=test_support.on_ToolPath)
        self.Checkbutton1.configure(variable=test_support.che46)

        self.Checkbutton2 = Checkbutton(top)
        self.Checkbutton2.place(relx=0.03, rely=0.73, relheight=0.05
                , relwidth=0.09)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Tool''')
        self.Checkbutton2.configure(textvariable=test_support.on_Tool)
        self.Checkbutton2.configure(variable=test_support.che47)

        self.Checkbutton3 = Checkbutton(top)
        self.Checkbutton3.place(relx=0.03, rely=0.8, relheight=0.05
                , relwidth=0.12)
        self.Checkbutton3.configure(activebackground="#d9d9d9")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''Spindle''')
        self.Checkbutton3.configure(textvariable=test_support.on_Spindle)
        self.Checkbutton3.configure(variable=test_support.che48)
        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.5, rely=0.82, height=30, width=57)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(command=self.DraftClear)
        self.Button3.configure(text='''Clear''')
        
        # Entry default value        
        test_support.Lt.set(78)
        test_support.Rf.set(20)
        test_support.Rc.set(50)
        test_support.n.set(6)
        test_support.Ang_delta.set(1)
        
    def show(self):
        self.calculation()
        #self.canvas = FigureCanvasTkAgg(self.f,self.Frame1)
        #self.canvas.get_tk_widget().pack()
        self.Frame1.update()
        print('buton pressed')
    def get_Val(self):
        global n,Rf,Rc,Ang_delta,Lt
        Lt = float(self.Lt.get())
        n = int(self.n.get())
        Rf = float(self.Rf.get())
        Rc = float(self.Rc.get())
        Ang_delta = float(self.Ang_delta.get())
   
    def calculation(self):
        self.get_Val()
        print(n,Rf,Rc,Ang_delta,Lt)
        S = Rc/cos(pi/n) 
        r2 = Rf/Rc*S
        Upper_phi = arccos(Rc/r2)
        Upper_the = arctan(Rf*sin(Upper_phi)/(S-r2*sin(Upper_phi)**2))
        
        the = np.linspace(0,2*pi/n,360)
        phi = np.linspace(0,2*pi,360)
        X,Y,S_x,S_y=[],[],[],[]
        P_x,P_y,D_p=[],[],[]
        for k in range(len(the)):
        	if the[k] < Upper_the:
        		a = 1 + tan(the[k])**2
        		b = -2*(S-r2)
        		c = (S-r2+Rf)*(S-r2-Rf)
        		X.append((-b+sqrt(b**2-4*a*c))/2/a)
        		Y.append(tan(the[k])*X[k])
        	elif (max(the)-Upper_the)<=the[k]:
        		a = 1 + tan(the[k])**2
        		b = -2*(S-r2)*(cos(2*pi/n)+sin(2*pi/n)*tan(the[k]))
        		c = (S-r2)**2-Rf**2
        		X.append((-b+sqrt(b**2-4*a*c))/2/a)
        		Y.append(tan(the[k])*X[k])
        	else:
        		X.append(S/(1+tan(the[k])*tan(pi/n)))
        		Y.append(tan(the[k])*X[k])
        		
        self.f = Figure(figsize=(5,5),dpi=80)
        a = self.f.add_subplot(111,aspect='equal')
        a.add_patch(patches.Circle((0,0),Rc,fill=False))
        for i in range(n):
        	ang = i*2*pi/n
        	M = np.matrix([[cos(ang),-sin(ang),0],[sin(ang),cos(ang),0],[0,0,1]])
        	for k in range(len(the)):
        		tmp = np.dot(M,np.array([X[k],Y[k],1]))
        		P_x.append(tmp[0,0])
        		P_y.append(tmp[0,1])
        		D_p.append(sqrt(tmp[0,0]**2+tmp[0,1]**2))
        
         
        phi = np.linspace(0,2*pi,n*360)
        for i in range(len(phi)):
        	P1 = np.array([-Lt,0,1])
        	M12 = np.matrix([[cos(phi[i]),-sin(phi[i]),D_p[i]*cos(phi[i])],[sin(phi[i]),cos(phi[i]),D_p[i]*sin(phi[i])],[0,0,1]])
        	P2 = np.dot(M12,P1)
        	S_x.append(P2[0,0])
        	S_y.append(P2[0,1])
        		
        a.plot(P_x,P_y)	
        a.plot(S_x,S_y)	
        
        self.canvas = FigureCanvasTkAgg(self.f,self.Frame1)
        self.canvas.get_tk_widget().pack()
 
    def DraftClear(self):
        #self.Frame1.destory()
        pass
        '''
        f.clf()
        self.canvas = FigureCanvasTkAgg(self.f,self.Frame1)
        self.canvas.get_tk_widget().pack()
        '''
    def on_press(self,event):
        'when "ok" is pressed '
        
if __name__ == '__main__':
    vp_start_gui()



