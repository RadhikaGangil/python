#deocrtator work on function specaility is that using it can return a functiom
'''
associating decorator with a function
defining my_decorator for a function 
'''
def mydecorator(func):
       def wrapper():
              func()
              print("good morning")
              print("have a nice day")
       return wrapper
@mydecorator
def sayhello():
       print("hello friend")
sayhello()       #here function sayhello is being called       
