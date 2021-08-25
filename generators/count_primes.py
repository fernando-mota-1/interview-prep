import math

def is_prime(num):
    res = True
    for n in range(3,math.floor(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return res

def count_primes(num):
    count = 0
    if num < 2:
        return 0
    elif num < 3:
        return 1
    count = 1
    for n in range(3, num + 1, 2):
        if is_prime(n):
            count += 1
    return count
    

if __name__ == '__main__':
    num = int(input("upper value:"))
    print(f'prime numbers between 0 and {num} are: ', end='')
    count = count_primes(num)
    print(count)    