# Write a program to create a NumPy array and display it.
import numpy as np

array=np.array([[1,2,3],[4,5,6]])
print("Numy array")
print(array)

# Create a NumPy array and find its mean, median, and standard deviation,maximum and minimum
ar1=np.array([1,2,3,4,5,6,7,8,9,10])
print("Mean -> ",np.mean(ar1))
print("Median -> ",np.median(ar1))
print("Standerd deviation -> ",np.std(ar1))
print("Minimum number -> ",np.min(ar1))
print("Maximum number -> ",np.max(ar1))


# Sort a NumPy array in ascending  or decending order.
ar2=np.array([10,5,4,3,7,6,5,4,2])
print("Sort array ascending")
print(np.sort(ar2))
print("Sort array decending")
print(np.sort(ar2)[::-1])

# Write a program to filter elements greater than a given value in a NumPy array.
ar3=np.array([20,78,9,56,75,43,56,89,0,3,4,34,32,46,98])
filter=ar3[ar3 > 70]
print("Number is filter")
print(filter)

# Add two NumPy arrays element-wise.
a1=np.array([1,2,3,4])
a2=np.array([5,6,7,8])

add_array=a1 + a2
print("add two array")
print(add_array)

# Write a program to reshape a 1D NumPy array into a 2D array.
arr4=np.array([1,2,3,4,5,6])
resize=arr4.reshape((2,3))
print("reshape array to create 2d array")
print(resize)

# Find the sum of all elements in a NumPy array.
arr5=np.array([1,2,3,4,5,6])
print("Sum of all elements in array -> ",np.sum(arr5))

# Write a program to perform basic mathematical operations (add, subtract, multiply) on NumPy arrays.
arr6=np.array([1,2,3,4,5,6])
add=arr6 + 2
subtract=arr6 - 4
multi=arr6 * 2
print("Add operation in array -> ",add)
print("subtract operation in array -> ",subtract)
print("Multiply operation in array -> ",multi)

# Write a program to find unique elements in a NumPy array.
arr7=np.array([1,2,2,3,1,4,4,5,5,6,7,8,7,9,9])

print("unique value in array")
print(np.unique(arr7))

