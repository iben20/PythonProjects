# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

#scores
score1 = 0
score2 = 0

#paddle position
paddle1_pos = 200
paddle2_pos = 200

#paddle velocity
paddle1_vel = 0
paddle2_vel = 0

#ball variables  
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [random.randrange(120, 140)/60, random.randrange(60, 180)/60]
    
    if direction:
        ball_vel[0] = ball_vel[0]
        
    elif direction == False:
        ball_vel[0] = -ball_vel[0]
        
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel = 200,200,0,0
    score1, score2 = 0,0
    spawn_ball(random.choice([True, False]))

def draw(canvas):
    global score1, score2, paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] -= ball_vel[1]
    
    if (ball_pos[0] <= BALL_RADIUS) or (ball_pos[0] >= ((WIDTH - 8) - BALL_RADIUS)):
        if (ball_pos[0] < WIDTH/2) and (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT)):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = 1.1* ball_vel[0]
        elif (ball_pos[0] > WIDTH/2) and (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT)):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = 1.1* ball_vel[0]
        elif (ball_pos[0] < (WIDTH/2)) and ((ball_pos[1] < paddle1_pos - HALF_PAD_HEIGHT) or (ball_pos[1] > paddle1_pos + HALF_PAD_HEIGHT)):
            score2 += 1
            spawn_ball(True)
        elif (ball_pos[0] > (WIDTH/2)) and ((ball_pos[1] < paddle2_pos - HALF_PAD_HEIGHT) or (ball_pos[1] > paddle2_pos + HALF_PAD_HEIGHT)):
            score1 += 1
            spawn_ball(False)
            
        
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= ((HEIGHT - 1) - BALL_RADIUS)):
        ball_vel[1] = -ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, 20, 2, 'Red', 'White')
    
    # update paddle's vertical position, keep paddle on the screen   
        
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if ((paddle1_pos + 40) >= HEIGHT) or ((paddle1_pos - 40) <= 0):
        paddle1_vel = 0
    elif ((paddle2_pos + 40) >= HEIGHT) or ((paddle2_pos - 40) <= 0):
        paddle2_vel = 0
        
    canvas.draw_line((3, paddle1_pos - 40), (3, paddle1_pos + 40), 8, 'Orange')
    canvas.draw_line((597, paddle2_pos - 40), (597, paddle2_pos + 40), 8, 'Orange')
    
    # draw scores
    canvas.draw_text( str(score1), (147, 40), 30, 'White')
    canvas.draw_text( str(score2), (447, 40), 30, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if (simplegui.KEY_MAP['s'] == key) and ((paddle1_pos + 40) <= HEIGHT):
        paddle1_vel = 5
    elif (simplegui.KEY_MAP['down'] == key) and ((paddle2_pos + 40) <= HEIGHT):
        paddle2_vel = 5
    elif (simplegui.KEY_MAP['w'] == key) and ((paddle1_pos - 40) >= 0):
        paddle1_vel = -5  
    elif (simplegui.KEY_MAP['up'] == key) and ((paddle2_pos - 40) >= 0):
        paddle2_vel = -5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel, paddle2_vel = 0, 0
   

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Reset', new_game, 160)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
