class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall_obj):
        self.__hall_list.append(hall_obj)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_details = (id, movie_name, time)
        self.__show_list.append(show_details)
        seat = []
        for i in range(self.__rows):
            temp = []
            for j in range(self.__cols):
                temp.append(0)
            seat.append(temp)
        self.__seats[id] = seat

    def book_seats(self, id, seats):
        if id not in self.__seats:
            return f"There is no show with id '{id}'"
        for i in seats:
            if (i[0] < 0 or i[0] >= self.__rows) or (i[1] < 0 or i[1] >= self.__cols):
                return  f"{i} is not valid!"
            elif self.__seats[id][i[0]][i[1]] is True:
                return f"Seat {i} is already booked"
            else:
                self.__seats[id][i[0]][i[1]] = True
                return f"Seat successfully booked"
        
    def view_show_list(self):
        print("Shows List:")
        for i in self.__show_list:
            print(f"ID : {i[0]}, Show name : {i[1]}, Time and date : {i[2]}")
    
    def view_available_seats(self, id):
        print()
        if id not in self.__seats:
            print(f"There is no show with id '{id}'")
            return -1
        else:
            print(f"Available Seats for the show with ID: {id} :")
            for i, row in enumerate(self.__seats[id]):
                for j, col in enumerate(row):
                    if j == 0:
                        if col == 0:
                            print("[", "0,", end = " ")
                        else:
                            print("[", "1,", end = " ")
                    elif j == len(self.__seats[id]) - 1:
                        if col == 0:
                            print("0", "]", end = " ")
                        else:
                            print("1", "]", end = " ")
                    else:
                        if col == 0:
                            print("0,", end = " ")
                        else:
                            print("1,", end = " ")
                print()
            return 1
hall1 = Hall(10, 10, 1)

hall1.entry_show("111", "The Flash", "3 PM January, 11th, 2024")
hall1.entry_show("222", "The Big Bang Theory", "3 PM January, 12th, 2024")
hall1.entry_show("333", "Friends", "3 PM January, 13th, 2024")
hall1.entry_show("444", "Lost in space", "3 PM January, 14th, 2024")
hall1.entry_show("555", "Agent of SHIELD", "3 PM January, 15th, 2024")

while True:
    print(" Option: Description                ")
    print(" -----------------------------------------")
    print(" 1: View all running shows")
    print(" 2: View available seats in a show ")
    print(" 3: Book a ticket in a show")
    print(" 4: Exit")

    option = int(input("Enter the option : "))

    print()

    if option == 1:
        hall1.view_show_list()
    elif option == 2:
        id = input("Enter the show ID: ")
        hall1.view_available_seats(id)
    elif option == 3:
        id = input("Enter the show ID: ")
        isValid = hall1.view_available_seats(id)
        if isValid == -1:
            print("Try Again with a valid Show ID!")
        else:
            x = int(input("Enter the row no. of the seat (1 - 10) : "))
            y = int(input("Enter the column no. of the seat (1 - 10): "))
            x -= 1
            y -= 1
            seat_loaction = (x,y)
            text = hall1.book_seats(id, [seat_loaction])
            print(text)
    elif option == 4:
        break
    else:
        print(f"{option} is an invalid option")

    print()
