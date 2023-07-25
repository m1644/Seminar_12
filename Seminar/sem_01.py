

''' Задание №1
Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
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


k_value = 5
calculator = FactorialCalculator(k_value)

print(calculator.factorial(3))
print(calculator.factorial(5))

print(calculator.get_history())
