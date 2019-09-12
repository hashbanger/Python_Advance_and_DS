class Node(object):

    def __init__(self, value, nextnode = None):
        self.value = value
        self.nextnode = nextnode

# if __name__ == '__main__':
#     l1 = Node(1)
#     l2 = Node(2)
#     l3 = Node(3)
#     l4 = Node(4)

#     l1.nextnode = l2
#     l2.nextnode = l3
#     l3.nextnode = l4
    
#     n = l1
#     for _ in range(4):
#         print(n.value)
#         n = n.nextnode
