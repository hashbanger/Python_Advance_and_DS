# Reversing a Linked List


# Implementing a node
class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


# Reversing the list
def ReverseList(head):
    
    current = head
    previous = None
    nextnode = None    

    while current:

        nextnode = current.nextnode

        current.nextnode = previous
        
        previous = current
        current = nextnode

    return previous

# creating list
if __name__ == "__main__":
    
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d

    head = a

    # printing the linked list
    n = head
    for _ in range(4):
        print(n.value)
        n = n.nextnode

    head = ReverseList(head)

    # printing the linked list
    n = head
    print('\nAfter Reversal')
    for _ in range(4):
        print(n.value)
        n = n.nextnode
