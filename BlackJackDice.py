##PROBLEM: Simulate the Blackjack Dice betting game
##
##ALGORITHM:
##      1. Ask the player for the pot amount
##      2. Ask the player for their wager
##      3. Both the player and dealer will roll two dice
##      4. Player keeps rolling until they stay or bust (dice total over 21)
##      5. Dealer keeps rolling until they beat the player or bust
##      6. Award the wager to the player closest to 21 without going over
##      7. Players keep playing until the pot is empty (jump to step 2)
##      8. Display the total rounds played and the highest pot attained in game
##      9. Ask if they want to play again or quit
##
##ERROR HANDLING: None.
import random

print("Welcome to Blackjack Dice\n")

playing = True
while playing:
    
    # Ask the player for the pot amount
    pot = 0
    while pot <= 0:
        userInput = input("Enter the amount of money you want in chips, or H for help ==> $").upper()
        if userInput in ("H", "HELP"):
            print("\nBlackjack Dice is a simple dice game. The player plays against the")
            print("dealer. First, both players roll two dice. Then, each player keeps")
            print("rolling until they stay (stop rolling), or bust (total is over 21).")
            print("The player closest to 21 without going over wins.\n")
        else:
            pot = int(userInput)
            if pot <= 0:
                print("The amount must be greater than 0\n")
    
    rounds = 0
    maxPot = pot
    while pot > 0:
        
        # Ask the player for their wager
        wager = 0
        while True:
            wager = int(input("Enter the amount you want to wager. ==> $"))
            if wager <= 0:
                print("The amount must be greater than 0")
            elif wager > pot:
                print("The wager cannot be greater than the amount you have in the pot")
            else:
                break

        # Both the player and dealer will roll two dice
        dealerDie1 = random.randint(1, 6)
        dealerDie2 = random.randint(1, 6)
        dealerTotal = dealerDie1 + dealerDie2
        print("\nDealer rolled a", dealerDie1, "and", dealerDie2, "for a total of", dealerTotal)

        playerDie1 = random.randint(1, 6)
        playerDie2 = random.randint(1, 6)
        playerTotal = playerDie1 + playerDie2
        print("\nYou rolled a", playerDie1, "and", playerDie2, "for a total of", playerTotal)

        # Player keeps rolling until they stay or bust (dice total over 21)
        while playerTotal <= 21:
            roll = input("Do you want to roll again (Y,YES,N,NO)? ").upper()
            if roll in ("Y", "YES"):
                playerDie3 = random.randint(1, 6)
                playerTotal += playerDie3
                print("You rolled a", playerDie3, "for a total of", playerTotal)
            elif roll in ("N", "NO"):
                print("You stayed on", playerTotal, "\n")
                break
            else:
                print("You must enter Y,YES,N or NO")

        # Dealer keeps rolling until they beat the player or bust
        if playerTotal <= 21:
            while dealerTotal <= playerTotal and dealerTotal <= 18:
                dealerDie3 = random.randint(1, 6)
                dealerTotal += dealerDie3
                print("The Dealer rolled", dealerDie3, "for a total of", dealerTotal)

        # Award the wager to the player closest to 21 without going over
        if playerTotal > 21:
            print("You busted, I'm so sorry\n")
            print("The dealer won this round, you've lost your $", wager, "wager")
            pot -= wager
        elif dealerTotal > 21:
            print("The dealer busted, you won $", wager)
            pot += wager
        elif dealerTotal > playerTotal:
            print("The dealer won this round, you've lost your $", wager, "wager")
            pot -= wager
        elif dealerTotal < playerTotal:
            print("Congratulation, you won $", wager)
            pot += wager
        elif dealerTotal == playerTotal:
            print("You tied the dealer, it's a push")

        print("\nYou now have $", pot, "in the pot")
        maxPot = max(maxPot, pot)
        rounds += 1

    # Players kept playing until the pot was empty
    print("You ran out of money")
    print("You played", rounds, "rounds. Your highest pot was", maxPot)

    # Ask if they want to play again or quit
    while True:
        play = input("\nDo you want to play again? (Y,YES,N,NO) ==> ").upper()
        if play in ("Y", "YES"):
            print()
            break
        elif play in ("N", "NO"):
            print("Thanks for playing. Bye")
            playing = False
            break
        else:
            print("You must enter Y,YES,N or NO")
