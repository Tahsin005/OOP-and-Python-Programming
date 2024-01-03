# money = input('Give me some money : ')
# print("Here is your money :",money)

first_money = input('Rean taka de: ')
second_money = input('Aziz taka de: ')

# By default the input from the user will be in string type:
print(type(first_money))
print(type(second_money))
print("Rean taka dise :",first_money,"Aziz taka dise :",second_money)
text = f"Rean taka dise : {first_money} Aziz taka dise : {second_money}"
print(text)
first_money_int = int(first_money)
second_money_int = int(second_money)
# total = (int)(first_money) + (int)(second_money)
total = first_money_int + second_money_int
print("Data type of total variable : ",type(total))
print(total)

