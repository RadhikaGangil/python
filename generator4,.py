#fibbonaci series
def fibonacci(n):
       a,b=0,1
       while a<n:
              yield a
              a,b=b,a+b
fib=fibonacci(10)
for num in fib:
       print(num)  #output ---0 1 1 2 3 5 8