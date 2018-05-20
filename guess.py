
import random

#number is equal to a random integer between 1 and 100.
number = random.randint(1, 100)
running = True
#name variable is set to the string that the user inputs (ideally there name).
name =  input("What is your name? ")

#introduces game to player.
print("You have to guess my number it's between 1 and 100, Best of Luck {0}".format(name))

#main code block of game, continues to ask this question until they get it correct.
while running:
    guess = int(input("""   What is your guess?
    {0} guessed: """.format(name)))

#tell player if they are correct then ends the script.
    if guess == number:
        print("""\n        That is correct! 
        {0} has won the game, Congratulations!
        
        I hope you play again soon!""".format(name))
        break
#tells player if their guess is too low and gives a hint.
    elif guess < number:
        print("""\n        Incorrect.
        Sorry {0}, but you are wrong.
        Please feel free to try again!
        
        Here is a hint, the number is higher than what you guessed.
        """.format(name))
#tells player if their guess is too high and gives a hint.
    else:
        print("""\n        Incorrect.
        Sorry {0}, but you are wrong.
        Please feel free to try again!
        
        Here is a hint, the number is lower than what you guessed.
        """.format(name))
