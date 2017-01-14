# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = True
outcome = ""
score = 0
used_cards = []
dealer = []
player = []
shuffled_deck = ''
player_pos = 350
dealer_pos = 150
x_pos = 100

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_list = []
        self.hand_value = 0

    def __str__(self):
        # return a string representation of a hand
        ans = ''
        for e in self.hand_list:
            ans += str(e) + ' '
        s = 'Hand contains ' + ans
        return 	s

    def add_card(self, card):
        # add a card object to a hand
        self.card = card
        self.hand_list.append(self.card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        self.hand_value = 0
        for i in self.hand_list:
            if i.get_rank() in VALUES:
                self.hand_value += VALUES[i.get_rank()]
        for b in self.hand_list:    
            if 'A' == b.get_rank():
                if self.hand_value + 10 <= 21:
                    self.hand_value += 10
        return self.hand_value
                
   
    def draw(self, canvas, pos):
        global x_pos
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.hand_list)):
            self.hand_list[i].draw(canvas, (pos[0] + i * CARD_SIZE[0], pos[1]))
         
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck_cards = []
        for s in SUITS:
            for r in RANKS:
                card_open = Card(s,r)
                self.deck_cards.append(card_open)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_cards)

    def deal_card(self):
        a = random.choice(self.deck_cards)
        if a not in used_cards:
            used_cards.append(a)	
            return a #####dont' forget to clear used_cards
        else:
            a = random.choice(self.deck_cards)
            return a
        
    def __str__(self):
        # return a string representing the deck
        deck_string = ''
        for i in self.deck_cards:
            deck_string += i + ' '
        return 'Deck Contains: ' + deck_string



#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, shuffled_deck, used_cards
    used_cards = []
    shuffled_deck = Deck()
    shuffled_deck.shuffle()
    in_play = True
    
    player = Hand()
    dealer = Hand()
    
    player.add_card(shuffled_deck.deal_card())
    dealer.add_card(shuffled_deck.deal_card())
    player.add_card(shuffled_deck.deal_card())
    dealer.add_card(shuffled_deck.deal_card())
    outcome = 'Hit or Stand?'
    
    print 'Player',player
    print "Dealer", dealer
    print 

def hit():
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    global in_play, score, outcome
    player.add_card(shuffled_deck.deal_card())
    if (player.get_value() <= 21) and in_play:
        print player
        print 'Card Value: ', player.get_value()
        print
    else:
        if in_play:
            in_play = False
            score -= 1
            print player
            print 'Player Card Value: ', player.get_value()
            print 'Dealer Card Value: ', dealer.get_value()
            outcome = 'You have BUSTED.'
            print
            print 'Score: ', score
       
def stand():
    # replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    
    global score, in_play, outcome
    
    if player.get_value() > 21:
        outcome = 'You have already BUSTED son!'
        print
        return
        
    while dealer.get_value() < 17:
        dealer.add_card(shuffled_deck.deal_card())
    
    if in_play:
        if dealer.get_value() >=  player.get_value() and dealer.get_value() <= 21:
            in_play = False
            outcome = 'You Lose!'
            score -= 1
        elif in_play:
            in_play = False
            score += 1
            outcome = 'You Win!'
        else:
            return
    
    print 'Player Card Value: ', player.get_value()
    print 'Dealer Card Value: ', dealer.get_value()
    print 'Score: ',score
    print 
    

# draw handler    
def draw(canvas):
    global player_pos, dealer_pos, x_pos
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BlackJack", (230, 40), 35, 'White')
    canvas.draw_text("Score: " + str(score), (500, 575), 25, 'White')
    canvas.draw_text("Dealer's Hand", (100, 100), 25, 'Black')
    canvas.draw_text("Player's Hand", (100, 320), 25, 'Black')
    canvas.draw_text("Dealer's Card Value "+ str(dealer.get_value()), (300, 100), 25, 'Black')
    canvas.draw_text("Player's Card Value "+ str(player.get_value()), (300, 320), 25, 'Black')
    canvas.draw_text(outcome, (100, 520), 25, 'Orange')
    
    #draw dealer's cards
    dealer.draw(canvas, (x_pos, dealer_pos))
    
    #draw player's cards
    player.draw(canvas, (x_pos, player_pos))


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric