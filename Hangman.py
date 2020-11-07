import random
# import countries_and_capitals.txt
countries_and_capitals = ['Poland', 'Warsaw', 'Germany', 'Berlin', 'Czechrepublic', 'Prague', 'Slovakia', 'Bratislava', 'Ukraine', 'Lviv', 'Russia', 'Moscow','Lithuania', 'Vilnius','Belarus', 'Minsk']

def gimmie_word():
    word = random.choice(countries_and_capitals).upper()
    return word

# The program allows to play the game on different levels.
# The game starts with a menu for picking a difficulty level. You should not change the play() function, though!
# The word-pool and the number of lives depend on the chosen level
def menu(word):
    print("Welcome to Hangman!")
    while True:
        level = input("Pick a difficulty level: (1)easy (2)medium (3)hard: ")
        if level == "1":
            lives = len(word) + 2
            print(f"You picked level easy - you have {lives} tries")
            return lives
        elif level == "2":
            lives = len(word)
            print(f"You picked level medium - you have {lives} tries")
            return lives
        elif level == "3":
            lives = len(word) - 2
            print(f"You picked level hard - you have {lives} tries")
            return lives
        else:
            print("You did't select valid level")
# Implement the play(word, lives) function as a basic hangman game.
# The function uses its parameter word as the word to guess and lives to as the number of available mistakes
def play(word, lives):
    # The initial game state is displayed as _ _ _ _ _ _ _ _ (one underscore for each letter in word)
    word_list = list(word)
    user_word_list = []
    for l in word:
        user_word_list.append('_')
    user_guesses_list = []
    while lives > 0:
        user_word = ' '.join(user_word_list)
        print(user_word)
        guess = input('Please guess a letter (or "Quit"): ').upper()
        if len(guess) == 1 and guess.isalpha():
        # When a guess is repeated (regardless of its occurrences), the player is notified, and nothing happens
            if guess in user_guesses_list:
                print("You've already tried this letter. Try another.")
        # The game state is displayed as _ o d _ _ o o _ if letters 'd' and 'o' have been revealed
        # It is possible to make guesses, and letters that occur in the word are revealed
            elif guess in word:
                user_guesses_list.append(guess)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for i in indices:
                    user_word_list[i] = guess
                    user_word = " ".join(user_word_list)
        # The player wins when all the letters in word have been revealed
                    if user_word_list == word_list:
                        print("Congratulations! You won!")
                        break
        # When a guessed letter does not occur in word, the player loses one life
        # When a guess is wrong (either a new or a repeated letter), the already tried missing letters are shown to the user
            elif guess not in word:
                user_guesses_list.append(guess)
                lives -= 1
                print("You've already tried these letters:" + str(user_guesses_list))
                if lives > 0:
                    print(f"You have {lives} more tries left.")
        # The player loses when misses a letter for the livesth time (not counting repeated guesses)
                elif lives == 0:
                    print('You are out of lives. You lose.')
                    print(f'The word to guess was: {word}.')
        # When the player types 'quit' as input, the program says good-bye and terminates
            elif guess == 'Quit':
                print('Good bye')
                break
        else:
            print("Not a valid guess. Try again")


def game():
    word = gimmie_word()
    lives = menu(word)
    play(word, lives)

game()
