import random
import string

import pytest

from homework6.oop_2 import Homework, HomeworkResult, Student, Teacher


def random_string(n=10) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))


def create_and_check_homework(is_success: bool = True):
    teacher = Teacher(random_string(), random_string())
    student = Student(random_string(), random_string())

    homework = teacher.create_homework(random_string(), 1)

    if is_success:
        homework_result = student.do_homework(homework, random_string())
    else:
        homework_result = student.do_homework(homework, random_string(4))

    teacher.check_homework(homework_result)

    return homework, homework_result, student, teacher


def test_check_success_homework():
    try:
        homework, *_ = create_and_check_homework()
        assert homework in Teacher.homework_done
    finally:
        Teacher.reset_results()


def test_check_failed_homework():
    homework, *_ = create_and_check_homework(is_success=False)
    assert homework not in Teacher.homework_done


def test_reset_result():
    homework, *_ = create_and_check_homework()
    Teacher.reset_results(homework)
    assert Teacher.homework_done[homework] == []


def test_reset_all_results():
    homework, *_ = create_and_check_homework()
    Teacher.reset_results()
    assert homework not in Teacher.homework_done


def test_init_homework_result():
    homework = Homework("", 5)
    student = Student("Roman", "Petrov")
    homework_result = HomeworkResult(homework, "solution", student)

    assert isinstance(homework_result, HomeworkResult)


def test_typeerror_homework_result():
    student = Student("Roman", "Petrov")

    with pytest.raises(TypeError):
        HomeworkResult(5, "solution", student)
