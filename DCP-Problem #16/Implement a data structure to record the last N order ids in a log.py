class LogDataStructure(object):
    def __init__(self,n):
        self.max_size=n
        self.circular_buffer=[0]*n
        self.current=0
    
    def RecordId(self,order_id):
        self.circular_buffer[self.current]=order_id
        self.current=(self.current+1)%self.max_size
    
    def get_last(self,i):
        return self.circular_buffer[(self.current-i+self.max_size)%self.max_size]

'''
n=int(input("enter max size::"))
log=LogDataStructure(n)
for i in range(1,9):
    log.RecordId(i)

print(log.get_last(2))
'''
