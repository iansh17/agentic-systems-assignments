class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            avg = sum(self.marks[-3:]) / 3
            if len(self.marks) < 3:
                raise ValueError
            print("Average of last 3 marks is:", avg)
        except:
            print("Not enough marks to calculate average")


marks = list(map(int, input("Enter marks separated by space: ").split()))
student = StudentMarks(marks)
student.last_three_avg()