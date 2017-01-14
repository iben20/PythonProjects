# implementation of card game - Memory

import simplegui
import random

#Cards in Play
list1 = range(8)
list2 = range(8)
card_list = []
card_list.extend(list1)
card_list.extend(list2)

#True = open cards, False = closed cards
exposed = range(16)
for i in exposed:
    exposed[i] = False
    i += 1
    
#Counter/state/index/flag
counter = -1
state = 0
index_card = []
turn = 0
    
#Shuffle the cards
random.shuffle(card_list)

#Card Position variable 
position = 15

#Back of cards
rect_x1, rect_x2, rect_y1, rect_y2 = 0,50,0,100

# helper function to initialize globals
def new_game():
    global card_list, exposed, counter, state, index_card, turn
    list1 = range(8)
    list2 = range(8)
    card_list = []
    card_list.extend(list1)
    card_list.extend(list2)
    exposed = range(16)
    for i in exposed:
        exposed[i] = False
        i += 1
    counter = -1
    state = 0
    index_card = []
    turn = 0
    label.set_text('Turns: ' + str(turn))
    random.shuffle(card_list)

     
# define event handlers
def mouseclick(pos):
    global exposed, state, index_card, turn
    # add game state logic here
       
    if len(index_card) == 2:
        if (card_list[index_card[0]] == card_list[index_card[1]]) == False:
            exposed[index_card[0]] = False
            exposed[index_card[1]] = False
        index_card = []
    index = pos[0]//50
    
    if exposed[index] == True:
        return
    
    index_card.append(index)
    exposed[index] = True    
    
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
        #leave exposed if match
        if card_list[index_card[0]] == card_list[index_card[1]]:
            exposed[index_card[0]] = True
            exposed[index_card[1]] = True
        turn += 1
        label.set_text('Turns: ' + str(turn))
    else:
        state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global position, exposed, rect_x1, rect_x2, rect_y1, rect_y2, counter  
    
    for i in exposed:
        counter += 1
        if i == True:
            #draw cards
            canvas.draw_text(str(card_list[counter]), 
                                (position,65), 45, 'red')
        
        else:        
        #draw back cards
            canvas.draw_polygon([[rect_x1, rect_y1], [rect_x2,rect_y1], 
                                [rect_x2, rect_y2], [rect_x1,rect_y2]], 
                                1, 'red', 'white')
        rect_x1 += 50
        rect_x2 += 50
        if rect_x2 > 801:
            rect_x1, rect_x2 = 0,50        
        position += 50
        if position > 800:
            position = 15
        if counter == 15:
            counter = -1
        
      

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns: 0')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric