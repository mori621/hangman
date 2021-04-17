import random

def hangman():
    word_list = ["cat", "dog", "egg"]
    word = word_list[random.randint(0, 2)]
    wrong = 0
    stages = ["",
              "_________      ",
              "|              ",
              "|       |      ",
              "|       0      ",
              "|     / | \    ",
              "|       |      ",
              "|      / \     "
              ]
    rletters = list(word)
    broad = ["_"] * len(word)
    win = False
    print("welcome to hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            broad[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(broad))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in broad:
            print("you win!")
            print(" ".join(broad))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("you lose!")
        print("correct is {}".format(word))

hangman()
