import random 
list_a = [[],[]]
matrix= []

for i in range(2): 
	list_a[i] = random.sample(range(0,9),8)

for i in range(len(list_a[0])):
	val = [list_a[0][i]+s for s in list_a[1]]
	matrix.append(val)
#print(len(matrix))
#print(['%s \r\n' % matrix[i][:] for i in range(5)]) 

def path_find(G,start_v): # G is a matrix, start_v = (row ,col) : list
	current_node = start_v 
	visited_que = G[start_v[0]][start_v[1]]
	n = len(G)
	unvisited_node = [[None]*n]*n
	
	
	
	return distance 

print(path_find(matrix,))
