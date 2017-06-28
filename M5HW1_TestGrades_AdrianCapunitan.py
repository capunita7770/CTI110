
# Test Grade
# 6/22
# CTI-110 M5HW1 - Test Average and Grade
# Adrian Capunitan
#
    
def calc_average(score1, score2, score3, score4, score5 ):
    average = (score1 + score2 + score3 + score4 + score ) / 5
    return average

def determineGrade(score):
    if ( score < 59):
        return "F"
    elif ( score < 69):
        return "D"
    elif ( score < 79):
        return "C"
    elif ( score < 89):
        return "B"
    elif ( score < 101):
        return "A"

# Ask the user to enter the 5 test score

def enterScore():
    score1 = float(input("Please enter score 1: "))
    score2 = float(input("Please enter score 2: "))
    score3 = float(input("Please enter score 3: "))
    score4 = float(input("Please enter score 4: "))
    score5 = float(input("Please enter score 5: "))

    return score1, score2, score3, score4, score5

def printTableResult( score1, score2, score3, score4, score5 ):
    print ("\nScore\tLetter Grade")
    print ( str(score1) + "\t\t",determineGrade(score1), \
            str(score2) + "\t\t",determineGrade(score2), \
            str(score3) + "\t\t",determineGrade(score3), \
            str(score4) + "\t\t",determineGrade(score4), \
            str(score5) + "\t\t",determineGrade(score5), sep = "\n")

def main():
    score1, score2, score3, score4, score5 = enterScore()
    print()
    printTableResult(score1, score2, score3, score4, score5)

main()
