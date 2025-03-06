# Hangman game
import random
from wordlist import words

hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/|  ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}

def display_man(wrong_gusses):
    print("*************")
    for line in hangman_art[wrong_gusses]:
        print(line)
    print("*************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_gusses = 0
    is_running = True
    guessed_latter = set()
    

    while is_running:
        display_man(wrong_gusses)
        display_hint(hint)
        guess = input("Enter Your Guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess")
            continue

        if guess in guessed_latter:
            print(f"{guess} is already guessed")
            continue

        guessed_latter.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_gusses += 1

        
        if "_" not in hint:
            display_man(wrong_gusses)
            display_answer(answer)
            print("You Won!!")
            is_running = False
        elif wrong_gusses >= len(hangman_art) - 1:
            display_man(wrong_gusses)
            display_answer(answer)
            print("You Loose!!")
            is_running = False

if __name__ == '__main__':
    main() 