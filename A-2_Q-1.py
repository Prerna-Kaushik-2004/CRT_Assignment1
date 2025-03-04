'''Ques-1: Write a function pascals_triangle(rows) that prints the first rows of
Pascal’s Triangle using nested for loops.
pascals_triangle(5) '''
a=[]
for i in range(5):
    r=[1]*(i+1)
    for j in range(1,i):
        r[j]=a[i-1][j-1]+a[i-1][j]
    a.append(r)  
w=len(" ".join(map(str,a[-1])))
for r in a:
    r_str=" ".join(map(str,r))
    print(r_str.center(w))     