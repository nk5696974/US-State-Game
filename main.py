import turtle
import pandas

SCORE = 0
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):              #   =>stackoverflow code
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()             

usMap = pandas.read_csv("50_states.csv")           #open csv file.

stateList = [] 
secondList = []     #second list create to store user input and avoid rewriting, and it also inhance score couting.

data = usMap["state"]                   #storing state names.
stateList = data.to_list()

while len(secondList) <= 50:
    userInput = screen.textinput(title=f"Guess the state {SCORE}/50", prompt="What's another state?")
    userInput = userInput.title()

    if userInput=="Exit":
        break
    if userInput in stateList:
        if not(userInput in secondList):
            secondList.append(userInput)
            data = usMap[usMap["state"] == userInput]
            coorX = int(data["x"])                             #getting X coordinate
            coorY = int(data["y"])                             #getting Y coordinate
            
            SCORE += 1

            new_turtle = turtle.Turtle()          #turtle funcions
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(coorX, coorY)
            new_turtle.write(arg=userInput, font=('Arial', 8, 'normal'))
    
# states_to_learn.csv
# MissedStates = []                    #create a list to states which are not entered by user.
# for state in secondList:
#     if not(state not in stateList):
#         MissedStates.append(state)

# df = pandas.DataFrame(MissedStates)
# df.to_csv("state_to_learn.csv")
