import datetime
from collections import defaultdict
from typing import Dict, List, Optional

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///main.db")


class Homework(Base):
    __tablename__ = "homework"

    id = Column(Integer, unique=True, primary_key=True, index=True)
    text = Column(String)
    deadline = Column(DateTime, default=datetime.datetime)
    created = Column(DateTime, default=datetime.datetime)

    def __init__(self, text, deadline):
        self.created = datetime.datetime.now()
        self.deadline = datetime.datetime.now() + deadline
        super(Homework, self).__init__(text=text)

    def is_active(self) -> bool:
        return self.deadline > datetime.datetime.now()


class DeadlineError(Exception):
    ...


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, unique=True, primary_key=True, index=True)
    last_name = Column(String)
    first_name = Column(String)

    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError("You are late")


class HomeworkResult(Base):
    __tablename__ = "homework_result"

    id = Column(Integer, unique=True, primary_key=True, index=True)
    homework_id = Column(Integer, ForeignKey("homework.id"))
    homework = relationship("Homework")

    solution = Column(String)
    author_id = Column(Integer, ForeignKey("student.id"))
    author = relationship("Student")

    created = Column(DateTime)

    def __init__(self, homework: Homework, solution: str, author: Student):
        self.created = datetime.datetime.now()
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        super(HomeworkResult, self).__init__(homework=homework, solution=solution, author=author)


class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, unique=True, primary_key=True, index=True)
    last_name = Column(String)
    first_name = Column(String)
    homework_done: Dict[Homework, List[HomeworkResult]] = defaultdict(list)

    @staticmethod
    def create_homework(text: str, days: int) -> Homework:
        return Homework(text=text, deadline=datetime.timedelta(days=days))

    def check_homework(self, homework: HomeworkResult):
        if len(homework.solution) > 5:
            self.homework_done[homework.homework].append(homework)
            return True
        return False

    @staticmethod
    def reset_results(homework: Optional[Homework] = None):
        if homework is None:
            Teacher.homework_done.clear()
        else:
            Teacher.homework_done[homework] = []


if __name__ == "__main__":
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)

    opp_teacher = Teacher(first_name="Daniil", last_name="Shadrin")
    db.add(opp_teacher)
    advanced_python_teacher = Teacher(first_name="Aleksandr", last_name="Smetanin")
    db.add(advanced_python_teacher)

    lazy_student = Student(first_name="Roman", last_name="Petrov")
    db.add(lazy_student)
    good_student = Student(first_name="Lev", last_name="Sokolov")
    db.add(good_student)

    oop_hw = opp_teacher.create_homework(text="Learn OOP", days=1)
    db.add(oop_hw)
    docs_hw = opp_teacher.create_homework(text="Read docs", days=5)
    db.add(docs_hw)

    result_1 = good_student.do_homework(homework=oop_hw, solution="I have done this hw")
    db.add(result_1)
    result_2 = good_student.do_homework(homework=docs_hw, solution="I have done this hw too")
    db.add(result_2)
    result_3 = lazy_student.do_homework(homework=docs_hw, solution="done")
    db.add(result_3)
    try:
        result_4 = HomeworkResult(homework=good_student, solution="fff", author="Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
    db.commit()
