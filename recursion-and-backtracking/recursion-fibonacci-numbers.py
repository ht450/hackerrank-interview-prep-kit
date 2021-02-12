def fibonacci(n):

    if n==0:
        return 0
    elif n==1:
        return 1

    num = fibonacci(n-1) + fibonacci(n-2)
    return num

n = int(input())
print(fibonacci(n))
