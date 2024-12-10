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
new_animal = input(f"შეიყვანეთ სიის მეორე ცხოველის ახალი სახელი: ")
favorite_animals[1] = new_animal
print("განახლებული სია:", favorite_animals)
