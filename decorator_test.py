'''
def decorator(fn):
	def wrapper():
		print ('before executing fun')
		fn()
		print ('after executing fun')
	return wrapper

def fun():
	print('print from fun')


dec = decorator(fun)
dec()
'''
'''
import time
def decorator(fn):
	def wrapper():
		t1 = time.time()
		fn()
		t2 = time.time()
		return 'time it took to run the fun:'+ str((t2-t1)) + '\n'
	return wrapper

@decorator
def my_fun():
	num_list=[]
	for i in range(1000):
		num_list.append(i)
	print ('\n Sum of all numbers :'+ str(sum(num_list)))


print (my_fun())
'''

class A(object):
	def __init__(self):
		self._x,self._x_last=None,None
	def set_x(self,value):
		print('change the value of x')
		self._x_last=self._x
		self._x=value
	def get_x(self):
		print ('the value of x is : %d' %self._x)
		return self._x
	x=property(fget=get_x,fset=set_x)
	def get_x_last(self):
		print ('the last value of x is : %d' %self._x_last)
		return self._x_last
	x_last=property(fget=get_x_last)

ob=A()
ob.x=10.
ob.x=11
ob.x_last=10

