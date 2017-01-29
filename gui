#-*-coding: UTF-8 -*-
from Tkinter import Tk,Frame,Menu,StringVar
from Tkinter import Button,Canvas,Label,Entry,Toplevel
import tkMessageBox
import tkFileDialog as filedialog
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import numpy as np

fig1 = Figure(figsize=(5,4))
ax=fig1.add_subplot(111)
t=np.arange(0,3,0.01)
y=np.sin(t)
ax.plot(t,y)

class app1(Frame):
	def __init__(self,parent):
 		Frame.__init__(self,parent)
 		self.parent=parent
 		self.create_widget()
		self.select_tool(self.parent)		
 	def create_widget(self):
 		self.parent.title('Simple test')
 		menubar=Menu(self.parent)
 		self.parent.config(menu=menubar)
		# ==== menubar === #
		filemenu_elem={'New':self.onExit,'Open':self.open_file,'Save':self.save_file,'Save as':self.save_as_file}
		editmenu_elem=['Copy','Paste','Select all']
		viewmenu_elem=['One window','Parallel','Vertical']
		toolbarmenu_elem=['FFT','Wavelet analysis']
		helpmenu_elem=['Help','About']
 		filemenu=Menu(menubar)
 		menubar.add_cascade(label='File',menu=filemenu)
		
		for elem in filemenu_elem:	
			filemenu.add_command(label=elem,command=filemenu_elem[elem])

		filemenu.add_separator()
		filemenu.add_command(label='Exit',command=self.onExit)

		editmenu=Menu(menubar)
		menubar.add_cascade(label='Edit',menu=editmenu)
		for elem in editmenu_elem:
			editmenu.add_command(label=elem)
 		
		viewmenu=Menu(menubar)		
		menubar.add_cascade(label='View',menu=viewmenu)
		for elem in viewmenu_elem:
			viewmenu.add_command(label=elem)

		toolbarmenu=Menu(menubar)
		menubar.add_cascade(label='Tool',menu=toolbarmenu)
		for elem in toolbarmenu_elem:
			toolbarmenu.add_command(label=elem)

		helpmenu=Menu(menubar)		
		menubar.add_cascade(label='Help',menu=helpmenu)
 		helpmenu.add_command(label='Help',command=self.save_file)
		helpmenu.add_command(label='About',command=self.help_info)
		menubar=Menu(self.parent)
		
		#===== tools ===#
	def select_tool(self,master):
		win1=FigureCanvasTkAgg(fig1,master=master)
		win1.show()
		win1.get_tk_widget().pack(side='top')
    
		#===== Button ====#
		btn1=Button(text='Ok')
		#btn1.pack(side=RIGHT,anchor=E)
		btn1.place(relx=0,anchor='center')
		btn2=Button(text='Close',command=self.onExit)
		#btn2.pack(side=RIGHT,anchor=E)
		btn2.place(relx=0,anchor='center')
		#==== check_box ===#

	def open_file(self):
		self.open_file_Dial=filedialog.open(defaultextension='.txt')	
 	def save_file(self):
		#取得目前開啟檔案的名稱,還沒寫						 
		self.save_file_Dial=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
	def save_as_file(self):
		self.save_as_file_Dial=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
 	def onExit(self):
		self.quit()
	def open_file(self):
		self.open_file_Dial=filedialog.askopenfilename(filetypes=[('text files','*.txt')])
		open_file_name = self.open_file_Dial.read.read()
		self.open_file_Dial.close()
	def help_info(self):
		title='About GUI'
		info='Version 1.0\n  Written by Brent'
		tkMessageBox.showinfo(title,info.center(40))
 

root=Tk()
gui=app1(parent=root)
root.mainloop()
