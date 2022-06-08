import random


countries = ("Netherlands", "Switzerland", "Croatia", "Portugal",
             "Belgium", "Iceland", "Malaysia", "Vietnam", "Tanzania", "Slovakia")
disney_characters = ("SnowWhite", "Rapunzel", "Jasmine",
                     "Mowgli", "Aladin", "Simba", "DaisyDuck", )

print('''
                     _                                                  
                    | |                          _                      
         _ _ _  ____| | ____ ___  ____   ____   | |_  ___               
        | | | |/ _  ) |/ ___) _ \|    \ / _  )  |  _)/ _ \              
        | | | ( (/ /| ( (__| |_| | | | ( (/ /   | |_| |_| |             
         \____|\____)_|\____)___/|_|_|_|\____)   \___)___/              
                                                                        
 _     _                                                                
| |   | |                                                               
| |__ | | ____ ____   ____ ____   ____ ____      ____  ____ ____   ____ 
|  __)| |/ _  |  _ \ / _  |    \ / _  |  _ \    / _  |/ _  |    \ / _  )
| |   | ( ( | | | | ( ( | | | | ( ( | | | | |  ( ( | ( ( | | | | ( (/ / 
|_|   |_|\_||_|_| |_|\_|| |_|_|_|\_||_|_| |_|   \_|| |\_||_|_|_|_|\____)
                    (_____|                    (_____|                  

                                                    
''')

print("Choose a category to guess the word or phrase: \n")
print("1.) Countries          2.) Disney Characters\n")
category = input("Enter your choice: ")
print()

# function to generate a random word


def word_generator(category):
    if category == "countries" or category == "1":
        random_word = random.choice(countries)
        return random_word.upper()
    elif category == "disney_characters" or "2":
        random_word = random.choice(disney_characters)
        return random_word.upper()


word = word_generator(category)


def play_game(word):
    length = len(word)
    word_spaces = "_" * length
    guessed_letters = []

    attempts = 6
    print("Let's begin the game!\n")
    print(hangman_pics[attempts])
    print(f"Word contains {length} letters.")
    print()
    print(word_spaces)
    print()

    while attempts != 0:

        guess = input("Guess a letter: ").upper()
        print()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter\n")
            elif guess not in word:
                print("This letter is not in the word/phrase \n")
                attempts -= 1
                guessed_letters.append(guess)
            elif guess in word:
                print("This letter is in the word. Good job!\n")
                guessed_letters.append(guess)
                # to fill spaces with correct guess, first convert word_as_space to list(as list is mutable)
                word_as_list = list(word_spaces)
                # using enumerate to get the index of the particular letter(guess) and then storing it in a list named indices
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                # replacing the "_" at the correct index with the guessed letter
                for index in indices:
                    word_as_list[index] = guess
                    # convert back to a sring
                    word_spaces = "".join(word_as_list)
                print(word_spaces)

                if "_" not in word_spaces:
                    print(f"You won {word} is the word.\n")
                    break

        elif len(guess) > 1 and guess.isalpha():
            if guess != word:
                print("This is not the word. Wrong attempt.\n")
                attempts -= 1
            elif guess == word:
                print(f"You nailed it.{guess} is the word.\n")
                print("Congratulations! You WON!\n")
                break
        elif len(guess) >= 1 and guess.isnumeric():
            print("You must enter a letter\n")
            attempts -= 1
        else:
            print("Invalid guess\n")
            attempts -= 1
        print(hangman_pics[attempts])

        if attempts == 0:
            print("No more attempts left. You lost... May be next time! \n")
            print("The correct answer was: ", word)
            print()


hangman_pics = ['''  --------- |
                     |          O/
                     |         /|
                     |         / \ 
                     |
                     |
                     |
                     ------
                        GAME OVER! ''',

                '''
         - -------- |
         |          O/
         |         /|
         |         /
         |
         |
         |
         ------
        This is your Last Chance!
''',
                '''
         - -------- |
         |          O/
         |         /|
         |
         |
         |
         |
         ------
         Two more attempts left.,
''',
                '''
         - ------- |
         |         O
         |        /|
         |
         |
         |
         |
         ------,
''',
                '''
        - -------- |
         |         O
         |         |
         |
         |
         |
         |
         ------
''',
                '''

         - -------- |
         |          O
         |
         |
         |
         |
         |
         ------
''',
                '''
         - -------- |
         |
         |
         |
         |
         |
         |
         ------

''']

play_game(word)
