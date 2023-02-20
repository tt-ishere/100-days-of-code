from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
bg = Turtle()
bg.shape(image)

correct_answer = 0
guessed_states = []
states_data = pandas.read_csv("50_states.csv")
state_list = states_data.state.to_list()

while len(guessed_states) < 50:
    # get user input and convert to tittle case
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state name? ").title()

    
    if answer_state == "Exit":
        states_to_learn = [states for states in state_list if states not in guessed_states]
        ms = pandas.DataFrame(states_to_learn)
        ms.to_csv("states_to_learn.csv")
        break
    #     for states in state_list:
    #         if states not in guessed_states:
    #             states_to_learn.append(states)
    
    
    

    if answer_state in state_list:
        state_row = states_data[states_data.state == answer_state]
        st = Turtle()
        st.hideturtle()
        st.penup()
        st.goto(int(state_row.x), int(state_row.y))
        st.write(arg=f"{answer_state}", align="center", font=("Arial", 8, "normal"))

        correct_answer += 1  # keep track of score
        guessed_states.append(answer_state)  # record correct guesses in a lis