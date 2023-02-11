# https://tproger.ru/translations/demystifying-decorators-in-python/
def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper


def f1():
    print('f1')


# decorator_function(f1)()


def f2():
    return 123


# print(f2())

@decorator_function
def f3():
    print('f3')


# f3()
# print(type(f3))

def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper


@benchmark
def fetch_webpage():
    import requests
    requests.get('https://google.com')


fetch_webpage()


def benchmark2(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper


@benchmark2
def fetch_webpage2(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


# webpage2 = fetch_webpage2('https://google.com')
# print(webpage2)
fetch_webpage2('https://google.com')


def benchmark3(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value

        return wrapper
    return actual_decorator


@benchmark3(iters=10)
def fetch_webpage3(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


# webpage3 = fetch_webpage3('https://google.com')
# print(webpage3)
fetch_webpage3('https://google.com')
