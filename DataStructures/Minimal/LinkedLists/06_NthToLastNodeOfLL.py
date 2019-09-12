# Nth to last node of a Linked List
# 1--2--3--|4|--5--6
# The 2nd to last node will be 4

# Implementing a node
class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

# Returning Nth Node of a list

# Method 1 (by finding the length first)
def nthToLastNode1(num, head):
    current = head
    length = 0
    while current:
        current = current.nextnode
        length = length + 1
    
    counter = 0
    current = head
    while counter != (length - num)-1:
        current = current.nextnode
        counter = counter + 1

    return current.value

# Method 2 (Using two pointers)
def nthToLastNode2(num, head):

    leftPointer = head
    rightPointer = head

    while num > 0:
        rightPointer = rightPointer.nextnode
        num = num - 1

    while rightPointer.nextnode:
        rightPointer = rightPointer.nextnode
        leftPointer = leftPointer.nextnode

    return leftPointer.value


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

    print('\n2nd to last node in the list is (Using Length Mehtod)')
    print(nthToLastNode1(2, head))

    print('\n4th to last node in the list is (Using Pointers Mehtod)')
    print(nthToLastNode2(4, head))