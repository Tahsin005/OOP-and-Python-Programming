marks = int(input())
if marks >= 81 and marks <= 100:
    print("Very Good")
elif marks >= 61 and marks <= 80:
    print("Good")
elif marks >= 41 and marks <= 60:
    print("Average")
elif marks <= 40:
    print("Fail")