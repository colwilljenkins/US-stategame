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
all_states = df.state.to_list()

# game fundamentals
game_is_on = True
score = 0
guessed_states = []

# Game exit instructions
exit_inst = turtle.Turtle()
exit_inst.penup()
exit_inst.hideturtle()
exit_inst.goto(0, -260)
exit_inst.write("Type 'Exit' to exit game and show missing states", align = 'center')


while game_is_on:
    answer_state = screen.textinput(title=f'{score}/50 States', prompt="What's another states name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missed_states = pd.DataFrame(missing_states)
        missed_states.to_csv('States-to-learn.csv')
        game_is_on = False

    elif score == 50:
        over = turtle.Turtle()
        over.penup()
        over.hideturtle()
        over.write('YOU WIN', align = 'center', font = ('courier', 40, 'bold'))
        game_is_on = False
    elif answer_state in all_states:
        if answer_state in guessed_states:
            pass
        else:
            guessed_states.append(answer_state)
            state_df = df[df['state'] == answer_state]
            state_title = turtle.Turtle()
            state_title.penup()
            state_title.hideturtle()
            state_title.goto(int(state_df.x), int(state_df.y))
            state_title.write(answer_state.title(), align = 'center')
            score += 1


screen.exitonclick()

# get x and y coor if not in given data

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
