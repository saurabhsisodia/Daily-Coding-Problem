class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None


def addNode(head,value):
    p=head
    if not head:
        head=Node(value)
    else:
        while p.next:
            p=p.next
        p.next=Node(value)
    return head

def intersectingNode(head1,head2):
    p1=head1;p2=head2
    l1=0;l2=0
    while p1:
        l1+=1
        p1=p1.next
    while p2:
        l2+=1
        p2=p2.next
    skip=abs(l1-l2)
    if l1>=l2:
        start1=head1
        while skip:
            start1=start1.next
            skip-=1
        start2=head2
    else:
        start2=head2
        while skip:
            start2=start2.next
            skip-=1
        start1=head1
    while start1 and start2:
        if start1 is start2:
            return start1.val
        start1=start1.next
        start2=start2.next
def joinNode(pointer,n):
    p=pointer
    if not p:
        pointer=n
    else:
        while p.next:
            p=p.next
        p.next=n
    return pointer
def main():
    'list 1'
    start1=addNode(None,3)
    start1=addNode(start1,7)
    start1=addNode(start1,8)
    start1=addNode(start1,10)
    
    'make intersection'
    nodeValue=8
    pointer=None
    p=start1
    while p:
        if p.val==nodeValue:
            pointer=p
            break
        p=p.next
        
    'list 2'
    start2=addNode(None,99)
    start2=addNode(start2,1)
    start2=joinNode(start2,pointer)
    print(intersectingNode(start1,start2))
main()
