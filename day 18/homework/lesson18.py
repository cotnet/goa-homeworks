#1
def multiply_numbers(a, b):
    result = a * b  
    return result   
number1 = 6 
number2 = 7  
product = multiply_numbers(number1, number2)  
print(product) 
#2
def check_even_or_odd(number):
   
    if number % 2 == 0:  
        return "ლუწია"
    else:
        return "კენტია"  
number1 = 12  
result1 = check_even_or_odd(number1) 
print(result1)
#3
def your_name(name):
    result="hello "+ name
    return result
name1="cotne"
names= your_name(name1)
print(names)

name2="nino"
names2=your_name(name2)
print(names2)
#4
def number_1(a,b):
    result=str(a)+str(b)
    return result

numbers1=13
numbers2=14
number4=number_1(numbers2,numbers1)
print(number4)
