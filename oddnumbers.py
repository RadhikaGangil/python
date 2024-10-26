#ITERATOR EXAMPLE:::

class Counter:
    def __init__(self,low,high):
        self.current =low
        self.high =high
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>self.high:
            raise StopIteration
        else:
            self.current +=1
            return self.current -1
        
counter = Counter(1,11)
for number in counter:
    if(number%2!=0):
        print(number)
    
   


 