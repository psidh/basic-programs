def is_prime(num):
    # Check if the number is less than or equal to 1
    if num <= 1:
        return False
    # Check if the number is 2 or 3
    elif num <= 3:
        return True
    # Check if the number is divisible by 2 or 3
    elif num % 2 == 0 or num % 3 == 0:
        return False
    # Check all the numbers up to the square root of the number
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_n_prime_numbers(n):
    prime_numbers = []
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            prime_numbers.append(num)
            count += 1
        num += 1
    return prime_numbers

# Find the first 10 prime numbers
print(find_n_prime_numbers(10))
