import random

coins = 100000

deck = []
deckCards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

def stats():
    print('\nSTATS')
    print('coins: '+ str(coins))
    print('coins gained/lost: ' + str(coins-100000))

def shuffleDeck():
    for x in range(0, 24):
        deck.extend(deckCards)
    random.shuffle(deck)

def game(c):
    dealerHand = []
    playerHand = []

    dealerCount = 0
    playerCount = 0

    while True:
        bet = int(input('make a bet: '))
        if c-bet >= 0:
            break
        else:
            print('not enough money')
            print("coins = " + str(c))

    while playerCount <= 21:
        print(str(playerHand) + ' = ' + str(playerCount))
        print(str(dealerHand) + ' = ' + str(dealerCount))
        move = input('hit(h)/stand(s) ')

        if move.lower() == 's' or playerCount == 21:
            while dealerCount < 17:
                if deck[0] == 'A':
                    dealerHand.append(deck[0])
                else:
                    dealerHand.insert(0, deck[0])
                deck.pop(0)

                dealerCount = 0

                for x in dealerHand:
                    if x == 'J' or x == 'Q' or x == 'K':
                        dealerCount += 10
                    elif x == 'A':
                        if (dealerCount + 11) <= 21:
                            dealerCount += 11
                        else:
                            dealerCount += 1
                    else:
                        dealerCount += x
            break
        elif move.lower() == 'h':
            if deck[0] == 'A':
                playerHand.append(deck[0])
            else:
                playerHand.insert(0, deck[0])
            deck.pop(0)

            playerCount = 0

            for x in playerHand:
                if x == 'J' or x == 'Q' or x == 'K':
                    playerCount += 10
                elif x == 'A':
                    if (playerCount + 11) <= 21:
                        playerCount += 11
                    else:
                        playerCount += 1
                else:
                    playerCount += x

    print(str(playerHand) + ' = ' + str(playerCount))
    print(str(dealerHand) + ' = ' + str(dealerCount))
    
    if playerCount > 21:
        print('DEALER WON!')
        print(str(c) + '-' + str(bet))
        c -= bet
        print('= ' + str(c))
        return c
    elif dealerCount > 21 and playerCount <= 21:
        print('PLAYER WON!')
        print(str(c) + '+' + str(bet))
        c += bet
        print('= ' + str(c))
        return c
    elif dealerCount < playerCount:
        print('PLAYER WON!')
        print(str(c) + '+' + str(bet))
        c += bet
        print('= ' + str(c))
        return c
    elif dealerCount > playerCount:
        print('DEALER WON!')
        print(str(c) + '-' + str(bet))
        c -= bet
        print('= ' + str(c))
        return c
    else:
        print('TIE!')
        return c

while True:
    #running games
    print("play a game? (y/n)")
    playGame = input()
    if playGame.lower() == 'y':
        #play game
        shuffleDeck()
        coins = game(coins)

        if coins <= 0:
            print('you lost all your money')
            break

    elif playGame.lower() == 'n':
        stats()
        break
    else:
        print("not an option dingus")
        continue