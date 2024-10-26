import poplib

user_value = int(input("What is the number you are thinking of? "))

value_list = []

def list_sort():
    value_list.append(user_value)
    print("The number " + str(user_value) + " has been added to the list")
    print(value_list)

def optional_options():
    optional_command = input("Do you want to do something with this? (Yes/No) ")
    if optional_command.lower() == "yes":
        print("options: \n 1) Take out the most recent number \n 2) copy and paste the most recent number \n 3) add another number \n 4) extend your current list")
        user_choice = input(" ")
        if user_choice == "1":
            value_list.pop()
            print("Here is the new list: " + str(value_list))
        elif user_choice == "2": 
            value_list.append(user_value)
            print("Here is the new list: " + str(value_list))
        elif user_choice == "3":
            new_number = int(input("Whats the new number? "))
            value_list.append(new_number)
            print("Here is the new list: " + str(value_list))
        elif user_choice == "4":
            new_length = int(input("How much do you want to extend it by? "))
            value_list.extend(value_list*new_length)
            print("Here is the new list: " + str(value_list))
        else:
            print("Haha what the heck are you adding")
    else:
        print("well too bad the final list is " + str(value_list))

def optional_options_after():
    optional_command = "yes"
    if optional_command.lower() == "yes":
        print("options: \n 1) Take out the most recent number \n 2) copy and paste the most recent number \n 3) add another number \n 4) extend your current list")
        user_choice = input(" ")
        if user_choice == "1":
            value_list.pop()
            print("Here is the new list: " + str(value_list))
        elif user_choice == "2": 
            value_list.append(user_value)
            print("Here is the new list: " + str(value_list))
        elif user_choice == "3":
            new_number = int(input("Whats the new number? "))
            value_list.append(new_number)
            print("Here is the new list: " + str(value_list))
        elif user_choice == "4":
            new_length = int(input("How much do you want to extend it by? "))
            value_list.extend(value_list*new_length)
            print("Here is the new list: " + str(value_list))
        else:
            print("Haha what the heck are you adding")
    else:
        print("well too bad the final list is " + str(value_list))
    optional_command = input("Do you want to do another thing? ")

list_sort()
optional_options()

retry_again = input("do you want to do more? ")

if retry_again.lower() == "yes":
    while retry_again.lower() == "yes":
        optional_options_after()



