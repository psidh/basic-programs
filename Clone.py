# import keyboard
import csv
import itertools
import threading
import time
import sys
import time

# import tkinter

print("Welcome To Clone!")



def choice_after_login():

    prompt = input("Share your day's experience with other ! \nChoose What you want to post TYPE EXIT to exit.\n").lower()
    print(" TEXT \n FOLLOWERS \n FOLLOWING \n POSTS")

    if prompt == "text":
        text_input = input("                          Type your thoughts: \n                     ")


        curr = time.time()
        curr2 = time.ctime(curr)

        done = False

        # here is the animation
        # ________________________________________________________________
        def animate():
            for c in itertools.cycle(['.', ' ..', '.. .', '.  ..', ' .']):
                if done:
                    break
                sys.stdout.write('\rloading ' + c)
                sys.stdout.flush()
                time.sleep(0.08)

        t = threading.Thread(target=animate)
        t.start()

        # long process here
        time.sleep(5)
        done = True

        #CSV STARTS FROM THE BELOW

        with open("data.txt", mode="a") as file:
            file.writelines(text_input)


        # ________________________________________________________________
        choice_after_login()

    elif (prompt == "followers"):
        pass


    elif prompt == "exit":

        print(">>> Thank you !")
    else:
        print("Looks like you've typed something else! Try again")
        choice_after_login()
# _________________________________________________________________
dict = {"philkhanasidharth14@gmail.com": "broforcebeta1@123#",
            "philkhana30@gmail.com": "Vzm@123#",
            }
# _________________________________________________________________

def checkKeyUP(email_, password):
    if email_ in dict.keys():
        print("You already have an account with this email\n Please login to your account")
        choice_after_login()
    else:
        dict[email_] = password
        choice_after_login()

def checkKeyIN(email_, password):
    if (email_, password) in dict:
        print("Login Successful")
        choice_after_login()
    else:
        print("Login Error , either your email or password or both are incorrect!!!")
        credentials()
# _________________________________________________________________

def credentials():
    global_user_data = []


    print("SignIn or SignUp")

    login_choice = input("").lower()
    if login_choice == "signup":

        email_ = input("Enter your Email Id: ").lower()
        password = input("Create a password: ")
        password2 = input("Confirm your password: ")

        checkKeyUP(email_, password)

        if password2 == password:
            dict[email_] = password
            choice_after_login()
        else:
            credentials()

    elif login_choice == "signin":

        email_ = input("Enter your Email Id: \n").lower()
        password = input("Enter your password: \n")

        checkKeyIN(email_, password)

    else:
        print("Login Error , either your email or password or both are incorrect!!!")
        credentials()

def signout():
    print("                                                        YOU HAVE SIGNED OUT \n")
    credentials()

def Clone():

    opening_of_app = input("                                   Do you want to Open Clone \n").lower()

    if opening_of_app == "yes":
       credentials()
    elif opening_of_app == "no":
        print("Thank You !")

    else: 
        print("Looks like you have typed something else, Try again")
        credentials()


Clone()



