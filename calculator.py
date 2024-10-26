# from tkinter import *
# import math
# class MyWindow:
#   def __init__(self,win):
#        self.lbl1=Label(win,text="first no")
#        self.lbl2=Label(win,text="second no")
#        self.lbl=Label(win,text="result")
#        self.t1=Entry()
#        self.t2=Entry()
#        self.t3=Entry()

#        self.lbl1.place(x=100,y=50)
#        self.t1.place(x=200,y=50)
#        self.lbl2.place(x=100,y=100)
#        self.t2.place(x=200,y=100)
#        self.b1=Button(win,text="Add",command=self.add) #another approch
#        self.b2=Button(win,text="subtract")
#        self.b3=Button(win,text="multiply")
#        self.b4=Button(win,text="sqrt")
#        self.b2.bind('<Button-1>',self.sub) #old approch
#        self.b1.place(x=100,y=150)
#        self.b2.place(x=200,y=150)
#        self.b3.place(x=300,y=150)
#        self.b4.place(x=370,y=150)
#        self.b4.bind('<Button-1>',self.calc)
#        self.lbl.place(x=100,y=200)
#        self.t3.place(x=200,y=200)
# def add(self):
#     self.t3.delete(0,'end')
#     num1=int(self.t1.get()) # to read data from text box
#     num2=int(self.t2.get())
#     result=num1+num2
#     self.t3.insert(END,str(result))        
# def sub(self,event):
#     self.t3.delete(0,'end')
#     num1=int(self.t1.get()) # to read data from text box
#     num2=int(self.t2.get())
#     result=num1-num2
#     self.t3.insert(END,str(result)) # to disply value within a text box
# def calc(self,event):
#     self.t3.delete(0,'end')
#     num1=int(self.t1.get())
#     result=math.sqrt(num1)
#     self.t3.insert(END,str(result))
# window=Tk()      
# myWin=MyWindow(window)
# window.title("hello python")
# window.geometry("400x300+10+10")
# window.configure(bg="pink")#changing the bg color
# window.mainloop()






# from tkinter import *
# import math
# class MyWindow:
#     def __init__(self,win):
#         self.lbl1=Label(win,text='First number')
#         self.lbl2=Label(win,text='Second number')
#         self.lbl=Label(win,text='Result')
#         self.t1=Entry()
#         self.t2=Entry()
#         self.t3=Entry()
        
#         self.lbl1.place(x=100,y=50)
#         self.t1.place(x=200,y=50)
#         self.lbl2.place(x=100,y=100)
#         self.t2.place(x=200,y=100)
#         self.b1=Button(win,text='Add' ,command=self.add) #Another Approach
#         self.b2=Button(win,text='Subtract')
#         self.b3=Button(win,text='Multiply')
#         self.b4=Button(win,text='Sqrt')
#         self.b2.bind('<Button-1>' ,self.sub) #Old Approach
#         self.b1.place(x=100,y=150)
#         self.b2.place(x=200,y=150)
#         self.b3.place(x=300,y=150)
#         self.b4.place(x=370,y=150)
#         self.b4.bind('<Button-1>' ,self.calc)
#         self.lbl.place(x=100,y=200)
#         self.t3.place(x=200,y=200)
       
#       def add(self):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get()) #To read data from a Text BOX
#         num2=int(self.t2.get())
#         result=num1+num2
#         self.t3.insert(END , str(result))  #To display a value within a Text Box
        
#       def sub(self,event):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get()) 
#         num2=int(self.t2.get())    
#         result=num1-num2 
#         self.t3.insert(END,str(result))  
       
        
#       def calc(self,event):
#         self.t3.delete(0,'end')    
#         num1=int(self.t1.get())
#         result=math.sqrt(num1)
#         self.t3.insert(END ,str(result))
# #     except ValueError:
# #         print("it is not proper value...please renter")
    
      

        
# window =Tk()
# mywin=MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.configure(bg="pink")  #Changing the window Background colo ur

# window.mainloop()


#assingmnent--
# third text box is disabled
# not possible to calcuate  put Exception using try catch when invalid value



