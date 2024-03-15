 # Static Linked list creation using structured programming
class Node: # defining proerty of node data structure
    def __init__(self, data): 
        self.data = data  
        self.next = None
n1=Node("3")
n2=Node("7")
n3=Node("10")
n1.next=n2
n2.next=n3
curr=n1
while True:
    if curr.next!=None:
        print(curr.data+" ")
    else:
        print(curr.data)
        break
    curr=curr.next
# Node is a concept analogus to pointers in C