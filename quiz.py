import pgzrun

WIDTH = 900
HEIGHT = 600

questions = []
q = open("questions.txt","r")
lines = q.readlines()
for i in lines:
    questions.append(i)
# print(questions)
x = questions[0]
# print(questions.pop(0).split(","))
questindex = 0

def readq():
    global questindex
    questindex = questindex + 1
    y = questions.pop(0).split(",")
    print(y)
    return y

current = readq()



marqueebox = Rect(0,0,900,50)
questionbox = Rect(15,55,650,180)
answer1 = Rect(15,250,310,160)
answer2 = Rect(330,250,310,160)
answer3 = Rect(15,420,310,160)
answer4 = Rect(330,420,310,160)
answers = [answer1,answer2,answer3,answer4]
skipbox = Rect(675,250,200,330)
timebox = Rect(675,55,200,180)



def draw():
    screen.draw.filled_rect(marqueebox, "lightgray")
    screen.draw.filled_rect(questionbox,"goldenrod")
    screen.draw.filled_rect(answer1,"goldenrod")
    screen.draw.filled_rect(answer2,"goldenrod")
    screen.draw.filled_rect(answer3,"goldenrod")
    screen.draw.filled_rect(answer4,"goldenrod")
    screen.draw.filled_rect(skipbox,"blue")
    screen.draw.filled_rect(timebox,"lightgray")
    screen.draw.textbox(current[0].strip(), questionbox, color="magenta")
    screen.draw.textbox(current[1].strip(), answer1, color="magenta")
    screen.draw.textbox(current[2].strip(), answer2, color="magenta")
    screen.draw.textbox(current[3].strip(), answer3, color="magenta")
    screen.draw.textbox(current[4].strip(), answer4, color="magenta")
    screen.draw.textbox("Skip", skipbox, color="lightgray", angle=-90)
def update():
    pass

def correct():
    global current, questions
    if questions:
        current = readq()

def skip():
    global current
    if questions:
        current = readq()


def on_mouse_down(pos):
    global answers
    index = 1
    for box in answers:
        if box.collidepoint(pos):
            if index == int(current[5]):
                correct()
                print("correct")
        index = index + 1
    if skipbox.collidepoint(pos):
        skip()

pgzrun.go()