def f1():
    print("Hi")


def f2(name):
    print('Hi ' + name)


def f3(name):
    return name


def f4():
    return 1, 2


x, x1 = f4()
print(x)
print(x1)
