from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


my_label = Label(text="I'm a label", font=('Ariel', 24))
my_label.pack()

def click_button():
    my_label.config(text=input.get())
    

# Button 
button = Button(text="Click me", command=click_button)
button.pack()

# Entry 
input = Entry(width=10)
input.pack()

input.get()


window.mainloop()
