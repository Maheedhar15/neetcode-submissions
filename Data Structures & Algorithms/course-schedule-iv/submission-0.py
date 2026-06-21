class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict 
        adj_list = defaultdict(list) 
        for dependency,node in prerequisites: 
            adj_list[node].append(dependency)

        def dfs(node,visited, dependency): 
            if node == dependency: 
                return True 
                
            flag = False 
            for neighbour in adj_list[node]: 
                if neighbour not in visited: 
                    visited.add(neighbour) 
                    flag = flag or dfs(neighbour, visited, dependency) 
            return flag
        res = []
        for dependency, node in queries:
            res.append(dfs(node,set([node]), dependency))
        
        return res
        