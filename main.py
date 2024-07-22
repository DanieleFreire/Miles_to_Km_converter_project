from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")
    print(km)

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

#Entry
input = Entry(width=7)
#Add some text to begin with
input.insert(END, string="0")
input.grid(column=1, row=0)

#Miles Label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)


#is equal to Label
is_equal_to_label = Label(text="is equal to", font=("Arial", 12))
is_equal_to_label.grid(column=0, row=1)

#kilometer result label
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

#Km Label
km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)


#Button
#calls miles_to_km() when pressed
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()