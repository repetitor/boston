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

import pandas as pd
import seaborn as sns
from google.colab import drive
from sklearn import tree
drive.mount('/content/drive')

base = '/content/drive/MyDrive/Colab Notebooks/stepik/126333-intro-data-analyze/'
df = pd.read_csv(base + 'students.csv', delimiter=',')
df_test = pd.read_csv(base + 'students_test.csv', delimiter=',')
