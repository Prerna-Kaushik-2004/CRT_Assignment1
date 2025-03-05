'''Ques-5: Write a function that takes a list as an argument and modifies it by
appending a new item. Demonstrate how changes to the list inside the
function affect the list outside the function.
Ans: In Python, when we pass a mutable object (like a list) to a function, any changes made to that object inside the function will affect the object outside the function as well. This is because the object is passed by reference, not by value. So, when we modify the object inside the function, we are modifying the original object, not a copy of it. 

This is demonstrated in the following code snippet:
'''
def new_list(old_list):
    old_list.append(10)
    print(old_list)
old_list=[1,2,3,4,5,6,7,8,9]
print("Old List outside the function before function execution: ",old_list)
new_list(old_list)
print("Old List outside the function after execution of the function: ",old_list)