def scores_grades():
    from random import randint
    print "Scores and Grades:"
    for i in range(10):
        score = randint(50, 100)
        if score >= 90 and score <= 100:
            grade_letter = "A"
        elif score >= 80 and score < 90:
            grade_letter = "B"
        elif score >= 70 and score < 80:
            grade_letter = "C"
        elif score >= 60 and score < 70:
            grade_letter = "D"
        else:
            grade_letter = "F"
        print " Score: {}; Your grade is: {} ".format(score, grade_letter)
scores_grades()