import tkinter as tk
import numpy as np

class main():
	def __init__(self,master):
		self.master = master
		self.frame = tk.Frame(self.master,width=300,height=300)
		self.create_board()
		Row	= self.create_rand(self.n)
		Col = self.create_rand(self.n)
		self.fill_num(Row,Col)
		self.mark_sol()

	def create_board(self):
		self.canvas = tk.Canvas(self.master,bg='white',height=500,width=500)
		self.canvas.pack()
		Pt_S, Pt_E,step = 50, 450 , 50
		self.n = (Pt_E - Pt_S)/step
		self.x , self.y = [],[]
		for k in range(2):
			for i in range(Pt_S,Pt_E+step,step):
				self.x.append(i+step/2)
				self.y.append(i+step/2)
				coord1 = [[Pt_S,i,Pt_E,i],[i,Pt_S,i,Pt_E]] 
				self.canvas.create_line(coord1[k],fill='red')
			
	def create_rand(self,k):
		return np.random.permutation(np.arange(1,k+1))
		

	def fill_num(self,list_a,list_b):
		#  matrix generation
		la , lb = len(list_a),len(list_b)
		M = np.zeros((la,lb))
		for i in range(la):
			for j in range(lb):
				M[i][j] = list_a[j] + list_b[i]
		
		self.Maze = M
		# plot the matrix 
		for i in range(la):
			for j in range(lb):
				self.canvas.create_text(self.x[i],self.y[j],text='%s' % M[i][j])
	def mark_sol(self):
		
		self.canvas.create_rectangle(50,50,100,100,outline='blue',width=2)
		
'''
	def dijkstra(self,dist_matrix,s):
		row ,col = dist_matrix.shape
		n = row*col
		path, adj_node,que = {},[[],[]],[]
		book = [] 
		for i in range(1,row):
			for j in range()
			que.append(())
'''	
		
			
	
if __name__ == "__main__":
	root = tk.Tk()
	app = main(root)
	root.mainloop()
