# #1
# # append(): ამატებს ახალ ელემენტს სიის ბოლოში.
# # არგუმენტები: 1 არგუმენტი - ელემენტი, რომელიც უნდა დაემატოს სიას.
# # მაგალითი:
# # fruits = ['apple', 'banana']
# # fruits.append('cherry')
# # შედეგი: ['apple', 'banana', 'cherry']

# # insert(): სიის კონკრეტულ ინდექსზე ამატებს ახალ ელემენტს.
# # არგუმენტები: 2 არგუმენტი -
# # 1. ინდექსი, სადაც ელემენტი უნდა ჩაისვას.
# # 2. ელემენტი, რომელიც უნდა ჩაისვას.
# # მაგალითი:
# numbers = [1, 2, 4]
# numbers.insert(2, 3)
# # შედეგი: [1, 2, 3, 4]

# # pop(): შლის და აბრუნებს სიის ელემენტს მისი ინდექსით.
# # არგუმენტები: 1 არასავალდებულო არგუმენტი - ინდექსი, რომლის მიხედვითაც ელემენტი წაიშლება.
# # თუ ინდექსი არ არის მითითებული, შლის და აბრუნებს ბოლო ელემენტს.
# # მაგალითი:
# letters = ['a', 'b', 'c']
# removed = letters.pop(1)
# # შედეგი: ['a', 'c'], removed = 'b'

# # len(): ითვლის ობიექტის (მაგალითად, სიის ან სტრიქონის) ელემენტების რაოდენობას.
# # არგუმენტები: 1 არგუმენტი - ობიექტი, რომლის სიგრძეც უნდა დაითვალოს.
# # მაგალითი:
# words = ['hello', 'world']
# length = len(words)
# # შედეგი: length = 2

# # upper(): სტრიქონის ყველა სიმბოლოს დიდ ასოებად გარდაქმნა.
# # არგუმენტები: არგუმენტები არ სჭირდება.
# # მაგალითი:
# text = "hello"
# uppercase_text = text.upper()
# # შედეგი: 'HELLO'

# # lower(): სტრიქონის ყველა სიმბოლოს პატარა ასოებად გარდაქმნა.
# # არგუმენტები: არგუმენტები არ სჭირდება.
# # მაგალითი:
# text = "HELLO"
# lowercase_text = text.lower()
# # შედეგი: 'hello'

# # capitalize(): სტრიქონის პირველი სიმბოლოს დიდ ასოდ გარდაქმნა, დანარჩენების კი პატარა ასოებად.
# # არგუმენტები: არგუმენტები არ სჭირდება.
# # მაგალითი:
# text = "python is fun"
# capitalized_text = text.capitalize()
# # შედეგი: 'Python is fun'

# # find(): სტრიქონში ქვეწერის (substring) პირველი გამოჩენის ინდექსის პოვნა.
# # არგუმენტები: 
# # 1. ქვეწერი, რომლის პოვნა გსურთ.
# # 2. (არასავალდებულო) საწყისი ინდექსი, საიდანაც ძებნა დაიწყება.
# # 3. (არასავალდებულო) ბოლო ინდექსი, სადაც ძებნა უნდა შეწყდეს.
# # მაგალითი:
# text = "hello world"
# index = text.find("world")
# # შედეგი: index = 6
# # შენიშვნა: თუ ქვეწერი არ მოიძებნა, find() აბრუნებს -1-ს.

#2
last_name=["berize,tevdorashvili,cigriashvili,jmuxaze,javaxishvili"]
name=(input("თქვენი სახელი:"))
if len(name)>7:
    last_name.append(name)
    print("თქვენი სახელი დამატდა")
else:
    print("თქვენი სახელი ვერ დამატდა")
print(last_name)
#3

elements = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
even_index_elements = []  

for i in range(len(elements)):  
    if i % 2 == 0:  
        even_index_elements.append(elements[i])
print("ლუწ ინდექსზე მდგომი ელემენტები:", even_index_elements)

#4    
frut=("apple")  
fruts=len(frut)
print(fruts)
#5
name1=(input("your name capital letters"))
name2=name1.lower()
print(name2)
#6 
last_name1=("tevdorashvili")
last_name2=last_name1.upper()
print(last_name2)
#7
animal=("dog")
animal1=animal.capitalize()
print(animal1)

