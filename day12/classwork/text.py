#1

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = int(input("შეიყვანეთ ინდექსი (0-9): "))

if 0 <= index < len(items):
    print(items)
else:
    print("ინდექსი არასწორია.")
