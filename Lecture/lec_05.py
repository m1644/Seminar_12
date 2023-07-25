from django.db import models


#### Дескрипторы

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)


class Student:
    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'


std1 = Student('Шурик', 7, 1, 12)
print(std1)
print('------------------------')


####

class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше 18 или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')

class Student:
    age = Range(3, 103)
    grade = Range(1, 11 + 1)
    office = Range(3, 42 + 1)

    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'


if __name__ == '__main__':
    std_one = Student('Архимед', 12, 4, 29)
    # std_other = Student('Аристотель', 2406, 5, 17)    # ValueError: Значение 2406 должно быть меньше 103
    print(f'{std_one = }')
    std_one.age = 15
    print(f'{std_one = }')
    # std_one.grade = 11.0    # TypeError: Значение 11.0 должно быть целым числом
    # std_one.office = 73    # ValueError: Значение 73 должно быть меньше 42
    # del std_one.age    # AttributeError: Свойство "_age" нельзя удалять
    print(f'{std_one.__dict__ = }')
print('------------------------')


#### Задание_5

class Text:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.param(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Bad {value}')

class User:
    first_name = Text(str.istitle)
    last_name = Text(str.isupper)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Student(age={self.first_name}, grade={self.last_name})'


if __name__ == '__main__':
    std_one = User('Гвидо ван', 'Россум')
