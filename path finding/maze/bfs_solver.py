graph = {'A':['B'],'B':['C','D'],'C':['E','F','H'],'D':['B','S'],'E':['C'],
				'F':['C','G'],'G':['F','H'],'H':['C','G'],'S':['D']}

def main():
	print(dfs(graph,'A',[]))
 
def dfs(G,start_v,visited):
	if start_v not in visited:
		visited.append(start_v)
		node = start_v 
		for n in graph[node]:
			dfs(G,n,visited)
	return visited
 
def dfs(G,start,visited):
	que = [start]
	while que:
		node = que.pop()
		for n in graph[node]:	
			if n not in visited:
				que.append(n)
		visited.append(node)
	return visited
	
def bfs(G,start_v):
	visited = []
	queue = [start_v]
	
	while queue:
		node = queue.pop(0)
		if node not in visited:
			visited.append(node)
			neighbors = graph[node]
		
			for neighbor in neighbors:
				queue.append(neighbor)

	return visited





if __name__ == '__main__':
	main()
