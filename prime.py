

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

#METHOD 2

n1 = int(input ())  
n2 = int(input ())  
  
print ("The Prime Numbers in the range are: ")  
def prime(n1, n2):

    for i in range (n1, n2 + 1):  
        if i > 1:  
            for j in range (2, i):  
                if (i % j) == 0:  
                    break
            else:  
                print (i)  
prime(n1, n2)
