import random

def unique_string(string):
    a = len(string)
    for x in range(a):
        for i in range(a - x - 1):
            if string[x] == string[x + i + 1]:
                return False
    return True

def main():
    print("Welcome to Mastermind.")
    print("Do you know how to play (y/n)?")
    tutorial = input(">")

    if tutorial == "n":
        print("In this game you are trying to find the hidden number combination.\nEvery number in the combination is only used once.\nIf you guess a correct number in the wrong space the 'close' count will go up by one.\nIf you guess a correct number in the correct space the 'match' count will go up one.")
    
    clear = True
    while clear:
        print("How many digits do you want the combination to be? (Between 2 and 9)")
        digits = input(">")
        print("How many guesses do you want to have? (Enter 0 for unlimited)")
        guesses = input(">")

        try:
            digits = int(digits)
            guesses = int(guesses)

            if digits >= 2 and digits <= 9:
                clear = False
            else:
                print("The game can only be played with between 2 and 9 digits.")
                pass
        except:
            print("Please answer both questions with a number.")
            pass
    
    if guesses == 0:
        guesses -= 1

    combo = []
    for _ in range(digits):
        while True:
            x = random.randint(0, 9)
            if x not in combo:
                combo.append(x)
                break

    win = False
    print("Hidden combination generated. Good luck!")
    while guesses != 0:

        if guesses > 0:
            print("You have", guesses, "guesses left.")

        temp = []
        match = 0
        close = 0

        guess = input("Guess >")

        try:
            int(guess)
            valid = True
        except:
            valid = False

        if unique_string(guess) and len(guess) == digits and valid:

            for x in range(len(guess)):
                if int(guess[x]) == combo[x]:
                    match += 1
                else:
                    temp.append(guess[x])

            for x in temp:
                if int(x) in combo:
                    close += 1

            if match == digits:
                win = True
                break

            print("Close:", close, ", Match: ", match)
            guesses -= 1

        else:
            print("You guess has to be a", digits, "digit number combination using each number only once.")

    if win:
        print("Congragulations! You guessed the secret number combination!")
    else:
        print("Sorry, you ran out of guesses. Better luck next time!")

main()