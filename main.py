import turtle
import pandas

screen = turtle.Screen()
screen.title("Mapa do Brasil")
image = "brasilbranco_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("estados.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 26:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/26, Advinhe o estado",
                                    prompt="Qual é o nome do estado?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("estados_restantes.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





# Codigo usado pra conseguir as coordenadas dos estados
"""def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()"""
