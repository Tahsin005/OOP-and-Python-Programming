""" Variables in Python """
age = 21
intest_rate = 2.5
name = "MD. Tahsin Ferdous"
district = 'Coxs Bazar'
is_single = True
is_studying = False
print(age)
print(intest_rate)
print(age * intest_rate)
print(name)
print(district)
print(is_single) 
print(is_studying)
print("\n")
print("Types of variable : ")
# This is a comment
""" This is a multiline comment 
that can be done using alt + shift + a"""
print(type(age)) 
print(type(intest_rate))
print(type(name))
print(type(is_single))

""" String concatenation """
# print('MD. Tahsin ' + 'Ferdous')
text = f"MD. Tahsin Ferdous {age}, who lives is {district}"
print(text)