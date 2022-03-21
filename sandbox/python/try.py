# print('hello-python')


def first(msg):
    print(msg)


first("Hello1")

second = first
second("Hello2-second")


# decorator
# https://www.programiz.com/python-programming/decorator
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


ordinary = make_pretty(ordinary)
ordinary()


# equivalent to:
@make_pretty
def ordinary():
    print("I am ordinary 2")


ordinary()
