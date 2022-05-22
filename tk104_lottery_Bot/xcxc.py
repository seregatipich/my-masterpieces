import random

win = []
game = [1, 2, 3, 4, 5]
for i in range(0, 3):
    index = random.randint(0, len(game) - 1)
    win.append(game[index])
    del game[index]

print(win)
