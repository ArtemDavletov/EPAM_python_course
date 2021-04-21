from homework5.oop_1 import Homework, Student, Teacher


def test_teacher_creation():
    teacher = Teacher("Daniil", "Shadrin")
    assert getattr(teacher, "last_name") == "Daniil"
    assert getattr(teacher, "first_name") == "Shadrin"


def test_homework_creation():
    homework = Homework("Do something", 0)
    assert getattr(homework, "text") == "Do something"
    assert getattr(homework, "deadline") == 0
    assert getattr(homework, "created") is not None


def test_student_creation():
    student = Student("Daniil", "Shadrin")
    assert getattr(student, "last_name") == "Daniil"
    assert getattr(student, "first_name") == "Shadrin"


def test_create_homework_by_teacher():
    student = Student("Daniil", "Shadrin")
    oop_homework = Teacher.create_homework("create 2 simple classes", 5)

    assert str(oop_homework.deadline) == "5 days, 0:00:00"
    assert isinstance(student.do_homework(oop_homework), Homework)


def test_create_expired_homework_by_teacher():
    student = Student("Daniil", "Shadrin")

    expired_homework = Teacher.create_homework("Learn functions", 0)

    assert str(expired_homework.deadline) == "0:00:00"

    assert student.do_homework(expired_homework) == "You are late"
