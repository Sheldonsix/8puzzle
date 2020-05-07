from Node import *
from breath_first import *
from best_first import *
from A_star import *
import time

if __name__ == '__main__':
    '''
    originate = [1, 3, 2, 4, 0, 5, 6, 7, 8]
    target = [4, 1, 2, 6, 3, 5, 7, 0, 8]
    '''
    #'''
    originate = [2, 8, 3, 1, 0, 4, 7, 6, 5]
    target = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    #'''
    '''
    originate = [5,4,2,0,8,3,7,6,1]
    target = [0,3,7,1,8,6,2,4,5]
    '''
    '''
    originate = [2, 8, 3, 1, 0, 4, 7, 6, 5]
    target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    '''
    '''
    originate = [1, 3, 2, 4, 0, 5, 6, 7, 8]
    target = [1, 2, 0, 4, 3, 5, 6, 7, 8]
    '''
    '''
    originate = [2, 8, 3, 1, 0, 4, 7, 6, 5]
    target = [0, 2, 3, 1, 8, 4, 7, 6, 5]
    '''
    '''
    originate = [1, 3, 2, 4, 0, 5, 6, 7, 8]
    target = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    '''
    node1 = Node(None, originate, 0)
    node2 = Node(None, target, 0)
    breadth = breadth_search(node1, node2, 100, 3)
    best = best_search(node1, node2, 100, 3)
    astar = astar_search(node1, node2, 100, 3)

    
    #记录时间
    start_bredath = time.perf_counter()
    flag_breadth = breadth.search()
    end_breadth = time.perf_counter()

    start_best = time.perf_counter()
    flag_best = best.search()
    end_best = time.perf_counter()

    start_astar = time.perf_counter()
    flag_astar = astar.search()
    end_astar = time.perf_counter()

    cost_breadth = end_breadth - start_bredath
    cost_best = end_best - start_best
    cost_astar = end_astar - start_astar
    
    #输出结果
    if(flag_breadth):
        print('宽度优先算法：最少移动 {} 步到达目标状态'.format(breadth.getStep()))
        
        breadth.showLine()
        for i in range(0, 3):
            print(target[i * 3 : i * 3 + 3])

        print('宽度优先算法用时 {} 秒'.format(cost_breadth))
    else:
        print('宽度优先算法：目标状态不可达')

    if(flag_best):
        print('全局择优搜索算法：最少移动 {} 步到达目标状态'.format(best.getStep()))
        best.showLine()
        for i in range(0, 3):
            print(target[i * 3 : i * 3 + 3])        
        print('全局择优搜索算法用时 {} 秒'.format(cost_best))
    else:
        print('局择优搜索算法:目标状态不可达')


    if(flag_astar):
        print('A* 搜索算法：最少移动 {} 步到达目标状态'.format(best.getStep()))
        astar.showLine()
        for i in range(0, 3):
            print(target[i * 3 : i * 3 + 3])        
        print('A* 搜索算法用时 {} 秒'.format(cost_best))
    else:
        print('A* 搜索算法:目标状态不可达')