import json


''' Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
'''

class FactorialCalculator:
    def __init__(self, k):
        self.k = k
        self.history = {}

    def factorial(self, n):
        if n in self.history:
            return self.history[n]
        if n == 0 or n == 1:
            result = 1
        else:
            result = n * self.factorial(n - 1)
        self.history[n] = result
        if len(self.history) > self.k:
            self.history.pop(list(self.history.keys())[0])
        return result

    def get_history(self):
        return self.history

class FactorialContextManager:
    def __init__(self, k, filename):
        self.calculator = FactorialCalculator(k)
        self.filename = filename

    def __enter__(self):
        return self.calculator

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, 'w') as file:
            json.dump(self.calculator.get_history(), file)


k_value = 5
filename = 'Seminar/factorial_history.json'

with FactorialContextManager(k_value, filename) as calculator:
    print(calculator.factorial(3))
    print(calculator.factorial(5))
