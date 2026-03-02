class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            if len(self.scores) < 2:
                raise ValueError
            highest = max(self.scores[-2:])
            print("Highest score among last two is:", highest)
        except:
            print("Not enough scores to find highest value")


scores = list(map(int, input("Enter scores separated by space: ").split()))
student = StudentScores(scores)
student.highest_last_two()