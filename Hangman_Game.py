words=["watermelon","apple","mango","orange","banana"]
import random
random_word=random.choice(words)
guessed_letters=[]
wrong_guesses=0
while wrong_guesses<6:
    guess=input("Guess a letter:").lower()
    guessed_letters.append(guess)

    if guess in random_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses+=1
        
    word_guessed=True
    for letter in random_word:
        if letter in guessed_letters:
            print(letter,end=" ")
        else:
            print("_",end=" ")
            word_guessed=False
    print()

    if word_guessed:
        print("Congratulations! You guessed the word!")
        break

if wrong_guesses ==6:
    print("Game Over!")
    print("The word was:",random_word)
