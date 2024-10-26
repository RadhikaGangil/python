#intialize the list 
# import sys # module -is used to forcefully close the prorgam 
# my_list=[2,1,3,6,10]
# a=(x**2 for x in my_list)
# # print(a)
# if(next(a)>=3):     #a is a itrerator 
#  sys.exit()
# print(list(a))
# print(type(a))


# # second way using generator
# def my_gen():
#  n=4
#  mylist=[10,3,45,8,7,24,6,15,82,19,37]
#  print("first 4 number")
#  #genertor funtion contian yeild statement
#  newlist=mylist[:n]
#  print(newlist)


#  newlist=my_list[:n+4]
#  yield newlist

#  n+=1
#  print("this print last")
#  yield  n 
# next(my_gen()) 


# #p>>>2
# sq=[k*k for k in range(1 ,11)]
# print(sq)


# #p>>>3
# Numlist=[y for y in range(1,21)if y%2==0 if y%5==0]
# print(Numlist)



#p>>>4
# i=0
# matrix=[[1,2],[3,4],[5,6]]
# trmatrix=[[row[i] for row in matrix]for y in range(0,3)]
# print(trmatrix)

i=0
matrix=[[1,2],[3,4],[5,6]]
Trmatrix =[[row[i] for row in matrix]for y in range(0,3)]
print(Trmatrix)