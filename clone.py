# import keyboard
import csv
import itertools
import threading
import time
import sys
import time

# import tkinter

print("Welcome To Clone!")

#___________________________AFTER LOGIN____________________________

def choice_after_login():
    print(" TEXT \n FOLLOWERS \n FOLLOWING \n POSTS")
    prompt = input("Share your day's experience with other ! \nChoose What you want to post TYPE EXIT to exit.\n").lower()
    
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



# ___________________DATABASE OF THE CLONE_________________________________________

dict = {"philkhanasidharth14@gmail.com": "broforcebeta1@123#",
            "philkhana30@gmail.com": "Vzm@123#",
            }

#________________START OF THE AUTHENTICATION_______________________________________

def credentials():
    global_user_data = []


    print("SignIn or SignUp")

    login_choice = input("").lower()
    

    #_____________________________________________________

    if login_choice == "signup":
    #_____________________________________________________
        
        email_ = input("Enter your Email Id: ").lower()
        password = input("Create a password: ")
        password2 = input("Confirm your password: ")


        if password == password2:
            dict[email_] = password
            dict.update({email_: password})
            print(dict)
            choice_after_login()
        else:
            credentials()

    #_____________________________________________________

    elif login_choice == "signin":
    #_____________________________________________________
        
        email_ = input("Enter your Email Id: \n").lower()
        password1 = input("Enter your password: \n")

        if dict[email_] == password1:
            print("Logged in Successfully")
            choice_after_login()
        else:
            credentials()

    else:

        print("Login Error , either your email or password or both are incorrect!!!")
        credentials()



#_______________SIGNED OUT___________________________________________________________

def signout():
    print("                                                        YOU HAVE SIGNED OUT \n")
    credentials()


#_______________THE OUTER MOST PART - UI______________________________________________

def Clone():

    opening_of_app = input("                                   Do you want to Open Clone \n").lower()

    if opening_of_app == "yes":
       credentials()
    elif opening_of_app == "no":
        print("Thank You !")

    else: 
        print("Looks like you have typed something else, Try again")
        Clone()

#________________START OF THE CODE____________________________________________________

Clone()



