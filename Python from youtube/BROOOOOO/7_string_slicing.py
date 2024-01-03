# slicing = create a substring by extracting elements from another string 
#     indexing[] or slice()
#     [start:stop:step]

'''indexing[]'''
name = "Tahsin Ferdous"
# first_name = name[0:6]
first_name = name[:6]
last_name = name[7:]
funcky_name = name[::2]

reversed_name = name[:: -1]
print(first_name)
print(last_name)
print(funcky_name)
print(reversed_name)

'''slice()'''
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)
print(website1[slice])
print(website2[slice])