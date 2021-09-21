from prettytable import PrettyTable
import random
import time
import datetime

file = open("vehicle_management_system.txt", "a")

vehicle_ms = PrettyTable()
vehicle_ms.field_names = ["Vehicle ID", "Vehicle Brand", "Vehicle Model", "Vehicle Reg",
                          "Vehicle Colour", "Vehicle Price", "Added date"]


# login to management system ---------------

def login():
    print("\nLogin to Vehicle Management System")
    attempt = 4
    while attempt >= 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if (username == "Admin") and (password == "Admin"):
            time.sleep(1)
            print("Login Successful")
            time.sleep(1)
            main()
            break

        elif (username != "Admin") or (password != "Admin"):
            print(f"Incorrect username or password. {attempt} left!")
            attempt -= 1


# main menu ---------------

def main():
    print("\nWelcome to Vehicle Management System")
    while True:
        try:
            print()
            choice = int(input("Press key:\n" +
                               "1. View Vehicle\n" +
                               "2. Add Vehicle\n" +
                               "3. Search Vehicle\n" +
                               "4. Save and Exit Database\n"))

            if choice == 1:
                view()

            elif choice == 2:
                add()

            elif choice == 3:
                search_v()

            elif choice == 4:
                exit_ms()

            elif choice != 1 or 2 or 3 or 4:
                print("Select again")
        except ValueError:
            print("Incorrect Value")


# add vehicle to system  ---------------

def add():
    print("\nAdd vehicle to Database")
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    plate = input("Enter vehicle registration plate: ")
    colour = input("Enter vehicle colour: ")

    # input cost of vehicle
    cost = float(input("Enter vehicle cost (no commas): "))
    # formats cost to 2 decimal places
    veh_cost = '{0:.2f}'.format(cost)

    # adds date of now
    d = datetime.datetime.now()
    date = d.strftime("%x")

    # random generator to generate id and combine with first index of brand and model
    gen = random.randint(1, 999999)
    v_id = brand[0] + model[0] + str(gen)

    print()
    time.sleep(1)
    print("Vehicle added successfully")
    vehicle_ms.add_row([f"{v_id.upper()}", f"{brand.upper()}", f"{model.upper()}",
                        f"{plate.upper()}", f"{colour.upper()}", f"{veh_cost}", f"{date}"])


# view database  ---------------

def view():
    print("\nVehicle Database")
    print(vehicle_ms)


# search vehicle ---------------

def search_v():
    print("\nSearch vehicle")
    search = input("Enter vehicle reg: ")
    vehicle_ms.get_string(fields=["Vehicle Reg"])

    # search for vehicle reg through this field "vehicle reg"
    if search.upper() in vehicle_ms.get_string(fields=["Vehicle Reg"]):
        print("Vehicle exits")
    else:
        print("Vehicle does not exist")


# exit management system ---------------

def exit_ms():
    print("Saving Progress")

    # writing data inputted by user in add() function into text file
    file.write(str(vehicle_ms))
    file.write("\n")
    file.write("\n")
    # closing text file
    file.close()

    time.sleep(2)
    print("Goodbye")
    time.sleep(1)
    exit()


login()
