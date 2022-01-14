def f2():
    yield 5
    yield 6


def f1():
    r = f2()
    yield r
    r = f2()
    yield r

for e in f1():
    for e1 in e:
        print(e1)