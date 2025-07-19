#Write a program to return - 1. zipped list from two lists 
#2. elements of two lists zipped together, but 2nd list in reverse order 
#3. elements of two lists zipped into a dictionary
set1=[1,2,3,4,5,6,7,8]
set2=["a","b","c","d","e","f","g"]
set3=zip(set1,set2)
print(list(set3))
list2=set2[::-1]
list4=zip(set1,list2)
print(list(list4))
