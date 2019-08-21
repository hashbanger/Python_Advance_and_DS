#Implementing a queue
#By Prashant Brahmbhatt (linkedin.com/in/prashantbrahmbhatt)


class Queue:
    def __init__(self):
        self.queue = list()
        self.front = 0
        self.rear = 0
        self.maxSize = 10
        
    def enqueue(self, data):
        #Checking for duplicates
        if self.rear < self.maxSize:
            if self.front is 0:
                self.queue.append(data)
                self.front = self.front +1
                self.rear = self.rear +1
                
            else:
                if data not in self.queue:
                    self.queue.append(data)
                    self.rear = self.rear + 1
                    return None
                else:
                    print("Duplicate Entry")
                    return None
        else:
            print("Queue Overflow")
            return None

    def dequeue(self):
        if self.rear <= 0:
            print("Queue Underflow")
            return None
        else:
            item = self.queue[self.front - 1]
            self.front = self.front + 1
            print("{} popped\n".format(item))
            return None

    def printQueue(self):
        if self.rear <=0:
            print("Queue Empty")
            return None
        else:
            for i in range(self.front-1, self.rear):
                print("{}".format(self.queue[i]))
            return None
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.printQueue()

            
