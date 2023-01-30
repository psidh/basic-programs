temp = int(input("Enter the external temperatire: "))
rain = input("Enter if its raining or not (True/False) : ")

if (temp <= 30 and rain == "False"):
  print("You can go for outting. Hurray !")
elif (temp >=30):
  print("The temperature is greater than 30 , so its hot out there")
elif (rain == True):
  print("It is raining outside so you cannnot go oustide.")
else:
  print("OOps you cannot go out  today!")
