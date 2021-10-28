import math
import trans
import transm
import time
from random import randint
from btree import *

def random_nonleaf_seq(n):
    """随机生成 n 层的非叶节点序列"""
    assert n>0, "层数至少为1"
    if n==1: return [0]
    seq = [1]
    while len(seq)!=n-1:
        total = seq[-1] * 2
        seq.append(randint(1,total))
    return seq+[0]

def main():
    '''
    p = [-1, -2, -4, -6, -10, 11, 21, 35, -7, 40, -11, -5, -8, -9, -12, -14, -16, 12, 5, 50, -15, 20, -17, 111, 9, -13, -3]
    i = [11, -10, 21, -6, 35, -4, 40, -7, -11, -2, -8, -5, 12, -16, 5, -14, 50, -12, 20, -15, 111, -17, 9, -9, -13, -1, -3]
    arr = trans.buildTree(p, i)
    arr = trans.buildNums(arr, 8)
    n = 8
    positions = []
    for _ in range(8):
        tmp = arr.copy()
        positions.append(tmp)
    time_sum = 0
    nonleaf2leaf = lambda nonleaf:[0]+[2*a-b for a,b in zip(nonleaf[:-1],nonleaf[1:])]
    random_leaf_seq = lambda n: nonleaf2leaf(random_nonleaf_seq(n))
    for _ in range(50):
        tmp_tar = random_leaf_seq(8)
        for k in range(len(tmp_tar)):
            tmp_tar[k] *= 8
        time_start=time.time()
        transm.test(positions, tmp_tar)
        time_end = time.time()
        time_sum += (time_end - time_start)
        print(tmp_tar)
    time_sum /= 50
    print('totally cost',time_sum)
    
    
    '''
    time_sum = 0
    nonleaf2leaf = lambda nonleaf:[0]+[2*a-b for a,b in zip(nonleaf[:-1],nonleaf[1:])]
    random_leaf_seq = lambda n: nonleaf2leaf(random_nonleaf_seq(n))
    max_time = -math.inf
    min_time = math.inf
    for _ in range(1000):
        positons = []
        for tree_k in range(8):
            if tree_k ==  0:
                tmp_arr = BTree.random_binary_tree(7, 1, 200)
                tmp_arr = BTree.tree_to_positions(tmp_arr)
                positons.append(tmp_arr)
            else:
                tmp_arr = BTree.random_binary_tree(randint(1, 7), 0, 200)
                tmp_arr = BTree.tree_to_positions(tmp_arr)
                positons.append(tmp_arr)
        # tmp_arr = BTree.random_binary_tree(7, 1)
        # tmp_arr = BTree.tree_to_positions(tmp_arr)
        tmp_tar = [0] * 8
        for _ in range(8):
            ttmp_tar = random_leaf_seq(8)
            for kk in range(len(tmp_tar)):
                tmp_tar[kk] += ttmp_tar[kk]
        time_start=time.time()
        transm.test(positons, tmp_tar)
        time_end = time.time()
        spend_time = time_end - time_start
        max_time = max(max_time, spend_time)
        min_time = min(min_time, spend_time)
        time_sum += spend_time
        # print(tmp_tar)
    time_sum /= 1000
    print('平均时长：', time_sum)
    print('最长花费：', max_time)
    print('最短花费：', min_time)    
    return

if __name__ == '__main__':
    main()
