class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}
        
        for i in prerequisites:
            key, val = i
            adjList[key].append(val)

        visit = [False] * numCourses
        rec_stack = [False] * numCourses
        
        def is_cyc_util(adjList,x,visit,rec_stack):
            if not visit[x]:

                visit[x] = True
                rec_stack[x] = True

                for node in adjList[x]:
                    if not visit[node] and is_cyc_util(adjList,node,visit,rec_stack):
                        return True
                    elif rec_stack[node]:
                        return True
            rec_stack[x] = False
            return False
        
        for i in range(numCourses):
            if not visit[i] and is_cyc_util(adjList,i,visit,rec_stack):
                return False
        
        return True





        