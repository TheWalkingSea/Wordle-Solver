import ui
import json
import random

with open("validwords.json", "r") as f:
    WORDS = json.load(f)
CWORD = WORDS[random.randint(a=0, b=12973)].lower()

UI = ui.gamelogic(CWord=CWORD)

def getNextGuess():
    pass


def main():
    counter = 1
    while True:
        if counter > 6:
            print("You couldn't guess the word in time, the word was {}".format(CWORD))
            break
        else:
            word = getNextGuess().lower()
        
            if len(word) == 5:
                g = guess(word)
                ui.clrscrn()
                print(UI)
                if len(list(filter(lambda x: isinstance(x, ui.Green), g))) == 5: 
                    print("You got the word!")
                    break
                counter += 1
            elif len(word) != 5:
                print("Word not 5 letters")
                continue
            elif word not in WORDS:
                print("Not Valid Word")
                continue

def guess(g: str) -> list:
    colorGuess = list(UI.makeGuess(g))
    UI.IWords.append(colorGuess)
    return colorGuess
    

if __name__ == "__main__":
    main()