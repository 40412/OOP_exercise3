# File: task4.py
# Author: Jasmin Fränti
# Description: Task 4 of exercise 3 
# Class ExamSubmission and method to determine and return a new list
# With only the submissions that passed the test

class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'Exam submission (examinee: {self.examinee}, points: {self.points})'

def passed(submissions: list, lowest_passing: int):
    passing = []
    
    for submission in submissions:
        if submission.points >= lowest_passing:
            passing.append(submission)

    return passing

if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)