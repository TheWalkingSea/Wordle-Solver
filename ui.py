import os
import platform
from colorama import Fore
import re

class Red:
    def __init__(self, word) -> None:
        self.word = word
    
    def __str__(self) -> str:
        return Fore.RED + self.word

class Green:
    def __init__(self, word) -> None:
        self.word = word
    
    def __str__(self) -> str:
        return Fore.GREEN + self.word

class Yellow:
    def __init__(self, word) -> None:
        self.word = word
    
    def __str__(self) -> str:
        return Fore.YELLOW + self.word
        
def clrscrn():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        os.system("clear")
    else:
        assert False, "OS not supported"

class gamelogic:
    def __init__(self, CWord) -> None:
        self.CWord = CWord
        self.IWords = list()
    def makeGuess(self, guess: str):
        for index, letter in enumerate(guess):
            if letter == self.CWord[index]: yield Green(letter)
            elif letter not in self.CWord: yield Red(letter)
            else:
                duplicateLetters = len(re.findall(letter, self.CWord)) # How many var letter there is in CWord
                GreenGuess = len(list(filter(lambda x: x == letter, [l for i, l in enumerate(guess) if l == self.CWord[i]]))) # How many Green letters there are in guess
                YellowGuess = list(filter(lambda x: self.CWord[x] != guess[x], [i for i, l in enumerate(guess) if l in self.CWord and l == letter]))[:(duplicateLetters-GreenGuess)]
                if index in YellowGuess:
                    yield Yellow(letter)
                else:
                    yield Red(letter)
                # BOOTS CWORD 2 # [3]
                # IMOoO GUESS 1
                # 4 [4]
        # self.IWords.append(prettyGuess)
    def __str__(self) -> str:
        return "\n".join(["".join(map(str, i)) for i in self.IWords]) + Fore.RESET
        # return 0h


