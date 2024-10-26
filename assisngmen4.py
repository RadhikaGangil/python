#using concept generator 
#evalute 1+4+9+16+25=? 
def sq(n):
       for i in range (1,n+1):
              yield i*i
              
              
sq1= sum(sq(5))
print(sq1)

              
