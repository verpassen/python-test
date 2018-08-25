import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as patches

class diagram:
    def __init__(self):
        #fig = plt.figure(figsize=(100,200),dpi=80)
        #ax = fig.add_subplot()
        fig, ax = plt.subplots(figsize=(100,200),dpi=80)
        r1 = patches.Rectangle((50,80),100,200,0)
        ax.add_patch(r1)
        self.show()
    def show(self):
        plt.show()

w1 = diagram()
w1.show()
