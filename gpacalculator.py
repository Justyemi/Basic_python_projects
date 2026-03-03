def grade_to_points(grade):
    grade = grade.upper()
    scale = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D': 1.0,
        'F': 0.0
    }
    return scale.get(grade, 0.0)

def gpa_courses(courses):
    total_points = 0
    total_credits = 0
    for course in courses:
        credits = course['credits']
        grade = course['grade']
        points = grade_to_points(grade) * credits
        total_points += points
        total_credits += credits
    return total_points / total_credits if total_credits != 0 else 0

# Example usage
courses = [
    {'credits': 3, 'grade': 'A'},
    {'credits': 4, 'grade': 'B+'},
    {'credits': 2, 'grade': 'C'}
]

gpa = gpa_courses(courses)
print(f"Semester GPA: {gpa:.2f}")