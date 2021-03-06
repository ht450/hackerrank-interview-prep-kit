from functools import cmp_to_key


class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name > b.name:
                return 1
            else:
                return -1
        else:
            return -1


data = []
n = 5
input = [
    ['amy', 100],
    ['david', 100],
    ['heraldo', 50],
    ['aakansha', 75],
    ['aleksa', 150],
]
for i in range(n):
    name, score = input[i][0], input[i][1]
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
