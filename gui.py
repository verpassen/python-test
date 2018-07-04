from tkinter import Tk, Label, Button,Entry
import Tkinter as tk
class MyFirstGUI(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self,master)
        self.grid() 
        self.createWidget()
    def createWidget(self):
        self.label = Label(self, text="This is our first GUI!")
        self.label.pack()
        self.greet_button = Button(self, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.close_button = Button(self, text="Close", command=self.quit)
        self.close_button.pack()
        self.label2 = Label(self,text='angle')
        self.label2.pack()
        self.entry = Entry(self,validate='key')
        self.entry.pack()
        self.label3 = Label(self,text = 'number of edge')
        self.label3.pack() 
        self.entry2 = Entry(self,validate='n')
        self.entry2.pack()
        
    def greet(self):
        print('Greeting')
        print(n)
        print(key)

my_gui = MyFirstGUI()
my_gui.master.title('A simple GUI')
my_gui.mainloop()

