import enum
import os
import sys
import colorama



class RED:
    def __init__(self, character):
        self.character = character
    def __str__(self):
        return colorama.Fore.RED + self.character
class YELLOW:
    def __init__(self, character):
        self.character = character
    def __str__(self):
        return colorama.Fore.YELLOW + self.character 
class GREEN:
    def __init__(self, character):
        self.character = character
    def __str__(self):
        return colorama.Fore.GREEN + self.character

class word:
    def __init__(self, word, answer):
        self.word = word
        self.answer = answer
        self.beutifword = list() # Each item is an object of RYG classes
    
    def parse(self):
        for index, letter in enumerate(self.word):
            if letter not in self.answer: self.beutifword.append(RED(letter))
            elif letter == self.answer[index]: self.beutifword.append(GREEN(letter))
            elif letter in self.answer and [i for i in self.beutifword if i.character != letter and isinstance(GREEN, type(i))]: self.beutifword.append(YELLOW(letter))
            else: self.beutifword.append(RED(letter)) # Duplicate letter
w = word("heels", "hello")
w.parse()
[print(i) for i in w.beutifword]
