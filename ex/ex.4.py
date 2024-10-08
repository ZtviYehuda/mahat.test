class Student:
    def __init__(self, student_id, arr_grades_a, arr_grades_b):
        self.student_id = student_id
        self.arr_grades_a = arr_grades_a
        self.arr_grades_b = arr_grades_b

    def is_improving(self):
        improving = True
        for grade_a, grade_b in (self.arr_grades_a, self.arr_grades_b):
            if grade_a != -1 and grade_b != -1:
                if grade_b < grade_a:
                    improving = False
                    break
        return improving
