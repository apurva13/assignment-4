#Q.1- Reverse the whole list using list methods.
List=[1,2,3,4,5]
List.reverse() #or we can use slice operator [::-1] as print(List[::-1])
print("Reverse List:",List)

#Q.2- Print all the uppercase letters from a string.
String="Welcome To World Of Python"
upper=""
for letter in String:
    if letter.isupper():
        upper=upper+letter+','
print("All uppercase letters:",upper)

#Q.3-Split the user input on comma's and store the values in a list as integers.
value=input("Enter input:")
a=value.split(',')
b=[]
for i in a:
    b.append(int(i))
print(b)
# we can also do this :a=[int(i) for i in a] then print(a)

#Q.4- Check whether a string is palindromic or not.
String="redivider"
rev=String[::-1]
if String==rev:
    print('String is a palindrome')
else:
    print('String is not a palindrome')

#Q.5- Make a deepcopy of a list.
#Also write the difference between shallow copy and deep copy.
import copy as c
l1=[1,2,3,[4,6],5]
l2=c.deepcopy(l1)
l1[3][1]='Hey'
l1[2]='Hi'
print(l1)
print(l2)

"""
The difference between shallow copy and deep copy:
->is for objects that contains other object like list containing list inside

1.A SHALLOWCOPY of an object won't create a copy of nested objects,instead it just copies the reference of nested objects.
Therefore, the copy is not fully independent of the original.

2.Whereas in Deepcopy of an object it creates independent copy of original object and all its nested objects.
Therefore, the copy is fully independent of the original, but creating a deep copy is slower.

"""












