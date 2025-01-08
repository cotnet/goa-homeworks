# 1)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


print("First day:", weekdays[0])  
print("Last day:", weekdays[-1])  

weekdays[2] = "Midweek"
print("Updated list:", weekdays)

# 2)
favorite_animals = []


for i in range(5):
    animal = input(f"Enter favorite animal {i+1}: ")
    favorite_animals.append(animal)

print("First animal:", favorite_animals[0])
print("Last animal:", favorite_animals[-1])


new_animal = input("Enter a new second animal: ")
favorite_animals[1] = new_animal
print("Updated list of animals:", favorite_animals)

# 3)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


every_third = numbers[2::3]
print("Every third element:", every_third)


reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)


middle_six = numbers[3:9]
print("Middle six elements:", middle_six)

# 4) 
divisible_by_500 = list(range(1000, 10001, 500))


first_five = divisible_by_500[:5]
print("First five numbers:", first_five)

every_third_number = divisible_by_500[::3]
print("Every third number:", every_third_number)

count_numbers = len(divisible_by_500)
print("Total numbers count:", count_numbers)

# 5) 
user_input = input("Enter 10 numbers separated by commas: ")
user_numbers = [int(x) for x in user_input.split(",")]


print("First three numbers:", user_numbers[:3])


middle_four = user_numbers[3:7]
print("Middle four numbers:", middle_four)


if user_numbers[-1] == 10:
    print("The last number is 10.")
else:
    print("The last number is not 10.")