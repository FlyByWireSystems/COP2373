import random

# Deck object
class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]  # creates the list of cards as numbers 0–51
        random.shuffle(self.card_list)             # shuffles the deck randomly
        self.current_card = 0                      # tracks which card to deal next
        self.size = size                           # the total size of deck

    def deal(self):
        # if all cards are dealt, reshuffles it automatically
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        # deals the next card and moves the index forward
        self.current_card += 1
        return self.card_list[self.current_card - 1]



# function to deal the initial poker hand
def deal_hand(deck):
    hand = []                                     # creates an empty list for cards to exist in
    for i in range(5):                            # deals the 5 cards for poker hand
        card_num = deck.deal()                    # get next card from deck
        hand.append(card_num)                     # add it to hand
    return hand                                   # return list of the 5 card numbers in your hand



# function that prints the hand
def show_hand(hand, ranks, suits):
    for c in range(len(hand)):                    # goes through each card number
        r = hand[c] % 13                          # find rank (0–12)
        s = hand[c] // 13                         # find suit (0–3)
        print(c + 1, ranks[r], 'of', suits[s])    # print with numbering


# function to replace selected cards
def draw_new_cards(deck, hand, indices):
    for i in indices:                             # for each index the user typed
        if 1 <= i <= 5:                           # only valid positions
            hand[i - 1] = deck.deal()             # replace that card with a new one
    return hand                                   # return the updated hand


# main game function
def poker_draw_game():
    ranks = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'J', 'Q', 'K', 'A']       # ranks of cards
    suits = ['clubs', 'diamonds', 'hearts', 'spades']   # suits of cards
    my_deck = Deck(52)                            #  create and shuffle deck of 52 cards


    print('Your initial poker hand:')
    hand = deal_hand(my_deck)                     # deal 5 cards
    show_hand(hand, ranks, suits)                 # show hand to user


    # ask user which cards to replace
    user_input = input('\nEnter the numbers of the cards you want to replace (e.g. 1 5 3), or press Enter to keep all: ')
    if user_input.strip() != '':                  # if user entered something
        indices = [int(x) for x in user_input.split()]  # convert to list of numbers
        hand = draw_new_cards(my_deck, hand, indices)   # replace those cards



    print('\nYour final poker hand:')
    show_hand(hand, ranks, suits)                 # show final hand


# starts the game
poker_draw_game()