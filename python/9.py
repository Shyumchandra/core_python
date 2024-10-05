def fun(a,b=3):
    print(a+b)
a=fun(1,2)
b=fun(b=5,a=1)
c=fun(1)
print(a,b,c)    

print()

def fu(n):
    if n==2:
        print(n," yayyy")
    else:
        print("FUCK OFFFFF")
fu(2)
fu(5)    

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

print()

double=lambda x:x*2
res=double(5)
print(res)    