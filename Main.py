import pandas
import turtle

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_states = []
while len(guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="Wild guess MF!").title()

    if user_guess == "Exit":
        break

    if user_guess in all_states:
        guessed_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_guess)

states_final = [states_final for states_final in all_states if states_final not in guessed_states]
data_final = pandas.DataFrame(states_final)
data_final.to_csv("Needtolearn.csv")
