def full_name(first, last):
    name = f"Full name is : {first} {last}"
    return name

# takes parameters in order
# name = full_name("Alu", "Kodu")

name = full_name(last  = "Kodu", first = "Alu")
print(name)

# def famous_name(first, last, title, additional):
#     name = f"{title} {first} {last} {additional}"
#     return name
 
def famous_name(first, last, **additional):
    name = f"{first} {last} {additional}"
    # name = f"{first} {last}"
    print(additional)
    # print(additional["title"], additional["additional"])
    for key, value in additional.items():
        print(key, value)
    return name
name = famous_name(title= "Hujur", first= "hoiye", last= "hasho", additional="keno")
print(name)



""" Multiple return: """
def a_lot(n1, n2):
    sum = n1 + n2
    mult = n1 * n2
    rem = n1 - n2
    # return sum, mult, rem # will be returned as a tuple 
    return [sum, mult, rem] # will be returned as a list

everything = a_lot(5,3)
print(everything)
for i in range(len(everything)):
    print(everything[i], end = " ")