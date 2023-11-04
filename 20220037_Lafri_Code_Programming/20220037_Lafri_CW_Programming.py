import time
drivers_list = [["Sam",27,"Mitsubishi Motorsports","Mitsubishi Lancer",5],["Jhonny",32,"Suzuki Motorsports","Suzuki Swift",10],["Steve",23,"Subaru Motorsports","Subaru WRX STi",7]]
date=2
file_opening = open("Random_Race_Table.txt","r")
print("\n")
print ("File name : ", file_opening.name)
print(file_opening.read())

def display_menu():
    print("\n\t \t \t \t \tWORLD RALLY ROSS CHAMPIONSHIP \n\n\tManagement Application console MENU \n\nType ADD for adding driver details \nType DDD for deleting \nType UDD for updating driver details \nType VCT for viewing the rally cross standings table  \nType SRR for simulating a random race \nType VRL for viewing race table sorted according to the date \nType STF to save the current data to a text file \nType RFF to load data from the saved text file \nType ESC to exit the program.")
    # Printing the whole menu using \t and \n. \t to the tabspace and \n to the next line

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def add_driver_details(): #ADD
    global add_list
    add_list = [] #to create a sub list
    add_name = input("\nEnter driver's name: ")
    find_name = False  # initially assumes there is no driver with the same name
    for check in range(0, len(drivers_list)):
        if (drivers_list[check][0] == add_name):  # to check the name is already there or not
            head = ["Name  ", "Age   ", "Team  ", "Car   ", "Points"]
            print("\n", head[0], "-", drivers_list[check][0], "\n", head[1], "-", drivers_list[check][1], "\n", head[2], "-", drivers_list[check][2], "\n", head[3], "-", drivers_list[check][3], "\n", head[4], "-", drivers_list[check][4])
            print("Name already Exists! Check the details and Please enter another name or try again with initials!")
            find_name = True # after find the driver with the same name
            add_driver_details()

    if find_name == False:
        add_list.append(add_name)

        while True:  # For loop until enter the correct value
            add_age = input("Enter driver's age: ")
            try:
                add_age = int(add_age)
                assert add_age > 0
                break
            except:
                print("You can only Input a positive Number for Age. TRY AGAIN ! ")
        add_list.append(add_age)

        add_team = input("Enter driver's team: ")
        add_list.append(add_team)
        add_car = input("Enter driver's car: ")
        add_list.append(add_car)

        while True:
            add_points = input("Enter driver's points: ")
            try:
                add_points = int(add_points)
                assert add_points >= 0
                break
            except:
                print("You can only Input a positive Number for Points. TRY AGAIN ! ")
        add_list.append(add_points)  # to add details in one list
        drivers_list.append(add_list)  # to put all sub list in the main list
        print("\nDriver Successfully Added")

        choose_option()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_driver_details(): #DDD
    try:
        del_driver = input("Enter driver's name to delete : ")  # to search the name
        for add_list in drivers_list:
            assert add_list[0] != del_driver  # if this is true except doesn't work

    except:  # this will run when try fails to  run
        index = drivers_list.index(add_list)  # to find the list where the searched name placed
        drivers_list.pop(index)  # to delete the searched name
        print("\nDriver deleted successfully")

    else:  # if try fails to run else won't run
        print("The name you entered does not exists, Try Again!")
        delete_driver_details()

    choose_option()



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_driver_details(): #UDD
    lenth = len(drivers_list)
    upd_detail = input("Enter driver's old name to update : ")
    for check in range(0, lenth):  # checks the name is there or not
        if drivers_list[check][0] == upd_detail:
            print(drivers_list[check])
            print("\nSelect an option to update")
            print("Type 'N' for Name")
            print("Type 'A' for Age")
            print("Type 'T' for Team")
            print("Type 'C' for Car")
            print("Type 'P' for Points")
            up_option = input(
                "Enter your option to update what you need : ")  # select the option to change the option you wanted
            if up_option == "N" or up_option == "n":
                try:
                    upd_name = input("Enter driver's new name: ")
                    for add_list in drivers_list:
                        assert add_list[0] != upd_name  # if this is true except doesn't work
                except:
                    print("Name already in use! please enter another name!")


                else:
                    drivers_list[check][0] = upd_name
                    print("\nDriver Name Successfully updated")
                    print(drivers_list[check])
                    break
            elif up_option == "A" or up_option == "a":
                while True:
                    upd_age = input("Enter driver's age: ")
                    try:
                        upd_age = int(upd_age)
                        assert upd_age > 0
                        break
                    except:
                        print("You can only Input a positive Number for Age. TRY AGAIN ! ")

                drivers_list[check][1] = upd_age
                print("\nDriver Age Successfully updated")
                print(drivers_list[check])
                break
            elif up_option == "T" or up_option == "t":
                upd_team = str(input("Enter driver's team: "))
                drivers_list[check][2] = upd_team
                print("\nDriver Team Successfully updated")
                print(drivers_list[check])
                break
            elif up_option == "C" or up_option == "c":
                upd_car = str(input("Enter driver's car: "))
                drivers_list[check][3] = upd_car
                print("\nDriver Car Successfully updated")
                print(drivers_list[check])
                break
            elif up_option == "P" or up_option == "p":
                while True:
                    upd_points = input("Enter driver's Points: ")
                    try:
                        upd_points = int(upd_points)
                        assert upd_points >= 0
                        break
                    except:
                        print("You can only Input a positive Number for Age. TRY AGAIN ! ")

                drivers_list[check][4] = upd_points
                print("\nDriver Points Successfully updated")
                print(drivers_list[check])
                break
            else:
                print("Invalid Input")
    else:
        print("Try again by searching the old name")
        update_driver_details()

    choose_option()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def sort(drivers_list): #VCT
    lenth=len(drivers_list)
    for loop1 in range(0,lenth):# loops the checking process again
        for loop2 in range(0,lenth-loop1-1):# check and will make few lists in the descending order
            if drivers_list[loop2][4]<drivers_list[loop2+1][4] :#check the highest point
                temp=drivers_list[loop2]# assigning the list to temp
                drivers_list[loop2]=drivers_list[loop2+1]
                drivers_list[loop2+1]=temp # swaps the list to each other's place
    return drivers_list
