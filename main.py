from random_word import RandomWords


# Imported a random word generator from https://pypi.org/project/Random-Word/
# Hang man ascii art from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
# Colored terminal code https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
# Blanks and word guessing snippets https://inventwithpython.com/invent4thed/chapter8.html

HangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


r = RandomWords()
MaxLife = 6
Life = 0
Won = False
HintUsed = False
GuessedLetters = []
IncorrectLetters = []
print("Welcome to hangman")

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def NewGame():
    while True:
        Choice = input("Do you want to play the game again? (y/n):  ").lower()
        if Choice == "y" or  Choice == "yes" :
            HangmanMenu()
            break
        elif Choice == "n" or Choice == "no":
            exit()
        print("Please enter a valid input")



def Hint(GuessedLetters, randomWord):
    for i in randomWord:
        if not i in GuessedLetters:
            print('\033[94m' + "Here is your free word " + i + '\033[0m')
            break



def SinglePlayer(Life, MaxLife, Won, HintUsed, GuessedLetters, IncorrectLetters):
    while True:
        MaxCount = input("Please specify the amount of letters you want for your word (Can't be higher than 20 or less than 4):   ")
        try:
            val = int(MaxCount)
            if val > 20:
                MaxCount = 20
            elif val < 4:
                MaxCount = 4
            break;
        except ValueError:
            try:
                float(MaxCount)
                print("Input is an float number please specify a real number")
                break;
            except ValueError:
                print("This is not a number. Please enter a valid number")

    randomWord = (r.get_random_word(minLength = MaxCount, maxLength=MaxCount)).lower()
    Blanks = '_' * len(randomWord)
    while not Won and Life <= MaxLife:
        print(HangmanPics[Life])
        if IncorrectLetters:

            #IncorrectLetters = IncorrectLetters.sort()
            print('\033[95mGuessed letters: ',end='');
            for i in bubbleSort(IncorrectLetters):
                print(i, end=' ')
            print('\033[0m')
        else:
            print('\033[95mGuessed letters:\033[0m')
        if HintUsed == False:
            print("You haven't used your hint say hint to get one!")
        if Life == MaxLife:
            Won = False
            print("You lost, maybe next time!")
            print("The word was " + randomWord)
            NewGame()
        Guessed = input("Guess a letter or the word (" + str(MaxLife - Life) + " lives left):    ").lower()
        if Guessed == randomWord:
            Won = True
            print("Congrats you won!")
            NewGame()
        Correct = False
        for i in range(len(randomWord)):
            if Guessed == randomWord[i]:
                Correct = True
                GuessedLetters.insert(i, Guessed)
                Blanks = Blanks[:i] + Guessed + Blanks[i + 1:]

        if not Correct and Guessed != "hint":
            Life += 1
            IncorrectLetters.insert(i, Guessed)
        elif Guessed == "hint" and not HintUsed:
            HintUsed = True
            Hint(GuessedLetters, randomWord)
        elif Guessed == "hint" and HintUsed:
            print("You have already used your hint guess again")
        if Blanks == randomWord:
            for i in Blanks:
                print(i, end=' ')
            print()
            print("Congrats you won!")
            NewGame()
        for i in Blanks:
            print('\033[92m'+i + '\033[0m', end=' ')



def MultiPlayer(Life, MaxLife, Won, HintUsed, GuessedLetters, IncorrectLetters):
    randomWord = input("Player 1 please input a word for Player 2 to guess:   ").lower()
    print('\n' * 5000)
    print("Do not scroll up otherwise you are cheating")
    Blanks = '_' * len(randomWord)
    while not Won and Life <= MaxLife:
        print(HangmanPics[Life])
        if IncorrectLetters:

            #IncorrectLetters = IncorrectLetters.sort()
            print('\033[95mGuessed letters: ',end='');
            for i in bubbleSort(IncorrectLetters):
                print(i, end=' ')
            print('\033[0m')
        else:
            print('\033[95mGuessed letters:\033[0m')
        if HintUsed == False:
            print("You haven't used your hint say hint to get one!")
        if Life == MaxLife:
            Won = False
            print("You lost, maybe next time!")
            print("The word was " + randomWord)
            NewGame()
        Guessed = input("Guess a letter or the word (" + str(MaxLife - Life) + " lives left):    ").lower()
        if Guessed == randomWord:
            Won = True
            print("Congrats you won!")
            NewGame()
        Correct = False
        for i in range(len(randomWord)):
            if Guessed == randomWord[i]:
                Correct = True
                GuessedLetters.insert(i, Guessed)
                Blanks = Blanks[:i] + Guessed + Blanks[i + 1:]
        if not Correct and Guessed != "hint":
            Life += 1
            IncorrectLetters.insert(i, Guessed)
        elif Guessed == "hint" and not HintUsed:
            HintUsed = True
            Hint(GuessedLetters, randomWord)
        elif Guessed == "hint" and HintUsed:
            print("You have already used your hint guess again")
        if Blanks == randomWord:
            for i in Blanks:
                print(i, end=' ')
            print()
            print("Congrats you won!")
            NewGame()
        for i in Blanks:
            print('\033[92m' + i + '\033[0m', end=' ')



def HangmanMenu():
    while True:
        MenuChoice = input("Please choose from the menu:\n1. Single Player Hangman\n2. Two Player Hangman\n3. Exit Hangman  ")
        try:
            val = int(MenuChoice)
            if val == 1:
                SinglePlayer(Life, MaxLife, Won, HintUsed, GuessedLetters, IncorrectLetters)
                break
            elif val == 2:
                MultiPlayer(Life, MaxLife, Won, HintUsed, GuessedLetters, IncorrectLetters)
                break
            elif val == 3:
                exit()
            else:
                print("Not an option in the menu try again")
        except ValueError:
            try:
                float(MenuChoice)
                print("Not an option in the menu try again")
                break;
            except ValueError:
                print("Not an option in the menu try again")




HangmanMenu()











