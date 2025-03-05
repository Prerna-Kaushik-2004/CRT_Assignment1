'''Ques-4: Write a function max_consecutive_sum(nums, k) that finds the
maximum sum of k consecutive elements in a list.'''
def max_consecutive_sum(num,k):
    max_sum=0
    for i in range(k):
        max_sum+=num[i]
    return max_sum
k=int(input("Enter the number of elements in the list: "))    
num=[int(input("Enter the elements of the list: ")) for i in range(1,10)]
print(num)
print("The maximum sum of consecutive elements in the list is: ",max_consecutive_sum(num,k))