from random import randint


def fun():
    ans=None
    
    for i,e in enumerate(list(map(int,input().split( )))):
        if i==0:
            ans=e
        elif randint(1,i+1)==1:
            ans=e
    return ans


print(fun())
