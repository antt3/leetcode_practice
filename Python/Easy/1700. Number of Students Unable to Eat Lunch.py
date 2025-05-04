def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # Optimized Solution
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                break
        
        return res 
        
        # Initial Solution
        # ute = len(students)
        # while sandwiches and ute:
        #     temp = ute
        #     for i in range(len(students)):
        #         if not sandwiches or not ute:
        #             break
        #         if students[i] == sandwiches[0]:
        #             del sandwiches[0]
        #             students[i] = 2
        #             ute = ute - 1
        #     if temp == ute:
        #         break
        # return ute