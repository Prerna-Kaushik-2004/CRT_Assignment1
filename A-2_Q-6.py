'''Ques-6: Take a number as input and print the Fibonacci sequence up to that
many terms using User-defined functions. '''
last_ele=int(input("Enter the numbers: "))
def fibonacci_series(last_ele):
    a=0
    b=1
    print(a,end=" ")
    for i in range(last_ele):
        a,b=b,a+b
        print(b,end=" ")
fibonacci_series(last_ele)