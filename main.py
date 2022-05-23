
import random

word_list = ["PASTA", "PLANT", "FRIED", "SMART", "DRINK", "LATER", "FIRST", "STRAP", "LOCAL", "APPLE", "CANDY", "TIGER"]
GREEN = '\033[92m' #'\033[42m'
YELLOW = '\033[93m' #'\033[43m'
PLAIN = '\033[0m'
UNDERLINE = '\033[4m'


def checkword(guess, answer):
    # Checks the guess against the answer
    results = []

    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            results.append(GREEN)
        elif letter in answer:
            results.append(YELLOW)
        else:
            results.append(PLAIN + UNDERLINE)
        results[i] = results[i] + guess[i]

    return (PLAIN + " ").join(results)

def guessinput():
    # Gets user input and checks it's the right length
    guess = input(PLAIN + "Enter your 5 Letter Guess:\n")

    while len(guess) != 5:
        guess = input(PLAIN + "Sorry your guess isn't 5 Letters, please try again\n" + "Enter your 5 Letter Guess:\n")

    return guess.upper()

# Main Loop
if __name__ == '__main__':

    numguesses = []
    x = 0
    maxguesses = 5
    ans = random.choice(word_list)

    while x < maxguesses:
        usrguess = guessinput()
        output = checkword(usrguess, ans)
        numguesses.append(output + PLAIN)
        print(PLAIN + "\n".join(numguesses))
        if usrguess == ans:
            print(PLAIN + "Congratulations You Won!\nThe word was: " + GREEN + ans + PLAIN)
            exit()
        x += 1

    print(PLAIN + "Sorry you're out of guesses.\nThe answer was: " + GREEN + ans + PLAIN)





