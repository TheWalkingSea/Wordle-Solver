import colorama
import platform
import os
import re

class Red():
    def __init__(self, letter) -> None:   
        self.letter = letter
    def __str__(self) -> str:
        return colorama.Fore.RED + self.letter

class Green():
    def __init__(self, letter) -> None:
        self.letter = letter
    def __str__(self) -> str:
        return colorama.Fore.GREEN + self.letter

class Yellow():
    def __init__(self, letter) -> None:
        self.letter = letter
    def __str__(self) -> str:
        return colorama.Fore.YELLOW + self.letter

def clearscreen():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() in ["Linux", "Darwin"]:
        os.system("clear")
    else:
        assert False, ("Not supported", platform.system())

class Guess():
    def __init__(self, cword, guess) -> None:
        self.correctWord = cword
        self._guess = guess
        
    @property
    def guess(self):
        for index, letter in enumerate(self._guess):
            if letter == self.correctWord[index]: print(Green(letter), index, "green")
            elif letter not in self.correctWord: print(Red(letter), index, "red")
            else: print(len(re.findall(letter, self.correctWord)))
        return 0
    
class GLogic:
    def __init__(self, word) -> None:
        super().__init__(word)
        self.correctWord = word.lower()




if __name__ == "__main__":
    e = Guess("hello", "lmaoe")
    e.guess