import numpy as np

lst=[1,2,3,4,5,6]

new_arr=np.array(lst)
print(new_arr)

# Create a NumPy array of zeros of size 10.
arr=np.zeros(10)
print(arr)

# Create a NumPy array of ones with shape (3, 4).
arr=np.ones((3,4))
print(arr)


# Create an array of numbers from 10 to 50.
arr=np.arange(10,60,10)
print(arr)

# Create an array of even numbers between 1 and 20.
arr=np.arange(2,21,2)
print(arr)

# Find the datatype of a NumPy array.
arr=np.array([1.0,8.0,9.0])
print(arr.dtype)

# Convert a float array into an integer array.
arr=np.array([1.0,8.0,9.0])
new_arr=arr.astype(int)
print(new_arr)

# Find the length of a NumPy array.
arr=np.array([[1,2],[3,4],[5,6]])
print(arr.shape)

# Access the 3rd element of an array.
arr=np.array([1.0,8.0,9.0,10.0])
print(arr[3])

# Reverse a NumPy array.
arr=np.array([1.0,8.0,9.0])
rev=arr[::-1]
print(rev)

# Generate a random array of size 5.
arr=np.random.rand(5)
print(arr)

# Create a 3×3 identity matrix.
arr=np.eye(3,3)
print(arr)

# Sort a NumPy array.
arr=np.array([4,5,3,2,6,7,1])
new_sort=np.sort(arr)
print(new_sort)


# Find the index of the maximum value.
arr=np.array([4,5,3,2,6,7,1])
print(max(arr),"at the inedx",np.argmax(arr))


# Stack two arrays vertically.
rr1=np.array([10,20,30])
arr2=np.array([40,50,60])
print(np.vstack((rr1,arr2)))

# Apply boolean masking to filter values greater than 50.
arr=np.array([10,20,30,40,50,60,90,100])
new_arr=arr[arr > 50]
print(new_arr)

# Compute the dot product of two arrays.
a1=np.array([1,2,3])
a2=np.array([2,2,2])
print(a1 * a2)

# Find the standard deviation of an array.
arr=np.array([10,30,7,68,99,30])
print(np.std(arr))

# Remove duplicate elements from a NumPy array.
arrr=np.array([1,3,2,2,4,5,4,5,6])
new_arr=np.unique(arrr)

print(new_arr)

# Create a 2D array of shape (3,3) with numbers 1 to 9.
arr_2d=np.arange(1,10,1)
new_arr2d=arr_2d.reshape(3,3)
print(new_arr2d)

# Access the second row of a 2D array.
arrr=np.array([[1,3,2],[2,4,5],[4,5,6]])
print(arrr[1])

# Access the last column of a 2D array.
arrr=np.array([[1,3,2],[2,4,5],[4,5,6]])
print(arrr[:,2])

# Find the maximum and minimum values in an array.
arr=np.array([10,20,30,40,50,60,90,100])
max_value=max(arr)
min_value=min(arr)
print(f"maximum value of the array {max_value} and minimum value of the array {min_value}")


# Find the sum and mean of an array.
a=np.array([1,2,3,4,5])
sum_array=np.sum(a)
mean_value=np.mean(a)
print("sum of all values in array: ",sum_array)
print("Average(mean) value of array: ",mean_value)

# Perform element-wise addition of two arrays.
a1=np.array([1,2,3,4])
a2=np.array([2,2,2,2])
add_arr=a1+a2
print(add_arr)

# Multiply all elements of an array by 5.
arr=np.array([1,2,3,4,5,6,7,8,9,10])
multiple_a=arr*5
print(multiple_a)

# Replace all odd numbers in an array with -1.
a=np.array([2,3,4,5,6,7,8])
a[a%2 != 0]=-1
print(a)

# Count the number of elements greater than 10.
a=np.array([1,2,10,30,14,2,5,0,50,87,65,11,21])
count_value = np.sum(a > 10) 
print(count_value)

# Reshape a 1D array of size 12 into (3,4).
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.reshape((3,4)))

# Check if two NumPy arrays are equal.
a1=np.array([1,2,3,4,5])
a2=np.array([1,2,3,4])
find_equality=(len(a1) == len(a2))
print(find_equality)


# Find missing numbers from an array containing numbers 1 to 10.
a=np.array([1,np.nan,3,4,5,6,np.nan,8,9,10])
clean_arr = a[~np.isnan(a)].astype(int)#nan clear
full = np.arange(1, 11)#compare with full range
missing = np.setdiff1d(full, clean_arr)#find num

print(missing)

# Normalize a NumPy array (values between 0 and 1).
a1=np.array([1,2,3,4,5])
normalize_num = (a1 - a1.min()) / (a1.max() - a1.min())
print(normalize_num)

# Swap two rows of a 2D array.
a2=np.array([[1,2,3],[4,5,6]])
a2[[0,1]]=a2[[1,0]]

a2[:, [0, 2]] = a2[:, [2, 0]]

print(a2)

# Find the row-wise sum of a 2D array.
a2=np.array([[1,2,3],
             [4,5,6]])
sum_num=np.sum(a2,axis=1)
print(sum_num)


# Find the column-wise mean of a 2D array.
a2=np.array([[1,2,3],
             [4,5,6]])
mean_num=np.mean(a2,axis=0)
print(mean_num)

# Replace NaN values with 0.
a=np.array([1,np.nan,3,4,5,6,np.nan,8,9,10])
new_array=np.nan_to_num(a)
print(new_array)

# Find common elements between two arrays.
p=np.array([1,2,3,4,5])
p2=np.array([4,3,5,7,8])
comman_value=np.intersect1d(p,p2)
print(comman_value)

# Flatten a 2D array.
arr_2D=np.array([[10,20,30],[40,50,60]])
print(arr_2D.flatten())

# Find cumulative sum of an array.
arr = np.array([1, 2, 3, 4, 5])

cum_sum = np.cumsum(arr)
print(cum_sum)

# Given marks of students, calculate average, max, min.
marks=np.array([89,90,80,70,60,45,30,65,30])
print("Average marks of student: ",np.mean(marks),
      "\n Maximum marks of student: ",np.max(marks),
      "\n Minimum marks of student: ",np.min(marks))

# Given daily temperatures, find days above average.
temp=np.array([89,90,80,70,60,45,30,65,30])
avg=np.mean(temp)
print(avg)

days=temp[temp > avg]
print(days)

# Create a matrix and find its transpose.
arr_2D=np.array([[10,20,30],[40,50,60]])
tranpose=arr_2D.T
print(tranpose)

# Apply vectorization instead of loops.
a=np.array([1,2,3,4,5])
multi=(a*5)
print(multi)

# Simulate rolling a dice 1000 times and find frequency.
rolls = np.random.randint(1, 7, size=1000)

# Count frequency of each face (1 to 6)
faces = np.arange(1, 7)
frequency = np.array([np.sum(rolls == face) for face in faces])

print("Dice faces:", faces)
print("Frequency:", frequency)
