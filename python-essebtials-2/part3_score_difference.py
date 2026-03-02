class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            difference = self.scores[-1] - self.scores[0]
            print("Difference between last and first score is:", difference)
        except:
            print("No scores available to calculate difference")


scores = list(map(int, input("Enter scores separated by space: ").split()))
student = StudentPerformance(scores)
student.score_difference()