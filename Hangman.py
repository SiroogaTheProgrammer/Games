import random

print("Hangman")
print("Loading contents...")

hardness_levels = ["3", "H", "M", "E", "VH"]
global_Variables = []

three_letter_words = ["cat", "dog", "hat", "bat", "run", "box", "sky", "car", "cup", "pie", "tap", "map", "pen", "fox", "red", "man", "sun", "win", "sea", "hot"]

easy_words = ["tree", "bird", "cake", "desk", "frog", "moon", "lamp", "fish", "book", "rose", "sand", "fire", "rain", "coat", "door", "ball", "star", "milk", "bear", "ring"]

medium_words = ["apple", "happy", "green", "table", "watch", "river", "plant", "smile", "hello", "mouse", "quiet", "juice", "beach", "happy", "horse", "peace", "grape", "tiger", "lemon", "music"]

hard_words = ["wonder", "chance", "yellow", "guitar", "butter", "banana", "circle", "bottle", "puzzle", "dragon", "summer", "rocket", "purple", "blossom", "planet", "sunset", "mirror", "smooth", "penguin", "potion"]

very_hard_words = ["exaggerate", "breathtaking", "catastrophe", "deliciously", "extraordinary", "fascinating", "happiness", "innovation", "labyrinth", "magnificent", "necessity", "overwhelming", "perpendicular", "quintessential", "ridiculous", "sensational", "tremendous", "unbelievable", "vulnerable", "wonderful"]

heart_num = 5

gameList = []

print("Ready")

lvl_key = True

print("Difficulty level")
print("3 letter (3)")
print("Easy (E)")
print("Medium (M)")
print("Hard (H)")
print("Very Hard (VH)")

while lvl_key:
    diff_lvl = input()
    if(diff_lvl not in hardness_levels):
        print(diff_lvl + " is not a difficulty level")
    else:
        global_Variables.append(diff_lvl)
        lvl_key = False

if(global_Variables[0] == "3"):
    gameList = three_letter_words
elif(global_Variables[0] == "E"):
    gameList = easy_words
elif(global_Variables[0] == "M"):
    gameList = medium_words
elif(global_Variables[0] == "H"):
    gameList = hard_words
elif(global_Variables[0] == "VH"):
    gameList = very_hard_words

word = []
invisible_word = []
lettersGuessed = []

for char in random.choice(gameList):
    word.append(char)
    invisible_word.append("*")

game_key = True

alphabet = [chr(ord('a') + i) for i in range(26)]

while game_key:
    print(invisible_word)
    print(lettersGuessed)
    print("\u2764\uFE0F " * heart_num)
    playerGuess = input("Your guess: ")

    if(playerGuess not in alphabet):
        print("invalid input")
    elif(playerGuess not in word):
        print("Nope, this letter is not in the word")
        heart_num -= 1
        lettersGuessed.append(playerGuess)
        if (heart_num <= 0):
            print("YOU LOST")
            print("The word was " + "".join(word))
            game_key = False
            break
    elif(playerGuess in word):
        print("This letter is in the word")
        invisible_word[word.index(playerGuess)] = playerGuess
        if("*" not in invisible_word):
            print("YOU WIN")
            print("The word was " + "".join(word))
            game_key = False
            break
