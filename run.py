
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


title_text()