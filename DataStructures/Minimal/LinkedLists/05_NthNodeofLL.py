# Nth node of a Linked List
# 1--2--3--|4|--5--6
# The 4th node will be 4


# Implementing a node
class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

# Returning Nth Node of a list
def nthNode(num, head):
    current = head

    while num-1 > 0 :
        current = current.nextnode
        num = num - 1
    return current.value

# creating list
if __name__ == "__main__":
    
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)


    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e
    e.nextnode = f

    head = a

    # printing the linked list
    n = head
    for _ in range(6):
        print(n.value)
        n = n.nextnode

    print('\n4th Node of the list is\n')
    print(nthNode(4, head))