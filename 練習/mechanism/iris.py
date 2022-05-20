import numpy as np
from numpy import sin,cos
import matplotlib.pyplot as plt 
import matplotlib
# issues 
'''
1. The main class have to be fixed 
2. how to create the linkage connect two blocks
3. 
'''
#
# linkage setup 
n = 12 
R = 100
D_angle =2*np.pi/n
section = 720 # 
Link_Rot_ang = -2*np.pi/4
phi = np.linspace(0,Link_Rot_ang,section) 
# ----
# setup
B_plot = 1
B_showInfo = 0
XLimit,YLimit = 300,300  # Diagram Range limit in X & Y axis 

# ----
# object class 
class Pivot:
	def __init__(self):
		self.x =[]
		self.y =[]

class Link:
	def __init__(self,Len,n,Origin):
		# self.ang = 2*np.pi/n
		self.L = 2*cos(D_angle)*Len
		self.A = np.array([Len*cos(D_angle),Len*sin(D_angle),1])
		self.B = np.array([self.L,0,1])
	
def Tran_M(shift_phase,ang,Org):
	# n is the n_th Pivto point 
	x,y = Org[0],Org[1]
	M = np.array([[cos(shift_phase+ang),-sin(shift_phase+ang), x],
		[sin(shift_phase+ang) ,cos(shift_phase+ang),y],
		[0,0,1]])
	return M

def plot_diagram(A,B):
	# k is the number of the pivot
	plt.plot(Org.x,Org.y,'D')
	plt.plot(A.x,A.y,'D')
	plt.plot(B.x,B.y,'D')
	plt.legend(['O','A','B'])
	plt.plot([A.x,Org.x,N_B.x],[A.y,Org.y,B.y],'b--')
	 
	
the = np.linspace(0,2*np.pi,n+1)
 
O = Pivot()
for deg in the[:-1] :
	O.x.append(R*cos(deg))
	O.y.append(R*sin(deg)) 

shift_deg = [ np.pi + (j-1)*D_angle for j in range(n)]

LinkJJ = []
N_A,N_B, Org= Pivot(), Pivot(),Pivot()
if B_plot == 1:
	fig  = plt.figure()
	ax = fig.add_subplot(111,xlim=(-XLimit,XLimit),ylim=(-YLimit,YLimit))
	ax.set_aspect('equal')
	plt.xlabel('X')
	plt.ylabel('Y') 
	plt.grid()

	# for j in range(n):
	for j in range(2):
		Org.x , Org.y = O.x[j], O.y[j]
		LinkJJ.append(Link(R,n,[Org.x,Org.y]))
		# for deg in phi:
		M = Tran_M(shift_deg[j],deg,[Org.x,Org.y])
		N_A.x = np.dot(M,LinkJJ[j].A.transpose())[0]
		N_A.y = np.dot(M,LinkJJ[j].A.transpose())[1]
		N_B.x = np.dot(M,LinkJJ[j].B.transpose())[0]
		N_B.y = np.dot(M,LinkJJ[j].B.transpose())[1]

		plot_diagram(N_A,N_B)

	plt.show()
else:
	for j in range(2):
		Org.x , Org.y = O.x[j], O.y[j]
		LinkJJ.append(Link(R,n,[Org.x,Org.y]))
		for deg in phi:
			M = Tran_M(shift_deg[j],deg,[Org.x,Org.y])
			N_A.x.append(np.dot(M,LinkJJ[j].A.transpose())[0])
			N_A.y.append(np.dot(M,LinkJJ[j].A.transpose())[1])
			N_B.x.append(np.dot(M,LinkJJ[j].B.transpose())[0])
			N_B.y.append(np.dot(M,LinkJJ[j].B.transpose())[1])
#----------------------
# show info 
def showInfo():
	print('current N : %d' % j)
	print('%6s %6s %6s %6s %6s %6s'  % ('O_x','O_y','A.x','A.y','B.x','B.y'))
	print('--------------------------------------')
	# print('Org@(%.3f %.3f)' % (Org.x,Org.y))
	print('A@(%.3f %.3f) - %.3f' % (N_A.x[-1],N_A.y[-1],np.sqrt((N_A.x[-1]-Org.x)**2+(N_A.y[-1]-Org.y)**2)))
	print('B@(%.3f %.3f) - %.3f' % (N_B.x[-1],N_B.y[-1],np.sqrt((N_B.x[-1]-Org.x)**2+(N_B.y[-1]-Org.y)**2)))			
# ---

if B_showInfo == 1:
	showInfo()
			
			
			
 
 
	