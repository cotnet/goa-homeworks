#1
items = [1,2,3,4,5,6,7,8,9,10]
index = int(input("შეიყვანეთ ინდექსი 0-9 "))
if 0 <= index < len(items):
    print(items)
else:
    print("ინდექსი არასწორია")

#2
names = ["giorgi" "nino" "mariami" "zurabi" "tea"]
name=input("თქვენი სახელი")
index=int(input("შეიყვანეთ ინდექსი 0-4"))

if 0 <= index < lan(names):
    names[index]=name 
    print("სიაში ცვლილება : [names]")
else:
    print("ინდექსი არასწორია.")
#3
#Mutable  მათი მონაცემები შეიძლება შეიცვალოს და განახლდეს.
#Immutable მათ არ შეუძლიათ ცვლილება, და ყოველი ცვლილება ახალ ობიექტს ქმნის.