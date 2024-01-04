numbers = [12, 45, 98, 68]
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)

print(even)

even_nums = [num for num in numbers if num % 2 == 0 and num % 4 == 0]
print(even_nums)

players = ['sakib', 'mushfik', 'mustafiz']
ages = [38, 37, 32]
age_comb = []
for player in players:
    print('Player:', player)
    for age in ages:
        print(player, age)
        age_comb.append([player,age])

print(age_comb)
age_comb2 = [[player,age] for player in players for age in ages]
print(age_comb2) 
