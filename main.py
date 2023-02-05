import random
def game1():
  while True: 
    user_action = input("Enter a choice (boulder, tree, axe): ")
    possible_actions = ["boulder", "tree", "axe", "bomb"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
      print(f"And...both players selected {user_action} nobody wins. Its a tie!")
    elif user_action == "boulder":
      if computer_action == "tree":
        print("Tree stops boulder!! You lose!")
      if computer_action == "axe":
        print("Snap! The axe couldn't cut the boulder, you win!")
      if computer_action == "bomb":
        print("Boulder? More like pebble, you lose!!")
    elif user_action == "axe":
      if computer_action == "tree":
        print("Timber! Axe chops down tree, you win!")
      if computer_action == "boulder":
        print("Snap! Stone is a little harder than wood, you lose!!")
      if computer_action == "bomb":
        print("Not cutting much anymore...you lose!!")
    elif user_action == "tree":
      if computer_action == "boulder":
        print("Tree stops boulder! You win!")
      if computer_action == "axe":
        print("Timberr! Down goes the tree, you lose!!")
      if computer_action == "bomb":
        print("Smells like fire...wood. You lose!")
    play_again = input("Play again? (yes/no):")
    if play_again.lower() !="y":
      breakpoint
def game2():   
  '''

This is a python game that was created using the built-in turtle module similar to the Google Snake Game (02/28/2020)

'''



import turtle 

top_score = 0

game = turtle.Screen()

game.bgcolor("gray")

game.setup(width=500, height=500)

game.title("Snake Game: Abdulrahman Abbas")

game.tracer(0)



import time

delay = 0.1

score = 0



first_segment = turtle.Turtle()

first_segment.speed(0)

#fastest animation speed so there's no lag

first_segment.shape("circle")

first_segment.color("blue")

first_segment.penup()

first_segment.direction = "stop"



segments = []



food = turtle.Turtle()

food.speed(0)

food.shape("triangle")

food.color("purple")

food.penup()

food.goto(0,200)





pen = turtle.Turtle()

pen.speed(0)

pen.color("black")

pen.penup()

pen.ht() #ht is hide turtle

pen.goto(0, 220)

pen.write("Current Score: 0 ----- Top Score: 0", align="center", font=("Sans serif", 30, "normal"))









def move():

    if first_segment.direction == 'up':

        first_segment.sety(first_segment.ycor()+20)

    if first_segment.direction == 'left':

        first_segment.setx(first_segment.xcor()-20)

    if first_segment.direction == 'down':

        first_segment.sety(first_segment.ycor()-20)

    if first_segment.direction == 'right':

        first_segment.setx(first_segment.xcor()+20)





def up():

    first_segment.direction = 'up'

def down():

    first_segment.direction = 'down'

def left():

    first_segment.direction = 'left'

def right():

    first_segment.direction = 'right'



game.listen()

game.onkeypress(up, 'Up')

game.onkeypress(down, 'Down')

game.onkeypress(left, 'Left')

game.onkeypress(right, 'Right')



import random 



while True:

    game.update()



    if first_segment.xcor()>230 or first_segment.xcor()<-230 or first_segment.ycor()>230 or first_segment.ycor()<-230:

        time.sleep(1)

        first_segment.goto(0,0)

        first_segment.direction = 'stop'



        #get rid of segments

        for i in segments:

            i.goto(1000,1000)

        segments = []

        score = 0

        delay = 0.1



        pen.clear()

        pen.write("Current Score: " + str(score) +' ----- '+ "Top Score: " + str(top_score), align='center', font=('Sans Serif', 30, "normal" ))

    if first_segment.distance(food) < 15:

        x = random.randint(-220,220)

        y = random.randint(-220,220)

        food.goto(x,y)

        #this moves the food to a random spot on within the screen

        body_segment = turtle.Turtle()

        body_segment.speed(0)

        body_segment.shape('square')

        body_segment.color("blue")

        body_segment.penup()

        segments.append(body_segment)



        delay -= 0.001

        score += 1



        if score > top_score:

            top_score = score



        pen.clear()

        pen.write("Current Score: " + str(score) +' ----- '+ "Top Score: " + str(top_score), align='center', font=('Sans Serif', 30, "normal" ))

    

    for i in range(len(segments)-1,0, -1):

        x = segments[i-1].xcor()

        #moves the segment to where the segment before it was

        y = segments[i-1].ycor()

        segments[i].goto(x,y)

    

    if len(segments) > 0:

        x = first_segment.xcor()

        y = first_segment.ycor()

        segments[0].goto(x,y)



    move()



    for i in segments:

        if i.distance(first_segment) < 20:

            time.sleep(1)

            first_segment.goto(0,0)

            first_segment.direction = "stop"

            for i in segments:

                i.goto(1000,1000)

            segments = [] 



    time.sleep(delay)

game.mainloop()

if __name__ == '__main__':  # This is how you usually do it.
    choice = input('Please select 1 for game1 and 2 for game2')
    if choice == '1':
        game1()
    elif choice == '2':
        game2()
    else:
        print('Please select a valid choice next time...!')