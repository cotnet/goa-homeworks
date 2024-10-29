#1
#>
print(15>3)
print(199999>131010140)
print(128>213)
#<=
print(9391<=8014)
print(2180<=830147)
print(9317465<=7654839201)
#>=
print(132574>=132574)
print(12684>=1665)
print(1>=134)
print(14>=13425)
#==
name="cotne"
print(name=="cotne")
age=19
print(age==87)
name1="achi"
print(name1=="luka")
#2
number=input("your favorite number :")
number1=7
print(int(number)==number1)
#3
print(True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5 )
#ჯერ 5 > 3 შემოწმდება, რაც True-ა.ახლა გვაქვს False and True – ეს ნაწილიც False-ად რჩება (რადგან and-ისთვის ერთი False საკმარისია).შემდეგ გვაქვს "name" == "name", რაც True-ა, მაგრამ 123 == "123" False-ია, ამიტომ ეს ნაწილი მთლიანად False იქნება.ასე რომ, მთლიანობაში დარჩა: True or False or False.or-ისთვის საკმარისია ერთი True, ამიტომ შედეგი იქნება True.
#4
age1=input("your age:")
surname1=input("your surname:")
mysurname="tevdorashvili"
print(int(age1)>=18 and surname1==mysurname)
#5
#ალგორითმი არის ნაბიჯების თანმიმდევრობა დავალების შესასრულებლად 3 მაგალითი 1) რეცეფტით კერძის მომზადება 2)დღის გეგმა 3)სუპერმარკეტის სია
#6
#flowchart-ი არის ფოტოთი ალგორითმის გამოსახვა pseudocode-ნატურალური და პროგრამირების ენის შერევა
#7
#control flow ის ტექნიკები sequences-კოდის გაშვება თანმიმდევრობით iterations-კოდის გამეორება selections-არჩევანის უფლება
#8
number2=int(input("first number="))
number3=int(input("second number="))
number4=int(input("thrid number="))
number5=int(input("fourth number="))
number6=int(input("fifth number="))
number7=(number2+number3+number4+number5+number6)
Arithmeticmean=(number7/5)
print(Arithmeticmean<number2*number6)




