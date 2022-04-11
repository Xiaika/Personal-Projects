from random import choice
from Color import Color
from collections import Counter
from copy import deepcopy

def print_keyboard(keyboard):
    print('━━━━━━━━━━━━━━━━━━━━━━━━━')
    for key in keyboard:
        if key.letter == 'a':
            print()
            print(' ', end='')
        if key.letter == 'z':
            print()
            print('  ', end='')
        print(key.color + key.letter + '\033[0m', end='')
    print('\n')


def output_guesses(previous_guesses):
    print('\n' * 100)  # Clear the console
    for g in previous_guesses:
        for letter in g:
            print(letter.color + letter.letter + '\033[0m', end='')
        print()

#  Generate random valid word from a pool
#  Load words
with open('fixed_words.txt') as file:
    words = [word for word in file.read().splitlines()]

with open('wordle.txt') as file:
    valid_words = set(line.rstrip() for line in file)

#  TODO Blacklist words

#  Game loop
keep_playing = True
victories = 0
while keep_playing:
    word = list(choice(words).lower())
    letter_count = Counter(word)
    guesses = list()  # list to store guesses
    game_over = False
    keyboard = 'qwertyuiopasdfghjklzxcvbnm'
    keyboard_colored: list[Color()] = list()
    for character in keyboard:
        key_color = Color(character, 'white')
        keyboard_colored.append(key_color)
    guess_count = 0
    while not game_over:
        print_keyboard(keyboard_colored)
        guess_string = input('Enter a word: ')
        guess = list(guess_string.lower())
        valid_guess = True
        buffer_word = [Color() for i in range(5)]

        #  Validate guess
        if len(guess_string) != 5:
            error_message = 'Guess must be 5 letters'
            valid_guess = False
        if not guess_string.isalpha():
            error_message = 'Guess must contain letters only.'
            valid_guess = False
        #  Check if guess is a real word
        guess_letters = str(''.join(i for i in guess))
        if guess_letters not in valid_words:
            error_message = f'{guess_letters} is not a valid word.'
            valid_guess = False
        if not valid_guess:
            output_guesses(guesses)
            print(f'\033[1;38;{255};{255};{255}m {error_message} \033[0m')
            continue

        #  Yellow pass: indicate that a letter is in the wrong position
        for index_w, letter_w in enumerate(word):
            for index_g, letter_g in enumerate(guess):
                if letter_g == letter_w and index_w != index_g:
                    buffer_word[index_g] = Color(letter_g, 'yellow')

        #  Green Pass: indicate that a letter is correct
        index = 0
        for letter_g, letter_w in zip(guess, word):
            if letter_g == letter_w:
                buffer_word[index] = Color(letter_g, 'green')
            index += 1

        #  Cyan pass: indicate that a letter appears twice
        #  for index, letter in enumerate(guess):
        #    if letter in letter_count.keys():
        #        if letter_count[letter] > 1 and buffer_word[index].color != '\033[92m':
        #            buffer_word[index] = Color(letter, 'cyan')

        #  Red pass
        guess_letter_counter = Counter(guess_string)
        buffer_letters = [i.letter for i in buffer_word]
        for index, (letter_g, letter_w) in enumerate(zip(guess, word)):
            if buffer_letters[index] == '#':
                buffer_word[index] = Color(letter_g, 'red')
            # Check if all occurrences of a letter in the word were correct
            elif guess_letter_counter[letter_g] > letter_count[letter_g]:
                correct_occurrences = 0
                for letter in buffer_word:
                    if letter.letter == letter_g and letter.color == '\033[92m':
                        correct_occurrences += 1
                if buffer_word[index].color == '\033[93m':
                    if correct_occurrences == letter_count[letter_g]:
                        buffer_word[index] = Color(letter_g, 'red')
                    if letter_g in buffer_letters[index - 1::-1]:
                        buffer_word[index] = Color(letter_g, 'red')
        guesses.append(buffer_word)

        #  Update keyboard coloring
        cached_keyboard = deepcopy(keyboard_colored)
        for index, item in enumerate(buffer_word):
            for key in keyboard_colored:
                if item.letter == key.letter:
                    #  TODO fix bug with coloring keyboard red instead of green
                    if item.color == '\033[92m' or item.color == '\033[91m':
                        count = 0
                        for previous in buffer_word[index - 1::-1]:
                            if previous.letter == item.letter and previous.color != '\033[92m':
                                count += 1
                            if count == len(buffer_word[index - 1::-1]):
                                key.set_color(item.color)
                    if index == 0:
                        key.set_color(item.color)
                    elif item.letter not in buffer_letters[index - 1::-1]:
                        key.set_color(item.color)
                    else:
                        continue
        for key_cached, key_current in zip(cached_keyboard, keyboard_colored):
            if key_cached.color == '\033[92m':
                key_current.set_color('\033[92m')
            if key_cached.color == '\033[91m':
                key_current.set_color('\033[91m')

        #  Output the guess results
        output_guesses(guesses)
        guess_count += 1
        correct_letters = 0
        for letter_g, letter_w in zip(guess, word):
            if letter_g == letter_w:
                correct_letters += 1
        if correct_letters == 5:
            print(f"Congrats, you won in {guess_count} guesses.")
            victories += 1
            game_over = True

        elif guess_count == 6:
            string = ""
            string = string.join(word)
            print(f'Game Over. \n the word was {string}')
            print(f'You won {victories} games')
            print()
            game_over = True

    invalid = True
    while invalid:
        finished = input("Would you like to play again? Y/N  ").lower()
        if finished in ['y', 'yes', 'ya']:
            invalid = False
            keep_playing = True
        elif finished in ['n', 'no', 'nah']:
            invalid = False
            keep_playing = False
            print(f'You won {victories} games')
            break
        else:
            continue
    game_over = True

#  TODO GUI
