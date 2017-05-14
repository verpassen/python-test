import numpy as np 
from rigidbody import *
# --- position ---#
a1 = np.array([50,0,10])
a2 = np.array([50,0,0])
b1 = np.array([400,0,140])
b2 = np.array([-300,0,140])

L1 = normalized(a1 - a2)
L2 = normalized(b1 - b2)

pos1 = np.array([150,200,50])
# === transform matrix === #
T1 = SE3.Atlas()
T1.position = a1
T1.orientation = L1
class P:
	def __init__(self,x):
		self.x = x
	@property
	def x(self):
		return self.x
	@x.setter
	def x(self,x):
		assert self.x <0,'value of x is out of range'
		self.x = x
		'''
		if x <0:
			self.__x = 0
		elif x>1000:
			self.__x = 1000
		else:
			self.__x = x
		'''

p1 = P(40)
print p1.x
p1.x= -10
print p1.x



