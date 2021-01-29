import random
def estimatepi():
    interval=100000
    inside_circle=0;total=0
    
    for i in range(interval):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        
        if x**2+y**2 <=1:
            inside_circle+=1
        total+=1
    
    pi=4*(inside_circle/total)
    print(pi)

estimatepi()
