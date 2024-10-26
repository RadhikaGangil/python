def my_decorator(func):
       def wrapper():
              print("before the function is called")
              func()
              print("after the function is called")
       return wrapper
@my_decorator#decorator is used


def say_hello():
       print("hello")

say_hello()       
       