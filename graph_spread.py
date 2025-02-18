graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
to_visit = []
visited = []
start = '0'
i = 0
while len(graph) > len(visited):
    if start not in visited:
        visited.append(start)
        temp_visit = list(graph[start])
        to_visit.extend(graph[start])
    else:
        start = to_visit[i]
        i += 1
print(visited)