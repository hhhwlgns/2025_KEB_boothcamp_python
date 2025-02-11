# main
number = input("Input two number : ").split()
n1 = int(number[0])
n2 = int(number[1])

if n1 > n2:
    n1, n2 = n2, n1

if n1 < 2:
    print("올바른 수가 아닙니다.")

else:
    while n1 <= n2:
        i = 2
        k = 0

        while i <= int(n1 ** 0.5):
            if n1 % i == 0:
                k = k + 1
                break
            i = i + 1

        if k == 0:
            print(n1, end=" ")

        n1 = n1 + 1



