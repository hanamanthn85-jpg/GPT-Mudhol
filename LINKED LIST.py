class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.first=None
    def insert(self,data):
        newnode=Node(data)
        if self.first==None:
            self.first=newnode
        else:
            cur=self.first
            while (cur.next):
                cur=cur.next
            cur.next=newnode
    def __iter__(self):
        cur=self.first
        while cur:
            yield cur.data
            cur=cur.next
l1=Linkedlist()
l1.insert (2009)
l1.insert("Welcome")
l1.insert("TO")
l1.insert("GPTA")
print("The content of Linked List is:")
for x in l1:
    print(x, end=" ")
            
