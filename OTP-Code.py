import random

def otp(l):
    d=""
    for i in range(l):
        a=random.randint(0,9)
        d=d+str(a)
    return int(d)

ll=int(input("Enter the length of OTP ypu want = "))
o=otp(ll)
print(o)