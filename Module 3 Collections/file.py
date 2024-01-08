# . csv comma separated value
# .txt text file

# with open('message.txt', 'w') as file:
#     file.write('Hello, i am tahsin')
#     file.write('i am a competitive programmer')
# with open('message.txt', 'a') as file:
#     file.write('Hello, i am tahsin')
#     file.write('i am a competitive programmer')
with open('message.txt', 'r') as file:
    text = file.read()
    print(text)