def open_screen():
    """print the game's opening screen"""
    print("""
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                        |___/
       Welcome to the game Hangman!                 
    """)


def check_win(secret_word, old_letters_guessed):
    """
    this function returns True if the secret word guessed,
    meanning all the letters in param old_letters_guessed are == secret_word.
    :param secret_word: the secret word
    :param old_letters_guessed: a list of letters
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: True or False
    """
    i = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            i.append(letter)
            i.sort()
    e = []
    e[:0] = secret_word
    e.sort()
    if i == e:
        return True
    else:
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    shows the letters guessed in secret word
    :param secret_word: the secret word
    :param old_letters_guessed: a list of letters
    :type secret_word: str
    :type old_letters_guessed: list
    """
    i = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            i.append(letter + ' ')
        else:
            i.append('_ ')
    i = ''.join(i)
    i = i.strip()
    print(i)


def check_valid_input(letter_guessed, old_letters_guessed):
    """this function will check the users input, and return True only if:
    1. it is a single letter.
    2. it is an alphabet letter.
    3. it wasn't being guessed before.
    else it will return False."""
    turn_to_lower = letter_guessed.lower()
    str_length = len(letter_guessed)
    only_alphabet = turn_to_lower.isalpha()
    if str_length > 1:
        return False
    elif not only_alphabet:
        return False
    elif turn_to_lower in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed: users input
    :param old_letters_guessed: the letters already guessed
    """
    old_letters_guessed.sort()
    reminder_list = " -> ".join(old_letters_guessed)
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(reminder_list)
        return False


def choose_word(file_path, index):
    with open(file_path, "r") as words_file:
        content_as_list = words_file.read().split(' ')
        unique_words = []
        for item in content_as_list:
            if item not in unique_words:
                unique_words.append(item)
        length_of_unique = len(unique_words)
        length_of_original = len(content_as_list)
        if index <= length_of_original:
            chosen = content_as_list[index - 1]
        else:
            chosen = content_as_list[index % length_of_original - 1]
        return chosen


def main():
    open_screen()

    file_path = input("Enter file path: ")

    word_index = int(input("Enter index: "))

    print("Let's start!")

    print("    x-------x")

    with open(file_path) as file_content:
        list_of_words = file_content.read().split(' ')
        secret_word = list_of_words[word_index]
        print(secret_word)

    print("_ " * len(secret_word))

    letter = input("Enter a letter: ")
    old_letters_guessed = []
    MAX_TRIES = 6
    num_of_tries = len(old_letters_guessed)
    HANGMAN_PHOTOS = {
        1: """x-------x
    |
    |
    |
    |
    |""",
        2: """x-------x
    |       |
    |       0
    |
    |
    |""",
        3: """x-------x
    |       |
    |       0
    |       |
    |
    |""",
        4: """x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
        5: """x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
        6: """x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
    }

    while num_of_tries < MAX_TRIES:
        #option for invalid selection
        if not check_valid_input(letter, old_letters_guessed):
            try_update_letter_guessed(letter, old_letters_guessed) == False
            letter = input("Enter a letter: ")
        #option for valid but wrong selection
        elif check_valid_input(letter, old_letters_guessed) and letter not in secret_word:
            old_letters_guessed.append(letter)
            print(":(")
            print(HANGMAN_PHOTOS[num_of_tries + 1])
            num_of_tries += 1
            letter = input("Enter a letter: ")
        #option for correct letter
        else:
            old_letters_guessed.append(letter)
            show_hidden_word(secret_word, old_letters_guessed) 
            if not check_win(secret_word, old_letters_guessed):
                letter = input("Enter a letter: ")
            else:
                print("WIN")
                break
    if num_of_tries == MAX_TRIES:
            print(":(")
            print(HANGMAN_PHOTOS[num_of_tries])
            print("LOSE")
    #elif check_win(secret_word, old_letters_guessed):
      #  print("WIN")    
    
if __name__ == "_main_":
    main()

C:\Users\aviv8\PycharmProjects\HangmanGame\wordsForGame.txt