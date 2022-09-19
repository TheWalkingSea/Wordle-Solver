import json
import string
with open("validwords.json", "r") as f:
    WORDS = json.load(f)
count = dict()
for letter in string.ascii_lowercase:
        count[letter] = [0, 0, 0, 0, 0]
for word in WORDS:
    for index, letter in enumerate(word):
        count[letter][index] += 1


maxNumber = [("a", 0), ("a", 0), ("a", 0), ("a", 0), ("a", 0)]
for key, value in count.items():
    for index, item in enumerate(value):
        letter, num = (key, value)
        if maxNumber[index][1] < item:
            maxNumber[index] = (key, item)
print(count)
print(maxNumber)

