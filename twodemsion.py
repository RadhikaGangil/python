#creating two demsional array
import numpy as np
arr1=np.array([[1,2,3,],[4,5,6]])
arr2=np.array([[0,-4,4],[3,2,9]])
print("array details")
print(arr1)
print("demsion of array is =%s"%(arr1.ndim))
print(arr2)
print("demsion of array is =%s"%(arr2.ndim))

arr3=arr1-arr2
print("Result array")
print(arr3)

arr4=np.array([[3,0],[4,-1],[0,1]])
arr5=arr1.dot(arr4)
print("result after multiplication")
print(arr5)
