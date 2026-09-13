class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_graph = [[] for i in range(numCourses)]

        remaining_prerequisites = [0] * numCourses

        for i, j in prerequisites:
            course_graph[j].append(i)
            remaining_prerequisites[i] += 1

        ready_courses = deque()

        for i in range(numCourses):
            if remaining_prerequisites[i] == 0:
                ready_courses.append(i)
        
        completed_courses = 0

        while ready_courses:
            current_course = ready_courses.popleft()
            completed_courses += 1
            for n in course_graph[current_course]:
                remaining_prerequisites[n] -= 1
                if remaining_prerequisites[n] == 0:
                    ready_courses.append(n)
        return completed_courses == numCourses


        