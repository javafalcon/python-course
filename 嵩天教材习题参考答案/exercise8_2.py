from random import random
from random import randint
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
def getInputs():
    g1 = eval(input("请输入球队A的投篮能力值(0-1): "))
    b1 = eval(input("请输入球队A的篮板能力值(0-1): "))
    g2 = eval(input("请输入球队B的投篮能力值(0-1): "))
    b2 = eval(input("请输入球队B的篮板能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    return g1, b1, g2, b2, n
def simNGames(n, goleA, boardA, goleB, boardB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(goleA, boardA, goleB, boardB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB
def gameOver(t):
    return t > 12*60
def simOneGame(goleA, boardA, goleB, boardB):
    scoreA, scoreB = 0, 0
    serving = 0 #0: 代表A队发球，1：代表B队发球
    totalTime = 0
    while not gameOver(totalTime):
        t = randint(1, 24)
        totalTime += t
        if t == 24:
            serving = (serving + 1)%2
        else:
            if serving == 0:
                if random() < goleA:
                    scoreA += 1
                    serving = 1
                else:
                    if random() < boardA:
                        serving=0
                    else:
                        serving = 1
            else:
                if random() < goleB:
                    scoreB += 1
                    serving = 0
                else:
                    if random() < boardB:
                        serving = 1
                    else:
                        serving=0
    return scoreA, scoreB
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))
def main():
    printIntro()
    goleA, boardA, goleB, boardB, n = getInputs()
    winsA, winsB = simNGames(n, goleA, boardA, goleB, boardB)
    printSummary(winsA, winsB)
main()

