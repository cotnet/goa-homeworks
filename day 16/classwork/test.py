#1
name = input("Enter your name: ")
change_type = input("How do you want to change your name? (lower/upper/capitalize): ")
if change_type == "upper":
    print(name.upper())  
elif change_type == "lower":
    print(name.lower())  
elif change_type == "capitalize":
    print(name.capitalize())  
else:
    print("Invalid option")
#2

last_name = input("Enter your last name: ")
if "shvili" in last_name:
    print("როგორ ხარ?")
elif "ia" in last_name:
    print("მუჭო რექ?")
else:
    print("Bye")
#3

names_list = []
user_name = input("Enter a name: ")
if user_name.startswith('d') and user_name.endswith('i'):
    names_list.append(user_name)
    print("Name added to the list:", names_list)
else:
    print("invalid")
#4
elements = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = int(input("Enter an index (0-9): "))
if 0 <= index < len(elements):
    print("Element at index", index, "is:", elements[index])
else:
    print("Invalid index")
print("Updated list:", elements)
#5
foods = ["Pizza", "Burger", "Pasta", "Sushi", "Salad"]
index = int(input("Enter an index (0-4): "))
favorite_food = input("Enter your favorite food: ")
if 0 <= index < len(foods):
    foods.insert(index, favorite_food)
    print("Updated list:", foods)
else:
    print("Invalid index")


