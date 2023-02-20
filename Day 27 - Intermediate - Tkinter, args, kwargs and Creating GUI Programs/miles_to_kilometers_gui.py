from tkinter import *

window = Tk()
window.minsize(width=300, height=70)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def cal_km():
    value = mile_entry.get()
    km = float(value) * 1.60934
    kmvalue_label.config(text=round(km, 2)) 

# entry 
mile_entry = Entry(width=10)
mile_entry.insert(END, 0)
mile_entry.grid(row=0, column=1)

# label
empty_label = Label(text="                                ")
empty_label.grid(row=0, column=0) 
mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

equal_label = Label(text="         is eaqual to")
equal_label.grid(row=1, column=0)

kmvalue_label = Label(text=0)
kmvalue_label.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

# Button 
calculate_button = Button(text="Calculate", command=cal_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
