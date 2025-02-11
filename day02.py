n = int(input("Input number : "))
is_prime = True

if n >= 2:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False #count = count + 1
            break

if is_prime: #count == 0:
     print("yes")
else:
     print("no")