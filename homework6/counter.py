"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(input_cls):
    """Some code"""

    class NewClass(input_cls):
        counter = 0

        def __new__(cls):
            cls.counter += 1
            return super().__new__(cls)

        def get_created_instances(*_):
            return NewClass.counter

        def reset_instances_counter(*_):
            tmp = NewClass.counter
            NewClass.counter = 0
            return tmp

    return NewClass


@instances_counter
class User:
    pass


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
