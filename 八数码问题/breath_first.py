# 盲目搜索之宽度优先搜索算法
from Node import *


class breadth_search:
    def __init__(self, originalNode, targetNode, MaxDegree, length):
        self.originalNode = originalNode
        self.targetNode = targetNode
        self.open = [self.originalNode]
        self.close = []
        self.spce = [-3, 3, -1, 1]  # 上下左右四个移动方向
        self.MaxDegree = MaxDegree  # 深度限制，到达此深度未找到便返回
        self.length = length
        self.step = 0

    # 判断是否可达，通过求逆序数
    def hasSolve(self):
        targetVer = self.getreVersNum(self.targetNode.state)
        originalVer = self.getreVersNum(self.originalNode.state)
        if(targetVer % 2 != originalVer % 2):
            return False
        else:
            return True

    # 获取逆序数
    def getreVersNum(self, state):
        sum = 0
        for i in range(0, len(state)):
            if(state[i] == 0):
                continue
            else:
                for j in range(0, i):
                    if(state[j] > state[i]):
                        sum += 1
        return sum

    def copyArray(self, state):
        arr = []
        return arr + state

    def isInTable(self, node, table):
        for i in table:
            if i.state == node.state:
                return True
        return False

    # 输出八数码
    def showLine(self):
        endState = self.open[0]
        road = []
        while(True):
            if(endState.parent):
                endState = endState.parent
                road.append(endState)
            else:
                break
        road.reverse()
        for j in road:
            for i in range(0, 3):
                print(j.state[i*3:i*3+3])
            print('\n\000\000\000\000↓\n')

    # 宽度优先搜索算法
    def search(self):
        if self.originalNode.state == self.targetNode.state:
            return True
        else:
            a = self.hasSolve()  # 判断是否可达
            while(a):
                if(len(self.open)):
                    extandNode = self.open[-1]  # 读取最后一个元素
                    # print(extandNode.degree)
                    spacIndex = extandNode.state.index(0)  # 0 所在的位置
                    flag = False
                    if(extandNode.degree >= self.MaxDegree):
                        node = self.open.pop()  # 移除 open 表中最后一个元素，并传递给 close 表
                        self.close.append(node)
                        continue
                    else:
                        for i in range(len(self.spce)):
                            if((i == 0 and (spacIndex + self.spce[i] >= 0) or
                                    (i == 1 and (spacIndex + self.spce[i]) < len(extandNode.state) - 1) or
                                    (i == 2) and (spacIndex % self.length != 0)) or
                                    (i == 3 and ((spacIndex + 1) % self.length) != 0)):
                                state = self.copyArray(extandNode.state)
                                # 扩展状态
                                temp = state[spacIndex + self.spce[i]]
                                state[spacIndex + self.spce[i]] = 0
                                state[spacIndex] = temp
                                newNode = Node(extandNode, state, extandNode.degree + 1)
                                # print(newNode.degree)
                                if(state == self.targetNode.state):
                                    self.open.insert(0, newNode)
                                    return True
                                elif(not self.isInTable(newNode, self.close) and not self.isInTable(newNode, self.open)):
                                    self.open.insert(0, newNode)
                                    flag = True
                                    self.step += 1
                                    # print(newNode.state)
                                else:
                                    continue
                        if(not flag):
                            self.open.pop()
                        else:
                            self.close.append(extandNode)
                            self.open.remove(extandNode)
                else:
                    return False

    def getStep(self):
        return self.step