# Referred from - https://linuxhint.com/sort-nested-list-python/
# THE AUTHOR - Kalsoom Bibi

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def random_race(): #SRR
    import random
    global date
    gap = ' ' * 3
    under_line = '=' * 110
    location = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]
    race_table = open("Random_Race_Table.txt", "a+")   #"a+"- For appending and reading. The file pointer is at EOF if the file exists. If the file does not exist, it creates a new file for reading and writing. , .txt file format
    race_table.write("\n") # .write writes the program to the txt file
    race_table.write("\n")
    race_table.write("\t\t\tLocation : ")
    race_table.write(location[random.randint(0, 5)])
    race_table.write(" \t\t\tRace on : 2022 MAY ")
    race_table.write(str(date))
    date = date + 1
    lenth = len(drivers_list)
    random.shuffle(drivers_list)
    x = f"{'Position':5s}{gap}{'Name':30s}{gap}{'Points':5s}"
    race_table.write("\n")
    race_table.write(x)
    race_table.write("\n")
    race_table.write(under_line)
    race_table.write("\n")
    for position in range(1, lenth + 1):
        if position == 1:
            position1 = f"{str(position):8s}{gap}{str(drivers_list[0][0]):30s}{gap}{str(10):5s}"
            race_table.write("\n")
            race_table.write(position1)
            race_table.write("\n")
            drivers_list[0][4] = drivers_list[0][4] + 10 # add the points(int) to the list
        elif position == 2:
            position2 = f"{str(position):8s}{gap}{str(drivers_list[1][0]):30s}{gap}{str(7):5s}"
            race_table.write("\n")
            race_table.write(position2)
            race_table.write("\n")
            drivers_list[1][4] = drivers_list[1][4] + 7
        elif position == 3:
            position3 = f"{str(position):8s}{gap}{str(drivers_list[2][0]):30s}{gap}{str(5):5s}"
            race_table.write("\n")
            race_table.write(position3)
            race_table.write("\n")
            drivers_list[2][4] = drivers_list[2][4] + 5
        else:
            position_x = f"{str(position):8s}{gap}{str(drivers_list[position-1][0]):30s}{gap}{str(0):5s}"
            race_table.write("\n")
            race_table.write(position_x)
            race_table.write("\n")
            drivers_list[position - 1][4] = drivers_list[position - 1][4] + 0
    race_table.close()


