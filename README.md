# 说明
暂空，无。

# 使用示例

## 运行代码
1. 在 btree 目录下运行，导入模块
   ```py
   from btree import *
   ```

2. 初始化旧树，一维列表
    ```py
    # 定义旧树
    n = 8
    positions = [None for i in range(2**n)]
    pos = [1, 
        2,3, 
        4,5, 
        8,9,10,11, 
        16,17,22,23, 
        32,33,34,35,46,47,
        68,69,70,71,
        136,137,138,139,142,143]
    values = [0,
            0,10,
            0,0,
            0,20,5,0,
            0,0,7,0,
            10,20,0,0,0,6,
            0,0,5,0,
            10,6,3,10,7,2]
    for p,v in zip(pos,values):
        positions[p-1] = v
    ```

3. 输入叶子序列，转为非叶序列
   ```py
    leaves = [0,0,3,0,3,0,4,0]
    nonleaves = leaves_to_nonleaves(leaves)
    ```

4. 求最优解
   ```py
   operates,optimals,cost = binary_tree_cost(positions,nonleaves)
   ```

5. 打印结果
   ```py
   old_tree = BTree.list_to_tree(positions)
   print(old_tree)
   for tree,operate in zip(optimals,operates):
       sep,com = operate
       print("拆分叶节点",sep)
       print("合并",com)
       print(tree)
   ```

## 输出结果
1. 初始图，新图及对应操作
   ![20211011173224](https://cdn.jsdelivr.net/gh/RexWzh/PicBed@picgo/picgo_folder/20211011173224.png)

2. 另一解
   ![20211011173235](https://cdn.jsdelivr.net/gh/RexWzh/PicBed@picgo/picgo_folder/20211011173235.png)

> 注：最优解很差，因为叶子序列 [0,0,3,0,3,0,4,0] 对应的图像第 8 层没有节点。