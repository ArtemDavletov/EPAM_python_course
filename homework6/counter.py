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
    input_cls.counter = 0
    new = input_cls.__new__

    def __new__(cls):
        cls.counter += 1
        return new(cls)

    def get_created_instances(*_):
        return input_cls.counter

    def reset_instances_counter(*_):
        tmp = input_cls.counter
        input_cls.counter = 0
        return tmp

    input_cls.__new__ = __new__
    input_cls.get_created_instances = get_created_instances
    input_cls.reset_instances_counter = reset_instances_counter

    return input_cls


@instances_counter
class User:
    pass


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
