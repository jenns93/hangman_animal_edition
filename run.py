import random
word_dic = {
    "easy": [
        "cat",
        "dog",
        "pig",
        "fish",
        "bear",
        "rat",
        "bee",
        "wasp",
        "sheep",
        "goat",
        "duck",
        "eagle",
        "tiger",
        "mouse",
        "lion",
    ],
    "med": [
        "horse",
        "rabbit",
        "lizard",
        "ostrich",
        "seagull",
        "giraffe",
        "chicken",
        "hyena",
        "gorilla",
        "monkey",
        "zebra",
        "moose",
        "cheetah",
        "dragonfly",
        "dolphin",
    ],
    "hard": [
        "crocodile",
        "hippopotamus",
        "mongoose",
        "tortoise",
        "antelope",
        "elephant",
        "chimpanzee",
        "platypus",
        "kangaroo",
        "wallaby",
        "aardvark",
        "rhinoceros",
        "woodpecker",
        "salamander",
        "chinchilla",
    ],
}
hangman = [
    " ______\n",
    ".     |\n.     |\n______|\n",
    "______\n.     |\n.     |\n.     |\n.     |\n______|\n",
    "______\n |    |\n.     |\n.     |\n.     |\n______|\n",
    "______\n |    |\n O    |\n.     |\n.     |\n______|\n",
    "______\n |    |\n O    |\n |    |\n.     |\n______|\n",
    "______\n |    |\n O    |\n/|    |\n.     |\n______|\n",
    "______\n |    |\n O    |\n/|\   |\n.     |\n______|\n",
    "______\n |    |\n O    |\n/|\   |\n/     |\n______|\n",
    " _______\n |     |\n O     |\n/|\    |\n/ \    |\n_______|\n",
]
guess_data_lists = {"wrong": [], "correct": [], "word_to_guess": [], "guess_results": [], }


def title_text():
    """
    Prints game title and prompts player to start playing
    """
    print("Let's Play Hangman!\nAnimal edition")
    play_game = input("Type 'play' to start!\n")
    while play_game != "play":
        print("Please enter a valid option")
        play_game = input("Type 'play' to start!\n")
    else:
        print("Let's go!")
        difficulty_selection()


def difficulty_selection():
    """
    Select diffuclty from easy/med/hard
    """
    select_difficulty = input("Choose a difficulty easy/med/hard:\n")
    while select_difficulty not in word_dic:
        print("Please enter a valid option")
        select_difficulty = input("Choose a difficulty easy/med/hard:\n")
    else:
        print(f"You selected: {select_difficulty}")
        word_to_guess = guess_data_lists["word_to_guess"]
        word_to_guess = random.choice(word_dic[select_difficulty])
        input_checker(word_to_guess)


def input_checker(word_to_guess):
    """
    Updates correct/inccorect letter lists and prints the main body of the game
     (hangman picture/word to guess/wrong answers)
    """
    i = 0
    set_of_word = set(word_to_guess)
    length_of_set = len(set_of_word)
    while i < 9:
        letter_input = input("Please enter a letter: ")
        if not letter_input.isalpha() or len(letter_input) > 1:
            print("Invalid! Please try again:")
        elif letter_input in guess_data_lists["correct"]:
            print(f"You have already tried: {letter_input}")
        else:
            if letter_input in word_to_guess:
                print(f"correct {letter_input} is in the word \n")
                if letter_input not in guess_data_lists["correct"]:
                    guess_data_lists["correct"].append(letter_input)
                if length_of_set == len(guess_data_lists["correct"]):
                    print(f"!! WINNER !!\n the word was {word_to_guess}")
            else:
                print(f"unlucky the word does not contain {letter_input}\n")
                if letter_input not in guess_data_lists["wrong"]:
                    guess_data_lists["wrong"].append(letter_input)
                    i += 1
                    print(hangman[i])
                elif letter_input in guess_data_lists["wrong"]:
                    print(f"You have already tried: {letter_input}")
                print(f"wrong answers {i}")
            if i >= 9:
                print(f"!! GAME OVER !!\nthe word was\n{word_to_guess}")


title_text()