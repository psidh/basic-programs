

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
