# Day 27

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        def addNode(source, dest, weight):
            if source in graph:
                graph[source].append((dest, weight))
            else:
                graph[source] = [(dest, weight)]
        
        for i, pair in enumerate(equations):
            addNode(pair[0], pair[1], values[i])
            addNode(pair[1], pair[0], 1/values[i])
        
        def graphSearch(pair):
            s = pair[0]
            d = pair[1]
            
            if s not in graph or d not in graph:
                return -1
                
            visited = set()
            queue = [(s, 1)]
            
            while queue:
                front, curTotal = queue.pop(0)
                if front == d:
                    return curTotal
                visited.add(front)
                for child, value in graph[front]:
                    if child not in visited:
                        queue.append((child, curTotal*value))
            
            return -1
            
        return [graphSearch(pair) for pair in queries]
            
            
            
            
