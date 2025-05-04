def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # Initial Solution
        ute = len(students)
        while sandwiches and ute:
            temp = ute
            for i in range(len(students)):
                if not sandwiches or not ute:
                    break
                if students[i] == sandwiches[0]:
                    del sandwiches[0]
                    students[i] = 2
                    ute = ute - 1
            if temp == ute:
                break
        return ute