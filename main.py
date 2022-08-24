# from exchange_rates_data import data
#
# print(data)

from tkinter import *

window = Tk()
window.title("Currency Converter")
window.minsize(width=900, height=600)
window.config(padx=50, pady=100)


label = Label(text="From", font=("Arial", 25, "bold"))
label.grid(row=0, column=0)


def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
    # print("45852")


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=1, column=0)




window.mainloop()