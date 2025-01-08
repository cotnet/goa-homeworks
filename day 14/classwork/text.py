# 1)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))


print("Selected elements:", my_list[start:end])

# 2)
my_list_5 = ['a', 'b', 'c', 'd', 'e']
index = int(input("Enter an index (0-4): "))

if 0 <= index < len(my_list_5):
    print("Element at the given index:", my_list_5[index])
else:
    print("Invalid index!")

# 3)
user_name = input("Enter your name: ")
my_name = "Giorgi"


combined_name = user_name[:3] + my_name[-2:]
print("Combined result:", combined_name)

# 4)
"""
Indexing (ინდექსაცია) - გამოიყენება სიის კონკრეტული ელემენტის ამოსაღებად, მაგალითად my_list[2] აბრუნებს მესამე ელემენტს.
Slicing (ნაწილი) - გამოიყენება სიის დიაპაზონის ამოსაღებად, მაგალითად my_list[1:4] აბრუნებს ელემენტებს მეორე, მესამე და მეოთხე პოზიციებიდან.
"""

# 5) 
user_surname = input("Enter your surname: ")

reversed_surname = user_surname[::-1]

print("Original surname:", user_surname)
print("Reversed surname:", reversed_surname)
