from collections import deque

location = ['A','B','C','D']
locationindex = {name: idx for idx, name in enumerate(location)}

adjmatrix = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]

def dfsmatrix(start):
    visited = [False] * len(location)
    result = []
    
    def dfs(node):
        visited[node]= True
        result.append(location[node])
        for neighbor in range(len(adjmatrix)):
            if adjmatrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
                
    dfs(locationindex[start])
    return result



adjlist = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A','D'],
    'D': ['B','C']
}

def bfslist(start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in adjlist[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

def menu():
    print("\n==== menu ====")
    print("1. DFS")
    print("2. BFS")
    print("3. Exit")
    
while True:
    menu()
    choice = input("Enter your choice:")
    
    if choice == '1':
        startlocation = 'A'
        dfsresult = dfsmatrix(startlocation)
        print("DFS transversal(using adjacenylist):",dfsresult)
        
    elif choice == '2':
        startlocation = 'A'
        bfsresult=bfslist(startlocation)
        print("BFS transversal(using adjacency list):", bfsresult)
        
    elif choice == '3':
        break