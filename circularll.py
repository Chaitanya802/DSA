class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def creation(self,n):
        i=0
        while i<n:
            newnode=Node(int(input("Enter Node value ")))
            if i==0:
                self.head=newnode
            if i in range(1,n-1):
                t=self.head
                while t.next:
                    t=t.next
                t.next=newnode
            if i==n-1:
                while t.next:
                    t=t.next
                t.next=newnode
                newnode.next=self.head
            i=i+1
    def show(self):
        x=self.head
        while x:
            print(x.val,end=" ")
            x=x.next
a=linkedlist()
b=int(input("Enter number of nodes "))
a.creation(b)
a.show()
