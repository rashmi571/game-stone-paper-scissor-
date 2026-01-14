def bs(l,target):
    st=0
    end=len(l)-1

    while(st <= end):
        mid=(st + end)//2
        
        if(l[mid] == target):
            return mid
        elif(l[mid] < target):
            st = mid+ 1
        else:
            end = mid - 1


l=[1,2,3,4,5,6,7]            
target=7
result=bs(l,target)             

if(result != -1):
    print(f"{target} is find at index {result}")
else:
    print(f"{target} is not find")     