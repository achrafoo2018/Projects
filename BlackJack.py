import random

'''

Black Jack Game VS Computer

Here is the game's rules:

The objective is to get a hand total of closer to 21 
than the dealer without going over 21 (busting). At 
the start of a Blackjack game, the players and the 
dealer receive two cards each. The players' cards are 
normally dealt face up, while the dealer has one face 
down (called the hole card) and one face up.

'''

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    '''
    Representation of the Card
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck(object):
    '''
    Representation of the deck
    '''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return '\t|\t'.join([str(self.deck[i]) for i in range(len(self.deck))])

    def shuffle_deck(self):
        random.shuffle(self.deck) # shuffle the deck's cards

    def deal(self):
        return self.deck.pop(-1) # deal 1 card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card): # Add card to the hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Bank: # Player Bank Account money to play with
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def __str__(self):
        print('Name: {}\nwallet: {} $\n'.format(self.name.capitalize(), self.wallet))

    def withdraw(self, with_amnt):
        if with_amnt > self.wallet:
            print("You don't have enough Funds")
        else:
            self.wallet -= with_amnt
            print('Operation done successfully\nYou have {} $ remain in your bank account !'.format(self.wallet))
            return with_amnt

    def deposit(self, dep_amnt):
        self.wallet += dep_amnt
        print("{} $ Deposited successfully onto Your bank account!".format(dep_amnt))


def bet_ask():
    while 1:
        try:
            choice = int(input('Enter Your bet : '))
            if choice < 0:
                continue
        except:
            print('Enter Valid Value !!')

        else:
            break
    return choice

def bust(hand): # check if total is greater than 21
    if hand.value > 21:
        return True
    else:
        return False

def replay(): # ask players whether they want to play again
    while 1:
        again = input("\t\t\tYou want to play again (y/n)?")
        if again in ['y', 'Y','Yes','YES','n','N','No', 'NO']:
            break
    return again not in ['n','N','No', 'NO']


def show_all(player, dealer): # print player's and dealer's cards
    print("\nDealer's Hand:", *dealer.cards, sep='\t|')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\t| ')
    print("Player's Hand =", player.value)


def show_some(player, dealer):
    print("\nDealer's Hand:\t|<card hidden>\t|", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\t| ')

# main
playing = True
if __name__ == '__main__':
    player = Bank('Player', random.randint(10000,50000)) # give random amount of money to player to bet with
    while playing:
        print('You Have {} $ in Your Bank Account'.format(player.wallet)) # print player's money
        deck = Deck()
        deck.shuffle_deck()
        BetAmount = player.withdraw(bet_ask()) # withdraw bet amount from player's bank account
        if BetAmount == None: # check if the player don't have enough money in his bank account
            break
        PlayerHand = Hand()
        DealerHand = Hand()
        for i in range(2): # give to cards to the player and the dealer
            PlayerHand.add_card(deck.deal())
            DealerHand.add_card(deck.deal())

        show_some(PlayerHand, DealerHand)
        if PlayerHand.value == 21: # Check If the player cards value equal to 21
            show_all(PlayerHand, DealerHand)
            print('Congratulations You Won The Game ')
            player.deposit(BetAmount * 2)
            playing = replay()
            print('\n' * 50)
            continue
        while not bust(PlayerHand): # while player card's value < 21 ask him if he wants to hit another card or stand
            try:
                PlayerDecision = int(input("1)Hit\n2)Stand "))
                if PlayerDecision == 1:
                    PlayerHand.add_card(deck.deal())
                    show_some(PlayerHand, DealerHand)
                    if PlayerHand.value == 21:  # Check If the player cards value equal to 21
                        show_all(PlayerHand, DealerHand)
                        print('Congratulations You Won The Game ')
                        player.deposit(BetAmount * 2)
                        playing = replay()
                        print('\n' * 50)
                        continue
                elif PlayerDecision == 2:
                    break
            except:
               print('1 or 2 !!!')

        if bust(PlayerHand): # check if player is busted
            print(f"You lost the game")
            playing = replay()
            print('\n' * 50)
            continue

        while DealerHand.value < 17: # dealer keep hitting another card until his cards value exceeds 21
            DealerHand.add_card(deck.deal())
        if bust(DealerHand): # check if the dealer is busted
            show_all(PlayerHand, DealerHand)
            print('Congratulations You Won The Game ')
            player.deposit(BetAmount * 2) # player won and his money is doubled and deposited to his bank account
            playing = replay() # ask for replay
            print('\n' * 50)
            continue
        else:
            if DealerHand.value > PlayerHand.value:
                show_all(PlayerHand, DealerHand)
                print("Oups You Lost The game ")
                playing = replay()
                print('\n' * 50)
                continue
            elif DealerHand.value < PlayerHand.value:
                show_all(PlayerHand, DealerHand)
                print('Congratulations You Won The Game ')
                player.deposit(BetAmount * 2)
                playing = replay()
                print('\n' * 50)
                continue
            else:
                show_all(PlayerHand, DealerHand)
                print('Tied Game !! GG ')
                player.deposit(BetAmount)
                playing = replay()
                print('\n' * 50)
