balance = 3000

def buy_things(item, price):
    """You can access global variable without the global keyword"""
    global balance
    print(f"Balance before buying {item}", balance)
    # if you want to modify a global variable, you have to use the global keyword
    balance -= price 
    print(f"Balance after buying {item}", balance)

buy_things("sunglass", 1000)