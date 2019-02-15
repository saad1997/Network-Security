import random
import sys

qi=sys.argv[1]
q=int(qi)
ai=sys.argv[2]
a=int(ai)
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
