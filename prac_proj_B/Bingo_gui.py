#!/usr/bin/env python 
#-*- coding:utf-8 -*- 
from tkinter import * 
from tkinter.messagebox import *
from tkinter.filedialog import *
import numpy as np 
from rand_square import * 

class gui:
	def __init__(self,master):
		frame =Frame(master)
		#-----self defined variables----#		
		self.sampling_qty=IntVar(value=6)
		self.create_widget()
		
	def create_widget(self):	
		self.w = Canvas(width=800,height=800)		 
		# plot the square 
		[self.w.create_line(0,k,300,k,fill="#470642",width=3) for k in range(0,350,50)]
		[self.w.create_line(k,0,k,300,fill="#470642",width=3) for k in range(0,350,50)]
		
		# create button and entry widget
		B1 = Button(width=15,height=3,text='Clear',command=self.txt_clear).grid(row=3,column=5)
		B2 = Button(width=15,height=3,text='Check',command=self.check_connect).grid(row=3,column=4)
		B3 = Button(width=15,height=3,text='New',command=self.create_rand_sqr).grid(row=3,column=3)
		L1 = Label(width=35, height=10,text='Sampling Number Quantity').grid(row=2,column=1)
		self.E1 = Entry(width = 15,textvariable=self.sampling_qty).grid(row=2,column=3)
		self.w.grid( )

	def create_rand_sqr(self):
		# create random square
		val_entry = self.sampling_qty.get()
		if self.sampling_qty != val_entry:
			self.sampling_qty.set(val_entry)
		#print(self.sampling_qty)
		#print(val_entry)
		self.data = create_rand_sqr(6)
		for s in range(25,325,50):
			for k in range(25,325,50):
				x,y = int(s/50),int(k/50)
				txt_content = self.data[x][y]
				self.w.create_text(k,s,text=txt_content,font=20)

		#create random sample number list 
		pop_list = np.arange(1,36)
		self.rand_list = sorted(create_rand_list(pop_list,val_entry))
		self.w.create_text(400,50,text='Lucky number',font=20)
		for s in range(len(self.rand_list)):
			txt_content = self.rand_list[s]
			k = 400 + (s%5)*50
			if len(self.rand_list) > 5:			
				self.w.create_text(k,120+50*(s//5),text=txt_content,font=20)

	def create_circle(self,x,y,r,**kwargs):
		return self.w.create_oval(x-r,y-r,x+r,y+r,**kwargs)

	def check_connect(self): 
		Matrix_C,s = check_line(self.rand_list,self.data)
		len_x,len_y = Matrix_C.shape[0],Matrix_C.shape[1]
		for x in range(len_x):						
			for y in range(len_y):			
				if Matrix_C[x][y] == 1:				
					self.create_circle(25+50*y,25+50*x,15,outline='#FF0000',width=2)

	def txt_clear(self):
		self.w.delete('all')		
		[self.w.create_line(0,k,300,k,fill="#470642",width=3) for k in range(0,350,50)]
		[self.w.create_line(k,0,k,300,fill="#470642",width=3) for k in range(0,350,50)]
		

root = Tk()
app = gui(root)
root.mainloop()
