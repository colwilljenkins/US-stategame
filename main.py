import pandas as pd
import turtle

# Background set up
screen = turtle.Screen()
screen.title('US State Game')
# Turtle only works with gif
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Turning CSV into df
df = pd.read_csv('50_states.csv')

# game fundamentals
game_is_on = True
score = 0

# Prompting user input and saving to title case for search
answer_state = screen.textinput(title='Guess the State', prompt="What's another states name?")

while game_is_on:
    answer = df[df['state'] == answer_state.title()]
    if score == 50:
        over = turtle.Turtle()
        over.penup()
        over.hideturtle()
        over.write('YOU WIN', align = 'center', font = ('courier', 40, 'bold'))
        game_is_on = False
    if len(answer) > 0:
        y_cor = int(answer['y'])
        x_cor = int(answer['x'])
        state_title = turtle.Turtle()
        state_title.penup()
        state_title.hideturtle()
        state_title.goto(x_cor, y_cor)
        state_title.write(answer_state.title(), align = 'center')
        score += 1
        answer_state = screen.textinput(title=f'{score}/50 States', prompt="What's another states name?")
    else:
        answer_state = screen.textinput(title=f'{score}/50 States', prompt="Not correct\nWhat's another states name?")

screen.exitonclick()

# get x and y coor if not in given data

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
