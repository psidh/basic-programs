from tkinter import *


def mile_to_km():
    miles = float(miles_input.get())
    km = round(miles *1.6)
    km_result_label.config(text= km)



window = Tk()
window.title("Mile to kilometre converter")
window.config(padx = 20  ,pady = 20)

window.mainloop()



miles_input = Entry(width=7)
miles_input.grid(column=1, row = 0)


# ++++++++++++++++++++++++++++++++++++

miles_label = Label(text = "miles")
miles_label.grid(column = 2 , row = 0)


is_equal_label = Label(text = "is equal to")
is_equal_label.grid(column = 0 , row = 1)

km_label = Label(text = "Km")
km_label.grid(column = 1 , row = 1)

km_result_label = Label(text = "0")
km_result_label.grid(column = 2 , row = 1)

calc_button = Button(text = "calculate", command = mile_to_km)
calc_button.grid(column = 1 , row = 2)

# +++++++++++++++++++++++++++++++++++++

