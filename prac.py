import Tkinter as tk
from Tkinter import StringVar
import tkMessageBox   
from tkFileDialog import * 
class Application(tk.Frame):
	def __init__(self,master=None):	
		tk.Frame.__init__(self,master,width = 200,height = 200)
		self.grid(row = 0,column = 0)
		self.create_widget()
	def create_widget(self):
		self.user_input = StringVar()
		self.user_input.set('')
		self.user_password = StringVar()
		self.user_password.set('')
		self.menubar=tk.Menu(self.master)
		self.master.config(menu=self.menubar)
		self.filemenu=tk.Menu(self.menubar)
		self.filemenu.add_command(label='New')
		self.menubar.add_cascade(label='File',menu=self.filemenu)
 
		lbl1 = tk.Label(text='Username',fg='black')
		lbl1.grid(row = 1,column = 0)
		self.ent1 = tk.Entry()
		self.ent1.grid(row = 2 ,column = 0)
		lbl2 = tk.Label(text='Password',fg='black')
		lbl2.grid(row = 3,column = 0)
		self.ent2 = tk.Entry()
		self.ent2.config(show = '*')
		self.ent2.grid(row = 4,column = 0)
		btn1 = tk.Button(text = 'Login',fg = 'black',bg = 'white',command = self.check_user)
		btn1.grid(row = 5,column = 0)
		btn2 = tk.Button(text = 'Cancel' , fg= 'black' , bg= 'white',command = self.close_window)
		btn2.grid(row = 6,column = 0)
	def check_user(self):
		# call back the string in entry
		self.user_input = self.ent1.get()
		self.user_password = self.ent2.get()
		#print ('Current User is: ' + str(self.user_input))
		#print ('password is: ' + str(self.user_password))
		# check the user name is correct or not
		user = ['Mary','Brent','John','Jay']
		user_password={'Mary':['123'],'Brent':['libra03'],'John':['456'],'Jay':['1111']}
		if self.user_input in user:
			if self.user_password in user_password[str(self.user_input)]:
				if tkMessageBox.showinfo('Message','Pass!'):
					self.newwindow= tk.Toplevel(self.master)
					self.app=main_gui(self.newwindow)

			else:
				tkMessageBox.showinfo('Message','Password is not correct!Please try again!')
		else:
			tkMessageBox.showinfo('Message','The username is not registed !')

	def close_window(self):
		if tkMessageBox.askokcancel('Quit','You want to quit now?' ):
			root.destroy()				

class main_gui(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master,width=200,height=200)
		self.create_widget
	def create_widget(self):
		btn1=tk.Button(text='Test')
		btn1.grid(row=1,column=0)
		btn2=tk.Button(text='Close',command=self.close_window)
		btn2.grid(row=2,column=0)
	def close_window(self):
		if		tkMessageBox.askokcancel('Quit','You want to close the window?'):
			self.master.destroy()
				



root=tk.Tk()
root.title('Test')
gui=Application(master = root)
root.mainloop()


