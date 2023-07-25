

''' Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
'''

class FactorialGenerator:
    def __init__(self, start=1, stop=None, step=1):
        self.start = start
        self.stop = stop if stop is not None else start
        self.step = step

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def generate_factorials(self):
        current = self.start
        while current <= self.stop:
            yield self.factorial(current)
            current += self.step


def get_input():
    args = input("Введите три параметра через пробел (start stop step): ").split()
    start = int(args[0]) if len(args) >= 1 else 1
    stop = int(args[1]) if len(args) >= 2 else None
    step = int(args[2]) if len(args) >= 3 else 1
    return start, stop, step


if __name__ == "__main__":
    start, stop, step = get_input()

    generator = FactorialGenerator(start, stop, step)
    for factorial in generator.generate_factorials():
        print(f"Факториал {start}: {factorial}")
        start += step
