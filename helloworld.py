# Program to accept new user details and print the user details to the user.

username="null"
address="null"
phoneno="null"

# function to get new user details.

def new_user_reg(): 

    global  username
    global  address
    global phoneno
    
    print(f"\n NEW USER REGISTRATION")

    username=input("\n Please enter your name")

    address=input("\n Please enter your address")

    phoneno=input("\n Please enter your phoneno")

#function to display the user details to the user.
    
def display_user_reg():

    print("\n USER DETAILS : ")

    print(username)

    print(address)

    print(phoneno)


def main():
    
    new_user_reg()
    display_user_reg()


main()
