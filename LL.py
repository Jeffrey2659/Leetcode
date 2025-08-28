class Node:
    #constructor
    def __init__(self,data):
        self.data = data
        # next is just a python attribute, holding a reference to another object
        # that is why i dont need to declare it as a parameter
        self.next = None
    
def traverseLL(head):

    currNode = head

    while currNode:
        print(currNode.data)
        currNode = currNode.next
    #need to constanly update the head

def rv

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


traverseLL(node1)