#1
number = int(input("შეიყვანეთ რიცხვი: "))

if number // 2 == 0:

    print("even")

else:

    print("odd")

#2

for i in range(1, 51):

    if i // 2 == 0:

     print(i)

#3

numbers = [5, 8, 12, 3, 15, 20, 7, 18]

for number in numbers:

    if number > 10:

     print(number)

#4

numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

first = numbers[0]

last = numbers[-1]

difference = last-first

sum_values=first + last

product=first*last

print(difference)

print(sum_values)

print(product)
#5

index = int (input("შეიყვანეთ რიცხვი: "))

names = ["გიორგი", "ნინო", "მარიამი", "ზურაბი", "თეა"]

if 0 <= index < len(names):

     print(names[index])

else:

     print("იწდექსი არასწორია.")