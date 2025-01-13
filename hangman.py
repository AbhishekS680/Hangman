import random

def randomWord():

    wordList = [
    "skibidi", "ohio", "rizzler", "diddy", "lebron", "sigma", "car", "house", "tree", "dog", "cat", "phone", "book", "laptop", "mouse", "keyboard",
    "table", "chair", "window", "door", "bottle", "pen", "pencil", "paper", "bag", "clock",
    "light", "fan", "bed", "shirt", "pants", "shoes", "hat", "glasses", "camera", "television",
    "radio", "speaker", "lamp", "candle", "flower", "garden", "grass", "stone", "river", "mountain",
    "ocean", "beach", "cloud", "sun", "moon", "star", "planet", "sky", "rain", "storm", "wind",
    "snow", "ice", "fire", "tree", "branch", "leaf", "root", "seed", "fruit", "bird", "fish",
    "insect", "animal", "farm", "city", "village", "road", "bridge", "train", "bus", "carriage",
    "plane", "airport", "ship", "harbor", "bicycle", "motorcycle", "helmet", "engine", "wheel",
    "path", "field", "forest", "desert", "cave", "hill", "valley", "lake", "pond", "island",
    "volcano", "earthquake", "tsunami", "hurricane", "tornado", "cliff", "waterfall", "spring", "geyser"
    ]

    chosenWord = random.choice(wordList)

    return chosenWord

def hangmanStages(x):
    if x == 0:
        return "  _______\n  |     |\n  |     \n  |\n  |\n  |\n__|__"
    if x == 1:
        return "  _______\n  |     |\n  |     O\n  |\n  |\n  |\n__|__"
    if x == 2:
        return "  _______\n  |     |\n  |     O\n  |    \\|/\n  |     \n  |\n__|__"
    if x == 3:
        return "  _______\n  |     |\n  |     O\n  |    \\|/\n  |     |\n  |\n__|__"
    if x == 4:
        return "  _______\n  |     |\n  |     O\n  |    \\|/\n  |     |\n  |    /\n__|__"
    if x == 5:
        return "  _______\n  |     |\n  |     O\n  |    \\|/\n  |     |\n  |    / \\\n__|__"

def errorCheck(input, lettersGuessed):
    try:
        if (ord(input) >= 123 or ord(input) <= 96):
            return True

        for i in lettersGuessed:
            if i == input:
                return "yessir"
    except:
        return True
    
def main():
    incorrectGuesses = 0
    correctGuesses = 0
    lettersGuessed = []
    print("Welcome to the Hangman game! You need to find the correct word, but you can only have 5 incorrect guesses. Good luck!")
    print("  _______\n  |     |\n  |     \n  |\n  |\n  |\n__|__")
    word = randomWord()
    hiddenWord = ["_"] * len(word)

    while incorrectGuesses < 5:
        print("\nWord: ", end="")
        print(" ".join(hiddenWord))
        print("Letters Guessed: ", end="")
        for i in lettersGuessed:
            print(i, end=" ")
        print()
        print(f"Incorrect Guesses: {incorrectGuesses}")
        userLetterGuess = input("\nPlease enter a single letter to guess: ").lower().strip()

        if (errorCheck(userLetterGuess, lettersGuessed) == "yessir"):
            print("ERROR! This letter has already been used, try again.")
            print(hangmanStages(incorrectGuesses))
            continue
        elif (errorCheck(userLetterGuess, lettersGuessed) == True):
            print("ERROR! Please enter a valid letter, try again.")
            print(hangmanStages(incorrectGuesses))
            continue
        lettersGuessed.append(userLetterGuess)

        if userLetterGuess in word:
            for i in range(len(word)):
                if userLetterGuess == word[i]:
                    hiddenWord[i] = userLetterGuess
            
            print(f"The letter {userLetterGuess} is in the word!")
            print(hangmanStages(incorrectGuesses))
            correctGuesses +=1


            if "".join(hiddenWord) == word:
                print(f"YOU WIN! :)\nThe word was {word}!")
                break
        else:
            print(f"Wrong, {userLetterGuess} is not in the word!")
            incorrectGuesses += 1

        if incorrectGuesses == 1:
            print(hangmanStages(1))
        if incorrectGuesses == 2:
            print(hangmanStages(2))
        if incorrectGuesses == 3:
            print(hangmanStages(3))
        if incorrectGuesses == 4:
            print(hangmanStages(4))
        if incorrectGuesses == 5:
            print(hangmanStages(5))

    if incorrectGuesses == 5:
        print(f"YOU LOSE!!! :(\nThe word was {word}")

if __name__ == '__main__':
    main()