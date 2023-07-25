

#### Создаём итераторы

class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1


fib = Fibonacci(20, 100)

# for num in fib:    # TypeError: 'Fibonacci' object is not iterable
#     print(num)
print('------------------------')


#### Возврат итератора, __iter__

class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.first < self.stop:
            self.first, self.second = self.second, self.first + self.second
            if self.start <= self.first < self.stop:
                return self.first
        raise StopIteration


fib = Fibonacci(20, 100)

for num in fib:    # TypeError: 'Fibonacci' object is not iterable
    print(num)
print('------------------------')


#### Задание_2

class Iter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start, self.stop):
            return chr(i)
        raise StopIteration


chars = Iter(65, 91)
for c in chars:
    print(c)
