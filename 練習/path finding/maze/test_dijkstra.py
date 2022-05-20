import numpy as np 
from collections import defaultdict

cost = np.array([[3,2,4,5],[7,1,8,0],[9,-3,2,1]])
def find_adj(size,cur_pos):
    # size = [row,col]
    # cur_pos = [x,y]
    adj_pos  =[] 
    x,y = cur_pos
    if x > size[0] or y > size[1]:
        print('out of bound')
        print('please check the input value')
        return 

    if x -1 >= 0:
        adj_pos.append([x-1,y])
    if y -1 >= 0:
        adj_pos.append([x,y-1])
    if x +1 <size[0]:
        adj_pos.append([x+1,y]) 
    if y +1 <size[1]:
        adj_pos.append([x,y+1])
    return adj_pos


def tran_graph(matrix):
    import numpy as np
    graph = {}
    (row ,col) = matrix.shape
    
    n = row*col
    S = np.array(range(n)).reshape(row,col)
    for i in range(row):
        for j in range(col):
            Pt_n = {}
            adj_pos = find_adj([row,col],[i,j])
            for u,v in adj_pos:
                Pt_n[str(S[u][v])] = matrix[u][v]

            cur = str(S[i][j])
            graph[cur] = Pt_n

    return graph

#print(tran_graph(cost))

#===================================================
'''
def init_graph():
    A = defaultdict(dict)
    A['P1'] = {'P2':7,'P3':3}   
    A['P2'] = {'P1':7,'P4':4} 
    A['P3'] = {'P1':3,'P5':99}  
    A['P4'] = {'P2':4,'P5':8,'P6':1}  
    A['P5'] = {'P3':99,'P4':8,'P6':6}
    A['P6'] = {'P7':5}
    A['P7'] = {'P6':5}
    return A
'''
def init_graph():
    A = defaultdict(dict)
    A['a'] = {'b':1,'c':1}   
    A['b'] = {'a':1,'d':1,'e':1} 
    A['c'] = {'a':1,'f':1}  
    A['d'] = {'b':1}  
    A['e'] = {'b':1}
    A['f'] = {'c':1,'g':1}
    A['g'] = {'f':1}
    return A

def bfs(graph,s):
    if s not in graph.keys():
        print('the input start point is not exist')
        return
    path, visited = [s],[s]
    while path != []:
        cur = path.pop()
        for x in graph[cur].keys():
            if x not in visited:
                visited.append(x)
                path.append(x)
        print(visited)
    return visited

def dfs(graph,s):
    if s not in graph.keys():
        print('the input start point is not exist')
        return
    path,visited = [s],[]
    while path:
        cur = path.pop()
        if cur not in visited:
            visited.append(cur)
            adj_node = graph[cur].keys()
            for i in adj_node:
                path.append(i)
    return visited

A = init_graph()
print(bfs(A,'p'))


def dijkstra(graph,s,goal):
    path, adj_node,que = {},{},[]
    book = []
    for node in graph:
        path[node] = float('inf')
        adj_node[node] = None
        que.append(node)
    path[s] = 0
    while que :
        key_min = que[0]
        min_val = path[key_min]
        for n in range(1,len(que)):
            if path[que[n]] < min_val:
                key_min = que[n]
                min_val = path[key_min]
        cur = key_min 
        que.remove(cur)
        for i in graph[cur]:
            alternate = graph[cur][i] + path[cur]
            if path[i] > alternate:
                path[i] = alternate
                adj_node[i] = cur
        #print(adj_node)

    book = searching_path(graph,path,s,goal)
    return book 
'''
def searching_path(graph,dist,s,g):
    path = [s]
    min_pos,min_dist = 0,float('inf')
 
    #while path[-1] != g:
    for i in range(5):
        cur = path[-1]
        print(graph[cur])
        tmp = [x, min(dist[x]) for x in graph[cur].values() 
        print(min_pos,min_dist)
        if min_pos not in path:
            path.append(min_pos)
         
    return path 
'''
'''
M = tran_graph(cost)
#print(M)
print(dijkstra(M,'0','11'))
'''