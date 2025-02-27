#Ques 2:Explain how Python handles type conversion between different data
#types, such as between integers and floats or between strings and
#lists.

#Ans: Python provides two types of type conversion:
#1. Implicit Type Conversion: Python converts one data type to another.
#Example:
x = 5   
y = 2.5 
result = x + y  
print(result, type(result))  



#2.Explicit Type Conversion: When we manually converts a data type using built-in functions.
#Examples:
#1.Integer to Float:
a = 10
b = float(a)
print(b, type(b)) 

        
#2.Float to Integer
c = 3.7
d = int(c)  
print(d, type(d))

 
#3.String to Integer/Float:
num_str = "42"
num_int = int(num_str) 
num_float = float(num_str) 
print(num_int, type(num_int))
print(num_float, type(num_float))


#4.Integer/Float to String:
num = 100
str_num = str(num) 
print(str_num, type(str_num))


#5.String to List:
word = "hello"
char_list = list(word)  


#6.List to String:
char_list = ['h', 'e', 'l', 'l', 'o']
word = "".join(char_list)  
print(word)

#7.List to Tuple and Vice Versa:
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  
my_new_list = list(my_tuple) 
print(my_tuple)
print(my_new_list) 


#8.Dictionary to List/Tuple:
my_dict = {"a": 1, "b": 2}
keys_list = list(my_dict.keys())  
values_tuple = tuple(my_dict.values())
print(keys_list)
print(values_tuple)
