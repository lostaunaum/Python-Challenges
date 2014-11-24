################## Student Grade Calculator ##################

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students =[lloyd, alice, tyler]

def average_grade(numbers):
    total = sum(numbers)
    total = float(total) / len(numbers)
    return total 

def get_total_average_score(student):
    total = 0
    homework = average_grade(student["homework"])
    quizzes = average_grade(student["quizzes"])
    tests = average_grade(student["tests"])
    
    total += float(homework) * 0.10
    total += float(quizzes) * 0.30
    total += float(tests) * 0.60
    return total
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
    

#Average of one student
score = get_total_average_score(lloyd)
print score
print get_letter_grade(score)

#Class Average
class_average = get_class_average(students)
print class_average
print get_letter_grade(class_average)



################## Student Grade Calculator ##################