# for table Referred from https://youtu.be/fsBslGyCeYI
# for file handling https://www.w3schools.com/python/python_file_handling.asp
# for shuffle https://www.w3schools.com/python/ref_random_shuffle.asp

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def driver_data(): #STF
    lenth = len(drivers_list)
    gap = ' ' * 3
    under_line = '=' * 110
    drivers_tabel = open("Drivers_Table.txt", "a+")
    header = f"{'Name':30s}{gap}{'Age':5s}{gap}{'Team':30s}{gap}{'Car':20s}{gap}{'Points':5s}"
    drivers_tabel.write(under_line)
    drivers_tabel.write("\n")
    drivers_tabel.write(header)
    drivers_tabel.write("\n")
    drivers_tabel.write(under_line)
    drivers_tabel.write("\n")
    for list_index in range(0, lenth):
        driver = f"{drivers_list[list_index][0]:30s}{gap}{str(drivers_list[list_index][1]):5s}{gap}{drivers_list[list_index][2]:30s}{gap}{drivers_list[list_index][3]:20s}{gap}{str(drivers_list[list_index][4]):5s}"
        drivers_tabel.write("\n")
        drivers_tabel.write(driver)
        drivers_tabel.write("\n")
# this is for STF and RFF as well

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def choose_option():

    option=input("\nType the required option from the menu to access it : ")  #To get the input
    if option == "ADD" or option == "add" or option == "Add":
        add_driver_details()

    elif option == "DDD" or option == "ddd" or option == "Ddd":
        delete_driver_details()

    elif option == "UDD" or option == "udd" or option == "Udd":
        update_driver_details()

    elif option == "VCT" or option == "vct" or option == "Vct":
        sort(drivers_list)
        from tabulate import tabulate
        head = ["Name", "Age", "Team", "Car", "Points"]
        print(tabulate(drivers_list, headers=head, tablefmt="fancy_grid"))

        choose_option()

    elif option == "SRR" or option == "srr" or option == "Srr":
        if date < 32:
            print("Race Completed")
            random_race()
            choose_option()

    elif option == "VRL" or option == "vrl" or option == "Vrl":
        file_opening = open("Random_Race_Table.txt", "r")
        print("File name : ", file_opening.name)
        print(file_opening.read())
        choose_option()

    elif option == "STF" or option == "stf" or option == "Stf":
        print("Data is saved")
        driver_data()

        choose_option()
    elif option == "RFF" or option == "rff" or option == "Rff":
        print("Driver Details")
        drivers_tabel = open("Drivers_Table.txt", "r")
        print("File name : ", drivers_tabel.name)
        print(drivers_tabel.read())
        print("If you want to Edit the file go to option and USE ADD or DDD or UDD and save data using STF")
        
        choose_option()
    elif option == "ESC" or option == "esc" or option == "Esc":
        print("Thank you using our Management Application")
        time.sleep(2)
        quit()
    else:
        print("INVALID OPTION!! Try Again! ")
        choose_option() # For looping the Whole Program

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

display_menu()
choose_option()