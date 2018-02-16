#Diffie-Hellman key Exchange Algorithm

from random import randint
import math
#check is prime or not using fermats primality test
def is_prime(num, count):
    if num == 1:
        return False
    if count >= num:
        count = num - 1
    for x in range(count):
    		#selecting a random number between a and number-1
        a = randint(1, num - 1)
        #checking if a^num-1(mod num)==0 then probabily prime
        if pow(a, num-1, num) != 1:  
            return False
    return True
#Generate very_big prime approximately 310 digit 
def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p
            
prime1=generate_big_prime(2**10)
print("prime 1: ")
print(prime1)

prime2=generate_big_prime(2**10)
print("prime 2: ")
print(prime2)


alice_private_key=randint(2**10, 2**15)
bob_private_key=randint(2**10, 2**15)

a=pow(prime2,alice_private_key,prime1)
b=pow(prime2,bob_private_key,prime1)

alice_key=pow(b,alice_private_key,prime1)
bob_key=pow(a,bob_private_key,prime1)

print("Alice Secret key :")
print(alice_key)

print("Bob Secret key :")
print(bob_key)

