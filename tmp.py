from tkinter import * 


class test:
    def __init__(self,master):
        self.a = 10
        self.b = 5
        w1 = Entry(width=10)
        C =DoubleVar()
        C.set(10)
        self.math_a()
        self.math_b()
        B1 = Button(width=10,text='ok',command=self.button_click())
        w1.pack()
        B1.pack()
    def math_a(self):
        return (self.a)#+C)
    def math_b(self):
        return (self.b)#+C)
    def button_click(self):
        print(C)


root = Tk()
obj = test(root)

root.mainloop()


