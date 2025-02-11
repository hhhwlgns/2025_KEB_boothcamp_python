def is_prime(num) -> bool:
    """
    소수 여부를 판정해서 소수면 True 아니면 False를 반환
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        for i in range(2, int(n ** 0.5) + 1):
            if num % i == 0:
               return False
    else:
        return False

    return True

# main
help(is_prime)
n = int(input("Input number : "))

if is_prime(n): #count == 0:
     print("yes")
else:
     print("no")