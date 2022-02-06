from tkinter import *

def calculationen():
    miles = float(input.get())
    kilometres = miles * 1.60934
    kilometers_val["text"] = round(kilometres, 2)
    # kilometers_val.config(text=round(kilometres))



window = Tk()
window.title("Miles Morales to Kilometers Morales")
window.minsize(width=300, height=75)
window.config(padx=15, pady=10)



input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles Morales", font=("Times new Roman", 11))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Times new Roman", 11))
equal_label.grid(column=0, row=1)


kilometres = 0

kilometers_val = Label(text=f"{kilometres}",font=("Times new Roman", 11))
kilometers_val.grid(column=1, row=1)

kilo_label = Label(text="Kilometers Morales", font=("Times new Roman", 11))
kilo_label.grid(column=2, row=1)


button = Button(text="Calculate", command=calculationen)
button.grid(column=1, row=2)


window.mainloop()