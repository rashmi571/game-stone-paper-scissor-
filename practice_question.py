import numpy as np
#decleration of numpy

arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(arr)

#creating array with list np.array([1,2,3])
a=np.array([1,2,3,4])
print(a)

#array with default values np.zeros(shape)
b=np.zeros(3)#3 degit in matrix
print(b)

#array with all one numbers np.ones((tuple))
c=np.ones((2,3))
print(c)

#array with specific number np.full((2*2),value)
d=np.full((2,2),3)
print(d)

#array with sequece np.arange(st,stop,step) it return array 
e=np.arange(1,10,2)
print(e)

#array with identity matrix np.eye(size)
f=np.eye(3)
print(f)

#properties of numpy
#'1. find row and column using (.shape)
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(arr.shape)#3x3 matrix

#  2. find the size of array (.size)
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(arr.size)#9 values
  
# 3. no. of dimansional find (.ndim) 
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(arr.ndim)#2D array

#4. (.dtype) data type of array
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(arr.dtype)

#5.type conversion astype()
p=np.array([2.3,3.0,5.5,8.0])
int_arr=p.astype(int)
print(int_arr)
print(int_arr.dtype)


#6. mathmatic operation performance
h=np.array([1,2,3,4])
print(h + 2)
print(h - 2)
print(h / 2)
print(h * 2)
print(h % 2)
print(h // 2)

#Aggregation function
#1. np.sum(arr)
#2. np.mean(arr)
#3. np.min(arr)
#4. np.max(arr)
#5. np.std(arr) standered derivation
#6. np.var(arr) verions

arr=np.array([10,20,30,40,50])
print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))

#indexing 1. positive (0) starting  2. negitive (-1) last elementt end
#using sequence data and it take only one value
arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[-1])

#silicing start,stop,step
#sequenc data and it take three value
arr=np.array([10,20,30,40,50,60])
print(arr[1:5])#index 20 t0 50
print(arr[:4])#10 to 40
print(arr[::2])#every second element
print(arr[::-1])#reverse array

#fancy indexing it take multiple value as a list and it create a copy not change in orignal
arr=np.array([10,20,30,40,50,60])
print(arr[[1,4,5]])

#boolen masking or filtering
arr=np.array([10,20,30,40,50,60])
print(arr > 25)

#reshaping array dimension .reshape(rows,columns)
arr=np.array([10,20,30,40,50,60])
print(arr.reshape(2,3))

#flatting type 1. ravel -> modify orignal array return
#2. flatten -> modify in array copy

arr_2D=np.array([[10,20,30],[40,50,60]])
print(arr_2D.ravel())
print(arr_2D.flatten())

#np.insert(array,which index,which value,axix=) 1D array this create copy
#axis -> 0 row wise
#axis -> 1 column wise
#axis -> NOne only single line

arr=np.array([10,20,30,40,50,60])
arr_index=np.insert(arr,2,90,0)
print(arr_index)

#insert in 2D array

arr=np.array([[10,20,30],[40,50,60]])
arr_2D=np.insert(arr,2,[1,1,1],0)
print(arr_2D)

#append in last np.append(array,value)
arr=np.array([10,20,30])
new_arr=np.append(arr,[40,50,60])
print(new_arr)


#concreate two arr np.concatenate((arr1,arr2),axis)
arr1=np.array([10,20,30])
arr2=np.array([40,50,60])
new_arr=np.concatenate((arr1,arr2),0)
print(new_arr)

#removing element np.delete(arr,index number,axis=none) 1d array
Arr=np.array([1,2,3,4,5,6])
print(Arr)
new_Arr=np.delete(Arr,4)#5 deleted
print(new_Arr)

#removing 2D array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)
new_arr=np.delete(arr,0,1)
print(new_arr)

#stacking array
'''np.vstack((arr1,arr2)) -> vertically row wise
   np.hstack((arr1,arr2)) -> hirizontally column wise
'''
arr1=np.array([10,20,30])
arr2=np.array([40,50,60])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

#splitting array -> array divided into subarray 
'''np.split(arr,how many divided array number) ->equal divide
   np.vsplit() -> row wise
   np.hsplit() -> column wise
   '''
arr=np.array([10,20,30,40,50,60])
print(np.split(arr,3))#make three subarrays

#Broadcasting in NumPy means performing operations on arrays of 
# different shapes without using loops
'''NumPy automatically expands the smaller array so shapes match.
    🔹 Why Broadcasting?
        Faster than loops
        Cleaner code
        Less memory usage
'''
prices = np.array([100,200,300])
discount= 10 #scalar -> single value

final_prices = prices -(prices * discount/100)
print(final_prices)

#🔹 Basic Rule of Broadcasting
'''1. matching D -> 2d arr + 2d arr none marching give error
    2. expanding single element -> [1,2,3] + 10 = [11,12,13]
     3. incompatitive shape -> [1,2,3] + [1,2] = error 
     '''
#broadcasting with single value     
arr=np.array([100,200,300])
result=arr*2 
print(result)        

#broadcasting with 1d and 2d array
arr_2d=np.array([[1,2,3],[4,5,6]])
arr_1d=np.array([10,20,30]) 

result=arr_2d + arr_1d
print(result)
 
#Vectorization means doing operations on entire arrays at once instead of using loops
'''Without Vectorization
        import numpy as np

            a = np.array([1, 2, 3, 4])
            b = np.array([10, 20, 30, 40])

            c = np.zeros(4)
            for i in range(4):
                c[i] = a[i] + b[i]

            print(c)

'''
#With Vectorization
a = np.array([1, 2, 3, 4])
print(a * 5)

#handling missing values in array
'''we can't compare the 
np.nan == np.nan values
'''
#built in functions
#1. np.isnan(array) it is used for dected missing value->nan meand not a value
#if give true missing value else false not missing value
arr=np.array([1,2,np.nan,4,5])
print(np.isnan(arr))

#2. np.nan_to_nam(array, nan=value) -> fill the missing place ,by default 0
arr=np.array([1,2,np.nan,4,5])
print(np.nan_to_num(arr,nan=3))

#3.np.isinf(arr) -> find infiniate value this is positive or negitive
arr=np.array([1,2,3,-np.inf,np.inf])
print(np.isinf(arr))
'''replace this space 
    using nan_to_nam function'''
result_fill=np.nan_to_num(arr,posinf=5,neginf=-4) 
print(result_fill)   
 



