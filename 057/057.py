def count_student_sex(students: list) -> list:
    male, female = 0, 0

    for student in students:
        if student.lower() == "male":
            male += 1
        elif student.lower() == "female":
            female += 1

    return [("Male", male), ("Female", female)]


def count_student_sex2(students: list) -> list:
    def filter_students(sex):
        return list(filter(lambda s: s.lower() == sex, students))

    return [("Male", len(filter_students("male"))),
            ("Female", len(filter_students("female")))]


def count_student_sex3(students: list) -> list:
    students_lowercase = list(map(lambda s: s.lower(), students))

    return [("Male", students_lowercase.count("male")),
            ("Female", students_lowercase.count("female"))]


if __name__ == "__main__":
    students = ['Male', 'Female', 'female', 'male', 'male', 'male',
                'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

    print(count_student_sex(students))
    print(count_student_sex2(students))
    print(count_student_sex3(students))
