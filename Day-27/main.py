from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

label_miles = Label(text="Miles", font=("Arial", 16, "italic"))
label_miles.grid(column=2, row=0)

label_result = Label(text="0", font=("Arial", 12, "bold"))
label_result.grid(column=1, row=1)

label_km = Label(text="Km", font=("Arial", 16, "italic"))
label_km.grid(column=2, row=1)

label_equal = Label(text="is equal to", font=("Arial", 16, "italic"))
label_equal.grid(column=0, row=1)

def button_clicked():
    miles = float(input_miles.get())
    km = miles * 1.60934
    label_result.config(text=f"{round(km, 2)}")


button_calculate = Button(text="Calculate", command=button_clicked)
button_calculate.grid(column=1, row=2)

input_miles = Entry(width=10)
input_miles.insert(END, string="0")
input_miles.grid(column=1, row=0)
window.mainloop()







# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=20,pady=20)

#Label

# my_label = Label(text="New Text", font=("Arial", 24, "italic"))
# my_label.grid(column=0, row=0)
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.config(padx=20,pady=20)
#Button

# def button_clicked():
    # my_label.config(text=input.get())

#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)


#Entry

# input = Entry(width=10)
# input.grid(column=3, row=2)
#
# window.mainloop()