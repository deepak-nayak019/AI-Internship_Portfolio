#list comprehension
def get_grades(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
scores = [95, 82, 76, 68, 59, 45, 88, 92]
grades = [get_grades(score) for score in scores]
print(grades)
print(scores)
