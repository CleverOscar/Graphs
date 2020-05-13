# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        #declaring list, 
        self.queue = [] # a collection which is ordered and changeable
    #add value passed into queue
    def enqueue(self, value):
        #append() adds value passed into queue
        self.queue.append(value)
    #removes item same order it was added
    def dequeue(self,value):
        #if the size of queue is greater than 0
        if self.size() > 0:
            # pop(0) removes item from specified position which is 
            # currently 0
            return self.queue.pop(0)
        else:
            #if there is no itme, return None
            return None
        #checking length of queue
    def size(self):
        #len() returns length of list
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = [] #a collection which is ordered and changeable
        
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size.stack > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
    