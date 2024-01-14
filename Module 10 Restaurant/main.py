from Menu import Pizza, Burger, Menu, Drinks
from Restaurant import Restaurant
from Users import Chef, Customer, Server, Manager
from Order import Order 
def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki Pizza', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alu Bhorta Pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'Beef', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_2)

    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks',  coke)
    coffee = Drinks('Mocha Coffee', 300, False)
    menu.add_menu_item('drinks', coffee)

    menu.show_menu()




    restaurant = Restaurant('Sai Baba Restaurant', 2000, menu)

    manager = Manager('Kala Chan', 5, 'Kala@chan.com', 'Kaliapur', 1500, 'Jan 1, 2020', 'core')

    restaurant.add_employee('manager', manager)

    chef = Chef('Rostom Baburchi', 6, 'kopa@rostom.com', 'rostomNagar', 3500, 'Feb 1, 2020', 'Chef', 'everthing')
    restaurant.add_employee('chef', chef)

    server = Server('Chotu', 6, 'nai@jai.com', 'restaurant', 2000, 'March 1, 2020', 'server')
    restaurant.add_employee('server', server)


    restaurant.show_employees()


    customer_1 = Customer('Sakib Khan', 6, 'King@khan.com', 'banani', 100000)

    order_1 = Order(customer_1, [pizza_3, coffee])

    customer_1.place_order(order_1)

    restaurant.add_order(order_1)


    restaurant.receive_payment(order_1, 2000, customer_1)

    print('Revenue and balance after first customer 1:',restaurant.revenue, restaurant.balance)

    customer_2 = Customer('Sakib AL Hasan', 6, 'King@khan.com', 'banani', 100000)

    order_2 = Order(customer_2, [pizza_1, pizza_1, coffee])

    customer_2.place_order(order_2)

    restaurant.add_order(order_2)


    restaurant.receive_payment(order_2, 2000, customer_2)

    print('Revenue and balance after first customer 2:',restaurant.revenue, restaurant.balance)


    # pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('After rent', restaurant.revenue, restaurant.balance, restaurant.expense)

    restaurant.pay_salary(chef)
    print('After salary', restaurant.revenue, restaurant.balance, restaurant.expense)

if __name__ == '__main__':
    main() 
