# import random
# import time
# import matplotlib.pyplot as plt
# onex = 500
# threex = 0
# fivex = 0
# tenx = 0
# redx = 0
# _sum = 3000
# max = _sum
# rounds = 1
# means = list()
# tests = 0
# meantotalrounds = list()
# while True:
#     num = random.randint(1, 25)
#     if num <= 12:
#         _sum += onex - threex - fivex - tenx - redx
#     elif num <= 18:
#         _sum += threex*2 - onex - fivex - tenx - redx
#     elif num <= 22:
#         _sum += fivex*4 - onex - threex - tenx - redx
#     elif num <= 24:
#         _sum += tenx*9 - onex - threex - fivex - redx
#     elif num <= 25:
#         _sum += random.randint(1, 9)*redx - onex - threex - fivex - tenx
#     rounds += 1
#     # print(num)
#     # print(_sum, num)
#     # input()
#     if _sum > max: max = _sum
#     if _sum <= 0 and tests < 10000:
#         tests += 1
#         means.append(max)
#         meantotalrounds.append(rounds)
#         plt.plot(tests, _sum)
#         # print(f"{rounds}, {max}: You lost")
#         _sum = 3000
#         rounds = 1
#         max = 3000
#     elif _sum <= 0:
#         plt.show()
#         # time.sleep(.5)
#         print((sum(means)/len(means), sum(meantotalrounds)/len(meantotalrounds)))
#         tests = 0
#         means = list()
#         meantotalrounds = list()
#         _sum = 3000
#         rounds = 1
#         max = 3000


import random
import time
import matplotlib.pyplot as plt
onex = 500
threex = 0
fivex = 0
tenx = 0
redx = 0
_sum = 3000
round = 0
max = _sum
x = list()
y= list()
while True:
    num = random.randint(1, 25)
    if num <= 12:
        _sum += onex - threex - fivex - tenx - redx
    elif num <= 18:
        _sum += threex*2 - onex - fivex - tenx - redx
    elif num <= 22:
        _sum += fivex*4 - onex - threex - tenx - redx
    elif num <= 24:
        _sum += tenx*9 - onex - threex - fivex - redx
    elif num <= 25:
        _sum += random.randint(1, 9)*redx - onex - threex - fivex - tenx
    # print(num)
    round += 1
    x.append(round)
    y.append(_sum)
    # input()
    if _sum > max: max = _sum
    if _sum <= 0:
        print(f"{round}, {max}: You lost")
        plt.plot(x, y)
        plt.show()