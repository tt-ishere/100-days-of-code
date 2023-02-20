from tkinter import *
import pandas as pd
import random


window = Tk()
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#fff"
BLACK = "black"
current_card = {}
words_data = {}

try:
    data = pd.read_csv("flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    oringinal_data = pd.read_csv("flash-card-project-start/data/french_words.csv")
    words_data = oringinal_data.to_dict("records")
else:  
    words_data = data.to_dict("records")


def next_card():
    global current_card, count_down
    
    window.after_cancel("count_down")
    canvas.itemconfig(card_tittle, text="French")
    current_card = random.choice(words_data)
    canvas.itemconfig(card_word, text=current_card['French'])
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_word, fill=BLACK)
    canvas.itemconfig(card_tittle, fill=BLACK)
    count_down = window.after(3000,turn_card)
    

def is_known():
    global words_data
    
    words_data.remove(current_card)
    print(len(words_data))
    data = pd.DataFrame(words_data)
    data.to_csv("flash-card-project-start/data/words_to_learn.csv", index=False)
    
    next_card()

  
def turn_card():
    canvas.itemconfig(card_tittle, text="English")
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_word, fill=WHITE)
    canvas.itemconfig(card_tittle, fill=WHITE)


window.title("Flashy Flash Cards")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0) 
card_front = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="flash-card-project-start/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_tittle = canvas.create_text(400, 100, text="",font=("Times New Roman", 49, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Times New Roman", 49, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()