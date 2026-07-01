from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(course):
            # in case of a cycle
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            # when dfs for a course is done, add to visited
            # check all prereqs for a course
            visiting.remove(course)
            visited.add(course)
            return True

        graph = defaultdict(list)
        # prereq must be visited before to visit the course
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        visiting = set()
        visited = set()

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            