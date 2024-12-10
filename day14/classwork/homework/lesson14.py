#1
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
first_day = week_days[0]
last_day = week_days[-1]
week_days[2] = "Midweek"
print("პირველი დღე:", first_day)
print("ბოლო დღე:", last_day)
print("განახლებული სია:", week_days)
#2

favorite_animals = []
for i in range(5):
    animal = input("შეიყვანეთ თქვენი საყვარელი ცხოველი : ")
    favorite_animals.append(animal)
print("პირველი ცხოველი:", favorite_animals[0])
print("ბოლო ცხოველი:", favorite_animals[-1])
new_animal = input("შეიყვანეთ სიის მეორე ცხოველის ახალი სახელი: ")
favorite_animals[1] = new_animal
print("განახლებული სია:", favorite_animals)
#3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
every_third = numbers[2::3]
reversed_list = numbers[::-1]
middle_six = numbers[3:9]
print("ყოველი მესამე ელემენტი:", every_third)
print("სია უკუღმა:", reversed_list)
print("შუა 6 ელემენტი:", middle_six)
#4

numbers = [x for x in range(1000, 10001) if x // 500 == 0]
first_five = numbers[:5]
every_third = numbers[::3]
count_elements = len(numbers)
print("პირველი ხუთი რიცხვი:", first_five)
print("ყოველი მესამე რიცხვი:", every_third)
print("საბოლოო სიის ელემენტების რაოდენობა:", count_elements)
#5

user_input = input("შეიყვანეთ 10 რიცხვი მძიმით გამოყოფილად: ")
numbers = [int(x.strip()) for x in user_input.split(",")]
first_three = numbers[:3]
middle_four = numbers[3:7]
is_last_ten = numbers[-1] == 10
print("პირველი სამი რიცხვი:", first_three)
print("შუა ოთხი ელემენტი:", middle_four)
print("სიის ბოლო ელემენტი არის 10:", is_last_ten)