##---
#Event Handling
# For handling event there are two methods===>> bind and command
# from tkinter import*
# import math
# class MyWindow:
#     def _init_(self,win):
#         self.lb1=Label(win,text="First Number")
#         self.lb2=Label(win,text="Second Number")
#         self.lb3=Label(win,text="Result")
#         self.t1=Entry()
#         self.t2=Entry()
#         self.t3=Entry(state="readonly")

#         self.lb1.place(x=100,y=50)
#         self.t1.place(x=200,y=50)
#         self.lb2.place(x=100,y=100)
#         self.t2.place(x=200,y=100)
#         self.b1=Button(win,text="Add",command=self.add)  #event handler   #another approach
#         self.b2=Button(win,text="Subtract")
#         self.b3=Button(win,text="Mutiply")
#         self.b4=Button(win,text="Sqrt")
#         self.b2.bind('<Button-1>',self.sub)  # old approach   $$$$$ bind-->for handling event
#         self.b1.place(x=100,y=150)
#         self.b2.place(x=200,y=150)
#         self.b3.place(x=300,y=150)
#         self.b4.place(x=370,y=150)
#         self.b4.bind('<Button-1>',self.calc)
#         self.lb3.place(x=100,y=200)
#         self.t3.place(x=200,y=200)
   
#     def update_result(self, result):
#         self.t3.config(state='normal')  # Temporarily set to normal so it can be edited
#         self.t3.delete(0, 'end')  # Clear the entry box
#         self.t3.insert(END, str(result))  # Insert the result
#         self.t3.config(state='readonly')
   
#     def add(self):
#         self.t3.delete(0,'end')
#         try:
          
#           num1=int(self.t1.get()) #to read data from a text box
#           num2=int(self.t2.get()) 
#           result=num1+num2
#           self.update_result(result)#to display a value within a text box
#         except ValueError:
#           self.t3.insert(END,"INVALID")    

#     def sub(self,event):
#           self.t3.delete(0,'end')
#           try:
#                num1=int(self.t1.get()) 
#                num2=int(self.t2.get()) 
#                result=num1-num2
#                self.update_result(result)
#           except ValueError:
#                 self.t3.insert(END,"Invalid")     


#     def calc(self,event):
#           self.t3.delete(0,'end')
#           try:
#               num1=int(self.t1.get())
#               result=math.sqrt(num1)
#               self.update_result(result)
              
#           except:
#               self.t3.insert(END,"Invalid input")
         
# window=Tk()
# mywin=MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.configure(bg="pink")
# window.mainloop()


from tkinter import*
import math
class MyWindow:
    def __init__(self, win):
        self.lb11 = Label(win, text="First Number")
        self.lb12 = Label(win, text="Second Number")
        self.lb13 = Label(win, text="Result")
        self.t1 = Entry()
        self.t2 = Entry()
        self.result_label = Label(win, text="")  # Changed to Label for result
        
        self.lb11.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lb12.place(x=100, y=100)
        self.t2.place(x=200, y=100)

        self.b1 = Button(win, text='Add', command=self.add)
        self.b2 = Button(win, text='Subtract', command=self.sub)
        self.b3 = Button(win, text='Multiply', command=self.multiply)
        self.b4 = Button(win, text='Sqrt', command=self.calc)

        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.b3.place(x=300, y=150)
        self.b4.place(x=370, y=150)

        self.lb13.place(x=100, y=200)
        self.result_label.place(x=200, y=200)  # Use Label for result

    def add(self):
        self.calculate_add()

    def sub(self):
        self.calculate_subtract()

    def multiply(self):
        self.calculate_multiply()

    def calc(self):
        self.calculate_sqrt()

    def calculate_add(self):
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            result = num1 + num2
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="Invalid input!")

    def calculate_subtract(self):
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            result = num1 - num2
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="Invalid input!")

    def calculate_multiply(self):
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            result = num1 * num2
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="Invalid input!")

    def calculate_sqrt(self):
        try:
            num1 = float(self.t1.get())
            result = math.sqrt(num1)
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="Invalid input!")

window = Tk()
mywin = MyWindow(window)
window.title("Calculator")
window.geometry("500x300+10+10")
window.configure(bg='orange')
window.mainloop()   

