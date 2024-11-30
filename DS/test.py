class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
        print("It's me ll")
    def travesal(self):
        l1=[]
        if s1.head is None:
            print("Hey i am empty")
        a=s1.head
        while a is not None:
            l1.append(a.data)
            print(a.data,end="-->")
            a=a.next
        return l1[::-1]
    def add_node_at_first(self, data):
        print()
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def add_at_end(self,data):
        print()
        ne=node(data)
        a=self.head   # a=nb,n1,n2,n3
        while a.next is not None:
            a=a.next
        a.next=ne
    def insert_at_specified_position(self,position,data):
        print()
        ns=node(data)
        a=self.head
        for i in range(position-1):
            a=a.next
        ns.next=a.next
        a.next=ns
    def delete_first_node(self):
        print()
        self.head=self.head.next
    def delete_last_node(self):
        print()
        a=self.head
        while a.next.next is not None: #n1,n2,n3,
            a=a.next
        a.next=None
    def delete_specific_node(self, position):
        print()
        a=self.head
        for _ in range(position-1):
            a=a.next
        a.next=a.next.next
    # def reverse_ll(self,ll_len):
    #     a=self.head
    #     for i in range(1,ll_len-1):
    #         for _ in range(ll_len-i):
    #             a=a.next
    def create_ll(self,data):
        n99=node(data)
        if self.head is None:
            self.head=n99
            return
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=n99
    def list_accept(self,l1):
        for i in l1:
            s2.create_ll(i)
    def travesal_2(self):
        l1=[]
        if s2.head is None:
            print("Hey i am empty")
        a=s2.head
        while a is not None:
            l1.append(a.data)
            print(a.data,end="-->")
            a=a.next
                
                
s1=ll()
n1=node(10)
s1.head=n1
n2=node(20)
n3=node(30)
n1.next=n2
n2.next=n3
s1.travesal()
s1.add_node_at_first(2)
s1.travesal()
s1.add_at_end(25)
s1.travesal()
s1.insert_at_specified_position(3,111)
s1.travesal()
s1.delete_first_node()
s1.travesal()
s1.delete_last_node()
s1.travesal()
s1.delete_specific_node(2)
s1.travesal()
s1.add_at_end(1010)
list1=s1.travesal()
print()
print(list1)
s2=ll()
s2.list_accept(list1)
s2.travesal_2()

