import math
import collections
import time
ans = math.inf
# ans = []
# 实现标签转换

class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    '''
    前中序构建二叉树
    preorder:list前序遍历
    inorderr:list后序遍历
    '''
    check = {}
    for i,value in enumerate(inorder):
        check[value] = i
    # 建立索引表
    def helper(start,sstart,end):  #start为前序第一个，sstart为后序第一个
        if start > end:
            return None
        root = TreeNode(preorder[start])
        cur = check[preorder[start]]
        left = cur - sstart
        root.left = helper(start+1,sstart,start+left)
        root.right = helper(start+left+1,cur+1,end)
        return root
        #ans = helper(0,0,len(preorder)-1)
    return helper(0,0,len(preorder)-1)

def buildNums(tree, cengshu):
    que = collections.deque()
    que.append(tree)
    nums = []
    k = 0
    while que and k < cengshu:
        for _ in range(len(que)):
            tmp = que.popleft()
            if not tmp:
                nums.append(None)
                que.append(None)
                que.append(None)
            else:
                if tmp.val > 0:
                    nums.append(tmp.val)
                else:
                    nums.append(0)
                que.append(tmp.left)
                que.append(tmp.right)
        k += 1
    return nums

def dfs(nums, target, i, cost):
    '''
    nums为层序遍历数组
    target为每层要求节点数
    i为递归到了第几层 0, 1, 2
    '''
    # print('成功进入')
    global ans
    # 此时还没有算出cost
    if i == len(target) - 1: # 最后一层不用管
        ans = min(ans, cost)
        #ans.append(cost)
        return
    if cost >= ans:
        print('跳出')
        return
    min_index, max_index = 2 ** i - 1, 2 ** (i + 1) - 2  # i层的index
    leaf_nums = 0  # 叶子结点数
    tmp_leaf = []
    tmp_noleaf = [] # 非叶子结点
    for j in range(min_index, max_index + 1):
        if nums[j] != None:
            # tmp_leaf.append(j)
            if nums[2 * j + 1] != None and nums[2 * j + 2] != None:
                tmp_noleaf.append(j) # 非叶子结点
            else:
                leaf_nums += 1
                tmp_leaf.append(j)  # tmp保存非叶子结点的index
    print(leaf_nums)
    print(target[i])
    if leaf_nums == target[i]: # 若此时已经满足
        dfs(nums, target, i + 1, cost)
    elif leaf_nums > target[i]: # 此时只需要分,找出最小的几个分即可
        # tmp_leaf中保存的是叶子结点
        need_separate_nums = leaf_nums - target[i]
        leaf_cost = {k:nums[k] for k in tmp_leaf}
        leaf_cost_order = sorted(leaf_cost.items(), key = lambda x:x[1])
        separate_index = [leaf_cost_order[kk][0] for kk in range(need_separate_nums)]
        nums_tmp = nums.copy()
        cost_sum = 0
        for ii in separate_index: # 要分开的index
            #nums_tmp = nums.copy()
            leaf_separate(nums_tmp, ii)
            cost_sum += nums[ii]
        #print('第几层', i)
        dfs(nums_tmp, target, i + 1, cost + cost_sum)
    else: # lear_nums < target[i] 此时只用合
        print('错误进入')
        need_merge_nums = target[i] - leaf_nums
        # 从非叶子结点 tmp_leaf中选出need_merge_nums个
        print(tmp_noleaf)
        merge_index = get_merge_index(tmp_noleaf, need_merge_nums)
        print(merge_index)
        for merge_index_set in merge_index:
            # 合并 并且算出cost
            nums_tmp = nums.copy()
            tmp_cost = 0
            for ii in merge_index_set:
                cc = cal_merge_cost(nums_tmp, ii)
                tmp_cost += cc
            dfs(nums_tmp, target, i + 1, cost + tmp_cost)
            
def cal_merge_cost(nums, index):
    '''
    合并时处理，计算出lost同时收缩子树
    '''
    res = 0
    que = collections.deque()
    que.append(index)
    while que:
        tmp = que.popleft()
        res += nums[tmp]
        if 2 * tmp + 1 < 255 and nums[2 * tmp + 1] != None:
            # 层数
            que.append(2 * tmp + 1)
        if 2 * tmp + 2 < 255 and nums[2 * tmp + 2] != None:
            que.append(2 * tmp + 2)
        nums[tmp] = None
    nums[index] = 0
    return res
        
def leaf_separate(nums, index):
    nums[index] = 0
    nums[2 * index + 1] = 0
    nums[2 * index + 2] = 0

def get_merge_index(nums, k):
    '''
    从nums中选出k个index
    '''
    res = []
    def dfs_getindex(tmp, arr):
        if len(tmp) == k:
            res.append(tmp)
            return
        for i in range(len(arr)):
            dfs_getindex(tmp + [arr[i]], arr[i + 1:])
        return
    dfs_getindex([], nums)
    return res

def test(positions, arr):
    global ans
    ans = math.inf
    dfs(positions, arr, 0, 0)
    print(ans)

def main():
    '''
    #arr = [0, 0, 15, 13, 14, None, None]
    tar = [0, 0, 2, 0, 3, 2, 3, 26]
    
    p = [-1, -2, -4, -6, -10, 11, 21, 35, -7, 40, -11, -5, -8, -9, -12, -14, -16, 12, 5, 50, -15, 20, -17, 111, 9, -13, -3]
    i = [11, -10, 21, -6, 35, -4, 40, -7, -11, -2, -8, -5, 12, -16, 5, -14, 50, -12, 20, -15, 111, -17, 9, -9, -13, -1, -3]
    arr = buildTree(p, i)
    arr = buildNums(arr, 8)
    n = 8
    positions = [0]*(2**(n-1)-1) + list(range(2**(n-1)))
    time_start=time.time()
    print(len(arr))
    test(positions, [0, 1, 0, 0, 5, 2, 5, 6])
    # print(arr)
    
    # n = 8
    # positions = [0 for i in range(2**n)]
    # pos = [ii for ii in range(129 ,257)]
    # value = [kk for kk in range(1, 129)]
    # for p,v in zip(pos,value):
    #     positions[p-1] = v
    #positions = [0]*(2**(n-1)-1) + list(range(2**(n-1)))
    # print(len(positions))
    # dfs(positions, [0, 0, 0, 0, 0, 6, 26, 52], 0, 0)
    # ss = cal_merge_cost(arr, 15)
    # print(arr)
    # print(ss)
    time_end = time.time()
    print('totally cost',time_end-time_start)
    print(ans)
    '''

if __name__ == '__main__':
    main()
