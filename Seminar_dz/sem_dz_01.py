import csv


''' Задание_1
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. 
Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета 
и по оценкам всех предметов вместе взятых.
'''

class NameValidator:
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        words = value.split()
        for word in words:
            if not word.isalpha() or not word.istitle():
                raise ValueError("ФИО должно содержать только буквы и начинаться с заглавной буквы.")
        setattr(instance, self.private_name, value)

class SubjectValidator:
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        subjects = instance.load_subjects()
        if value not in subjects:
            raise ValueError(f"Предмет {value} не найден в списке доступных предметов.")
        setattr(instance, self.private_name, value)

class Student:
    name = NameValidator()
    subject = SubjectValidator()

    def __init__(self, name):
        self.name = name
        self.subjects = self.load_subjects()
        self.scores = {subj: [] for subj in self.subjects}
        self.test_results = {subj: [] for subj in self.subjects}

    def load_subjects(self):
        subjects = []
        with open("Seminar_dz/subjects.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                subjects.append(row[0])
        return subjects

    def add_score(self, subject, score):
        if score not in range(2, 6):
            raise ValueError("Оценка должна быть от 2 до 5.")
        self.scores[subject].append(score)

    def add_test_result(self, subject, result):
        if result not in range(0, 101):
            raise ValueError("Результат теста должен быть от 0 до 100.")
        self.test_results[subject].append(result)

    def average_test_score(self, subject):
        return sum(self.test_results[subject]) / len(self.test_results[subject])

    def average_score_all_subjects(self):
        all_scores = [score for subject_scores in self.scores.values() for score in subject_scores]
        return sum(all_scores) / len(all_scores)


if __name__ == "__main__":

    student = Student("Ivan Ivanov")

    student.add_score('Math', 4)
    student.add_score('English', 5)
    student.add_score('History', 5)
    student.add_score('Physics', 3)
    student.add_score('Chemistry', 3)

    student.add_test_result('Math', 85)
    student.add_test_result('Math', 92)
    student.add_test_result('English', 78)
    student.add_test_result('English', 68)
    student.add_test_result('History', 74)
    student.add_test_result('History', 88)
    student.add_test_result('Physics', 44)
    student.add_test_result('Physics', 54)
    student.add_test_result('Chemistry', 64)
    student.add_test_result('Chemistry', 74)
    
    
    print(f'Имя студента: {student.name}')
    print(f'Предметы студента: {student.subjects}')
    print(f'Средний бал по тестам (Математика): {student.average_test_score("Math")}')
    print(f'Средний бал по тестам (Английский): {student.average_test_score("English")}')
    print(f'Средний бал по тестам (История): {student.average_test_score("History")}')
    print(f'Средний бал по тестам (Психология): {student.average_test_score("Physics")}')
    print(f'Средний бал по тестам (Химия): {student.average_test_score("Chemistry")}')
    print(f'Средний бал по всем оценкам, всех предметов: {student.average_score_all_subjects()}')
