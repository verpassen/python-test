import Tkinter as tk
from Tkinter import StringVar
#from tkMessageBox import * 
#from tkFileDialog import * 

class Application(tk.Frame):
	def __init__(self,master=None):	
		tk.Frame.__init__(self,master,width = 200,height = 200)
		self.grid(row = 0,column = 0)
		self.create_widget()
	def create_widget(self):
		self.user_input = StringVar()
		self.user_input.set('')
		lbl1 = tk.Label(text='Username',fg='black')
		lbl1.grid(row = 1,column = 0)
		ent1 = tk.Entry()
		ent1.grid(row = 2 ,column = 0)
		lbl2 = tk.Label(text='Password',fg='black')
		lbl2.grid(row = 3,column = 0)
		ent2 = tk.Entry()
		ent2.grid(row = 4,column = 0)
		btn1 = tk.Button(text = 'Login',fg = 'black',bg = 'white',command = self.check_user)
		btn1.grid(row = 5,column = 0)
	def check_user(self):
		user = ['Mary','Brent','John','Jay']
		if user_input in user:
			pass
		else:
			tk.Message(text = 'The username is not registed !')

root=tk.Tk()
root.title('Test')
gui=Application(master = root)
root.mainloop()
