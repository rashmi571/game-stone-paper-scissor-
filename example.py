# #Print “Hello, World!”
# print("Hello, World")

# # Take a number as input and check if it is even or odd
# n=int(input("enter the number to check even or not: "))

# if(n%2 == 0):
#     print("Number is even.")
# else:
#     print("Number is odd.")    
# # Find the largest of three numbers
# a=int(input("enter the number a: "))
# b=int(input("enter the number b: "))
# c=int(input("enter the number c: "))

# if(a >= b and a>=c):
#     print(f"{a} is largest more than {b},{c}")
# elif(b >= a and b >= c):
#     print(f"{b} is the largest more than {a},{c} ")
# else:
#    print(f"{c} is the largest more than {a},{b} ")         

# # Print numbers from 1 to 100
# for i in range(1,101):
#     print(i)

# # Print the multiplication table of a number
# n=int(input("enter the number n: "))

# for i in range(1,11):
#     print(f"{n}x{i} = {n*i}")

# # Find the sum of digits of a number
# n=int(input("entr the number: "))
# digit=0
# while(n > 0):
#     rem=n%10
#     digit += rem
#     n=n//10

# print("sum of a digit",digit)    
    
# # Reverse a given number
# n=int(input("entr the number: "))
# c=n
# rev=0
# while(n > 0):
#     rem=n%10
#     rev =rev*10 + rem
#     n= n//10

# print(f"{c} Number is reversed {rev}")  

# # Check if a number is prime
# n=int(input("enter the number: "))

# if(n <= 1):
#     print("number is not prime")
# else:
#     is_prime=True
    
#     for i in range(2,n):
#         if(n%i == 0):
#             is_prime=False
#             break

# if(is_prime):
#     print("number is prime")
# else:
#     print("number is not prime")        
        
        
# # Find the factorial of a number
# n=int(input("enter the number: "))
# fact=1
# for i in range(1,n+1):
#     fact *= i

# print(f"factorial of {n} = {fact}")

# # Check if a string is a palindrome
# n=int(input("enter th number:  "))
# c=n
# pali_Num=0
# while(n > 0):
#     rem=n%10
#     pali_Num =rem +(pali_Num * 10)
#     n=n//10
    
# if(c == pali_Num):
#     print("Number is palidrome")
# else:
#     print("Number is not palidrome")
    
            
# # Count vowels and consonants in a string
# text=input("enter the string: ").lower()
# vowel="aeiou"

# vowel_count=0
# cons_count=0

# for char in text:
#     if char in vowel:
#         vowel_count += 1
#     elif char.isalpha():
#         cons_count += 1

# print(f"vowels in the string: {vowel_count}\n consonanats in a string: {cons_count}")            

# # Find duplicate elements in a list
# l=[1,2,2,3,4,5,4,5,3,8]
# seen=set()
# count_dup=0

# for i in l:
#     if i in seen:
#         count_dup += 1
#     else:
#         seen.add(i)
        
# print("duplicate values in list : ",count_dup)        
        

# # Sort a list without using sort()
# l=[1,2,2,3,4,5,4,5,3,8]
# n=len(l)

# for i in range(n):
#     for j in range(0,n-i-1):
#         if l[j] > l[j+1]:
#             temp = l[j]
#             j[j] = l[j+1]
#             l[j+1] = temp

# print("sorted list",l)        

# Find the second largest number in a list
# l=[1,2,3,4,7,5,6]
# n=len(l)

# first_largest=max(l)
# second_largest=float('-inf')

# for i in l:
#     if i < first_largest and i > second_largest:
#         second_largest=i 

# print("first largest in list ->",first_largest)
# print("second largest in list -> ",second_largest)


# # Merge two lists into a dictionary
# list1=[1,2,3]
# list2=[4,5,6]

# d=dict(zip(list1,list2))

# print(d)
# # Count word frequency in a sentence
# text=input("enter the sentence: ").lower()
# words=text.split()
# word_freq={}

# for word in words:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] =1

# for w, freq in word_freq.items():
#     print(f"{w} frequancy in sentence: {freq} ")         
        


# Remove duplicates from a list
# lst=[1,2,2,3,4,5,5,5,]
# seen=set()
# for i in lst:
#     if i not in seen:
#         seen.add(i)

# print(seen)        
# # Find the intersection of two lists
# l1=[1,2,3,4,5,6]
# l2=[4,6,7,5,8,2,0]

# intersection=[]

# for i in l1:
#     if i in l2 and i not in intersection:
#         intersection.append(i)
        
# print(intersection)        

# # Check if two strings are anagrams
# s1="listen"
# s2="silent"

# if len(s1) != len(s2):
#     print("string not anagrams")
# else:
#     count={}
    
#     for ch in s1:
#         count[ch] =count.get(ch,0)+1
#     for ch in s2:
#         if ch not in count or count[ch] == 0:
#             print("not anagram")
#             break
#         count[ch] -= 1
#     else: 
#         print("strings are anagram")
        
#generate random password
import random
import string

n=int(input("enter the length of password: "))

characters = string.ascii_letters + string.digits + string.punctuation
password=" "
for i in range(n):
    password += random.choice(characters)
    
print("generate random password:  ",password)    
        
                        