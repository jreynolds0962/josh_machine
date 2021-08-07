# 1. import random module and system
# 2. welcome user to game
# 3. ask user if they want to play the slots
# 4. print to user the rules of the game
# 5. initalize coin system
# 6. let user play slots
# 7. ask user how much they want to bet( no more than 50 coins at a time)
# 7 if user wins, they win double what they put in
# 8. if user loses, they lose the same amount they put in


#1.
import random, sys
from time import sleep

slots = ["DING", "7", "JOKER"]


#2
while True:
    print("Welcome to the slots!")

    health = 100

    #3.
    while True:
        ready = input("Are you ready to play the slots?: (y/n) ")
        if ready.lower() == 'n' or ready.lower() == 'no':
            sys.exit()
        elif ready.lower() == 'yes' or ready.lower() == 'y':
            print("Let's play!")
            break
        elif ready.lower() == "yerr" or ready.lower() == 'yup':
            print("Let's get to this money!! ")
            break
        else:
            print("something went wrong")
            continue

    while True:

        if health == 0:
            print("GAME OVER")
            break

        print("""Rules:  
        1. Bet an amount less than or equal to your health
        2. Win health/lose health""")
        print(f"You are at {health} health")
        answer = int(input("how much do you want to bet?: (0 to quit) "))

        if answer == 0:
            sys.exit()
        elif answer > health or answer < 0:
            print("This amount is not valid, please put an amount greater than 0 and less than your health:", health)
            continue
        else:
            print(f"You bet {answer} points of health")

            health -= answer
            spin1 = random.choice(slots)
            spin2 = random.choice(slots)
            spin3 = random.choice(slots)
            print(spin1, end=" ")
            sleep(1.3)
            print(spin2, end=" ")
            sleep(1.3)
            print(spin3)
            sleep(1.5)

            while True:
                if spin1 == spin2 == spin3:
                    health += 3 * answer
                    print("You won!")
                    break
                else:
                    print("This was a bust!")
                    sleep(1.5)
                    break

