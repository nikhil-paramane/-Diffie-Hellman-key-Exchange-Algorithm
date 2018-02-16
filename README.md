# -Diffie-Hellman-key-Exchange-Algorithm
Diffie-Hellman key Exchange Algorithm implented in python

It uses Fermats Primality Testing method to check whether given number is probabaly prime or not.

Alice and Bob agrees on two big random prime number say prime1 and prime2.

Alice chooses random number as a private key say x, bob chooses y;

alice and bob sends A=(prime1^x)modprime2 and B=(prime1^y)modprime2 to each other respectively.

now alice computes secret key k1=B^x mod prime1 and Bob computes secret key k2=A^x mod prime1.

and k1=k2;
