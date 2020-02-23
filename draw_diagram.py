import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg

class diagram:
    def __init__(self):
        #fig = plt.figure(figsize=(100,200),dpi=80)
        #ax = fig.add_subplot()
        # if the figsize is too big, it shows there are not engough free memory for image buffer
        fig, ax = plt.subplots(figsize=(20,10),dpi=80)
        r1 = patches.Rectangle((10,10),10,20,3)
        ax.add_patch(r1)
        canvas = FigureCanvasTkAgg(fig)
        toolbar = NavigationToolbar2TkAgg
        self.show()
    def show(self):
        plt.show()

w1 = diagram()
w1.show()

