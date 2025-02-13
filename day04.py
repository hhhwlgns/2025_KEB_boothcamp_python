# 2중 데코레이션 적용, 성능측정 데코, 디스크립션 데코를 팩토리얼 함수에 적용

import time

def description(outhamsu):
    def inner (*inhamsu):
        print(outhamsu.__name__)
        print(outhamsu.__doc__)
        r = outhamsu(*inhamsu)

        return r

    return inner


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper


@time_decorator
@description
def factorial_repetition(n) -> int:
    """
     factorial_repetition 설명
    :param n:
    :return:
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


number = int(input())
print(f"{number}! = {factorial_repetition(number)}")