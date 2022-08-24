# from exchange_rates_data import data
#
# print(data)
import pandas as pd
from tkinter import *
from Untitled import country_name

window = Tk()
window.title("Currency Converter")
window.minsize(width=900, height=600)
window.config(padx=50, pady=10)


label1 = Label(text="COUNTRIES", font=("Arial", 10, "bold"))
label1.grid(row=0, column=0)
country = Label(text=country_name, font=("Arial", 7, "bold"))
country.grid(row=1, column=0)


label2 = Label(text="FROM\n(serial number)", font=("Arial", 20, "bold"))
label2.place(x=200, y=250)
#
label3 = Label(text="TO\n(serial number)", font=("Arial", 20, "bold"))
label3.place(x=500, y=250)












# # ------------------------------FROM------------------------------------------
# label_from = Label(text="FROM", font=("Arial", 25, "bold"))
# label_from.grid(row=0, column=0)
#
# choice_from = None
#
#
# def listbox_used_from(event):
#     # Gets current selection from listbox
#     global choice_from
#     choice_from = listbox_from.get(listbox_from.curselection())
#     # print("45852")
#
#
# listbox_from = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox_from.insert(fruits.index(item), item)
# listbox_from.bind("<<ListboxSelect>>", listbox_used_from)
# listbox_from.grid(row=1, column=0)
#
# label = Label(text="text", font=("Arial", 22, "bold"))
# label.grid(row=0, column=2)
# # -------------------------------TO---------------------------
#
# label_from = Label(text="TO", font=("Arial", 25, "bold"))
# label_from.grid(row=0, column=4)
#
# choice_to = None
#
#
# def listbox_used_to(event):
#     # Gets current selection from listbox
#     global choice_to
#     choice_to = listbox_to.get(listbox_to.curselection())
#
#
# listbox_to = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox_to.insert(fruits.index(item), item)
# listbox_to.bind("<<ListboxSelect>>", listbox_used_to)
# listbox_to.grid(row=1, column=4)

# -------------------------------------------------------------


window.mainloop()
