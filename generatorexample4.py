# generator exmaple
def generator():
       print("first item")
       yield 10
       print("second item ")
       yield 20
       print("third item")
       yield 30

try:
       output1=generator()
       print(next(output1))
       print(next(output1))
       print(next(output1))
       print(next(output1))

except StopIteration:
       print("ALL RESULTS DISPLAYED")
