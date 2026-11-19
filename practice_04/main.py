x = 32 #снаружи функции - внешняя переменная
def show():
    x = 22 #ВНУТРИ ФУНКЦИИ - локальная переменная
    print(x)
show()
print(x)
#вывод:
# 22
# 32

def total(*args):
    sum((args))
    return sum((args))
print(total(22, 23, 24))


def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age
print(person(name='Соня',age = 18))


def increase(x):
    return x + 2
def apply(func, value):
    func(value)
    return func(value)
print(apply(increase, 3))


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(3)

