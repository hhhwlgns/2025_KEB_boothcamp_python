#countdown
for i in range (10,0,-1):
    print(i)
print('Boom!')

def countdown(n):
    if n == 0:
        print('Boom!')
    else:
        print(n)
        return countdown(n-1)

countdown(10)

#factorial
def factorial1(n) -> int:
    result = 1
    for i in range (1, n+1):
        result = result * i
    print(result)

factorial1(5)

def fectorial2(n) -> int:
    if n == 0:
        return 1
    return n * fectorial2(n-1)

print(fectorial2(5))

#fibonacci
def fibonacci1(n) -> int:
    f_list = [0,1]
    if n >= 0:
        for i in range (2, n+1):
            f_list.append(f_list[i-1]+f_list[i-2])
        return f_list[n]

print(fibonacci1(10))

def fibonacci2(n) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci2(n-2) + fibonacci2(n-1)

print(fibonacci2(10))




