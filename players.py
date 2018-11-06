
players = ['charles','martina','michael','florence','eli']
print(players[1])
print(players[3:6])
print(players[:6])
print(players[3:])
print(players[-3:])
print(players[-1:])
# ~ 打印所有的元素
print(players[:])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(" "+player.title())
