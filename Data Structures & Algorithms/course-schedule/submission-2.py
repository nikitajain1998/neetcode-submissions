class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # course -> courses that depend on it
        course_graph = [[] for _ in range(numCourses)]

        # number of prerequisites still remaining for each course
        remaining_prerequisites = [0] * numCourses

        # Build the graph and count prerequisites
        for course, prerequisite in prerequisites:
            course_graph[prerequisite].append(course)
            remaining_prerequisites[course] += 1

        # Courses that are ready to be taken
        ready_courses = deque()

        for course in range(numCourses):
            if remaining_prerequisites[course] == 0:
                ready_courses.append(course)

        completed_courses = 0

        # Process courses in dependency order
        while ready_courses:

            current_course = ready_courses.popleft()
            completed_courses += 1

            # This course is completed,
            # so remove it as a prerequisite from dependent courses
            for next_course in course_graph[current_course]:

                remaining_prerequisites[next_course] -= 1

                # All prerequisites are now completed
                if remaining_prerequisites[next_course] == 0:
                    ready_courses.append(next_course)

        # We can finish only if every course was completed
        return completed_courses == numCourses

        