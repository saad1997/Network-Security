import random
from Crypto.Util import number
import os

n_length = 10
primeNum = number.getPrime(n_length, os.urandom)
q=primeNum
prime = q
num_to_check = 0
p_minus_1_range = range(1,prime)
primitive_roots = []
for each in range(1, prime):
	num_to_check += 1
	candidate_prim_roots = []
	for i in range(1, prime):
		modulus = (num_to_check ** i) % prime
		candidate_prim_roots.append(modulus)
		cleanedup_candidate_prim_roots = set(candidate_prim_roots)
		if len(cleanedup_candidate_prim_roots) == len(range(1,prime)):
			primitive_roots.append(num_to_check)
a=random.choice(primitive_roots)
print('The Prime Number is',q,'\nThe Primitive Root is',a)
xa=random.randint(1,q)
print("secret key for user1=",xa)
ya=(a**xa)%q
print("Public key for user1=",ya)
xb=random.randint(1,q)
print("secret key for user2=",xb)
yb=(a**xb)%q
print("Public key for user2=",yb)
shared_secret_key_User1=(yb**xa)%q
shared_secret_key_User2=(ya**xb)%q
print("Shared Secret Key for User1=",shared_secret_key_User1)
print("Shared Secret Key for User2=",shared_secret_key_User2)
