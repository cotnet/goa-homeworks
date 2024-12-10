#1

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
start = int(input("შეიყვანეთ პირველი რიცხვი დიაპაზონისთვის: "))
end = int(input("შეიყვანეთ მეორე რიცხვი დიაპაზონისთვის: "))
subset = my_list[start:end+1]
print("დიაპაზონში არსებული ელემენტები:", subset)
#2

small_list = ["apple", "banana", "cherry", "date", "elderberry"]
index = int(input("შეიყვანეთ ინდექსი (0-დან 4-მდე): "))
if 0 <= index < len(small_list):
    print("ამ ინდექსზე მდგომი ელემენტი არის:", small_list[index])
else:
    print("შეყვანილი ინდექსი არასწორია.")
#3

user_name = input("შეიყვანეთ თქვენი სახელი: ")
my_name = "ცოტნე"
result = user_name[:3] + my_name[-2:]
print("შედეგი:", result)
#4
# Indexing:Indexing გამოიყენება სიის ან სტრიქონის კონკრეტულ პოზიციაზე მდგომი ერთი ელემენტის ამოსაღებად.მაგ., my_list[2] იძლევა მესამე ელემენტს.

# Slicing:- Slicing საშუალებას გვაძლევს ამოვიღოთ ელემენტების დიაპაზონი სიის ან სტრიქონისგან.მაგ., my_list[2:5] იძლევა ელემენტებს მე-3-დან მე-5-მდე (3 ≤ i < 5).
#5

last_name = input("შეიყვანეთ თქვენი გვარი: ")

reversed_last_name = last_name[::-1]

print("თქვენი გვარი:", last_name)
print("შებრუნებული გვარი:", reversed_last_name)

