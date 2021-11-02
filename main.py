def converter0_256 ():
    print("convert_one")

def converter_one(one_value):
    print("converter0_256")

def binary_hex():
    #user inputs
    print("binary_hex")
    print("This program will demonstrate Integer values 0-256, ")
    print("reperesented as Binary tables and Hexadecimal  ")
    print("")
    all_or_one = input("Convert Integer to HEX and Binary Y/N ?")
    Run_all = ""
    print(all_or_one)
    if all_or_one == "Y" or all_or_one == "y":
            print("you did " + all_or_one)
            converter_one(1)
            #call a function
    else:
            print("you did " + all_or_one)
            converter0_256()
            #call a function


binary_hex()