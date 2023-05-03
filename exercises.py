# 1.Write a function to reverse a string in Python without using any built-in functions.
def stmt(word):
    new=""
    for w in range(len(word)-1,-1,-1):
        new+=word[w]
    return new  

# 2.Write a function that takes an array of integers and returns the sum of all the even numbers in 
# the array.  
def evennum (nums):
    num=0
    for i in nums:
        if i%2==0:
            num+=i
    return num   
#3.Write a function that takes an array of integers and returns the sum of all the odd numbers in
# the array. 
def oddnum (numbs):
    numb=0
    for n in numbs:
        if n%2 !=0:
            numb+=n
    return numb  

#4.Write a function that takes an array of integers and returns the largest number in the array.
def largenum (arraynum):
    largest=arraynum[0]
    for l in arraynum:
        if l>largest:
            largest=l
    return largest 

#5.Write a function that takes an array of integers and returns the smallest number in the array.  
def smallnum (nums):
    smallest = nums[0]
    for s in nums:
        if s < smallest:
            smallest=s
    return smallest  

#6.Write a function that takes an array of integers and returns a new array with all the even numbers 
#removed.        
def arrayeven(evens):
    empty=[]
    for num in evens:
        if num % 2 != 0:
            empty.append(num)
    return empty

#7.Write a function that takes an array of integers and returns a new array with all the odd numbers
#removed.
def oddarray (odds):
    empty=[]
    for num in odds:
        if num % 2 ==0:
           empty.append(num)
    return empty  

#8.Write a function that takes an array of integers and returns a new array with all the duplicates 
#removed.         
def remove_dups (numbs):
    new=[]
    for n in numbs:

        if n not in (new):

           new.append(n)

    return new    

#9.Write a function that takes an array of integers and returns the second largest number 
#in the array.
def second_largest(integers):
    for n in integers:
         integers.sort()
         
    return integers[-2]

#10.Write a function that takes two arrays of integers and returns a new array containing the
#elements that appear in both arrays.
def two_arrays(arr,arr1):
    my_arr=set(arr)
    my_arr2=set(arr1)  
    new_list= list(my_arr.intersection(my_arr2))
    return new_list

#11.Write a function that takes two strings and returns a new string containing 
#the characters that appear in both strings.
def two_strings(str2,str1):
    u=set(str2)
    z=set(str1)
    new_string=u.intersection(z)
    t="".join(new_string)
    return t

#12.Write a function that takes an array of integers and returns a new array 
#containing only the prime numbers.   
def prime_array(prime):
    newArray=[]
    for i in prime:
        if i > 1:
            for num in range(2,i):
                if i%num == 0:
                    break
            else:
                newArray.append(i)       
    return newArray  

#13.Write a function that takes an array of integers and returns the product
#of all the numbers in the array.
def products(numbs):
    num=1
    for m in numbs:
        num*=m
    return num  
# **#14.Write a function that takes an array of integers and returns the median value.
def find_median(values):
    for x in values:
        values.sort()
    return values
# Write a function that takes an array of integers and returns the mode value.

# Write a function that takes an array of integers and returns the range of the
#  numbers in the array.

# Write a function that takes an array of integers and returns the average of the
# numbers in the array.

# Write a function that takes a string and returns the number of words in the string.
def statement(stmt):
    for w in stmt:
        stmt.count(w)
    return stmt    

# Write a function that takes an array of strings and returns a new array with all 
# the strings capitalized.

# Write a function that takes an array of strings and returns a new array with all the 
# strings sorted alphabetically.

            # revision
# Write a python function that takes one argument as a list a = [2,4,6,8] and remove the
#  second last item from that list and returns the whole list without the removed item    
def remove_item(argslist):
    argslist.pop(-2)
    return argslist

# Write a python program that has a list days = [ “Monday”, “Tuesday”, “Friday”, “Monday”] and 
# counts the number occurrences of Monday
def count_occurences(weekdays):
    sum=0
    for i in weekdays:
        if i=="monday":
            sum+=1
    return sum


# Write a Python function named smallest that accepts a list of unsorted integers and returns the
#  smallest number in the list. Example:
# smallest([3,6,8,2,4,1,5,7]) returns 1
def small_num(small):
    for n in small:
        small.sort()
    return small[0]
# Write a python function named divisible_by_seven that; using the range function and a for loop
# returns a list containing all the numbers between 100 and 200 that are divisible by 7.
def divisible_by_seven():
    












    








