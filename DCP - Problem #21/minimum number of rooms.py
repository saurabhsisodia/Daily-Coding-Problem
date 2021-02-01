from sys import stdin,stdout

def main():
    a=[(30, 75), (0, 50), (60, 150)]
    
    b=[]
    for u in a:
        b.append([u[0],1])
        b.append([u[1],0])
    b.sort(key=lambda x:x[0])
    
    count=0
    ans=0
    for u,v in b:
        if v==1:
            count+=1
        else:
            count-=1
        ans=max(ans,count)
    print(ans)
main()
