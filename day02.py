def my_pow(one, two) -> float:
    k = 0
    res = 1
    while k < two:
        res = res * one
        k = k + 1
    return res


def is_prime(num) -> bool:
    if num >= 2:
        i = 2
        while i*i < (num)+1:
        #for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

# main
#help(abs)
#help(is_prime)
num = input("Input number : ").split()
n1 = int(num[0])
n2 = int(num[1])

if n1 > n2:
    n1, n2 = n2, n1

while n1 <= n2:
    if is_prime(n1):
        print(n1, end = " ")
    n1 = n1 + 1
