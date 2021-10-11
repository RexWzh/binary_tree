# 说明
一道图论问题，纯粹遍历，没有用什么图论优化知识，算法弊端很明显。


# 使用示例

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

![20211011173224](https://cdn.jsdelivr.net/gh/RexWzh/PicBed@picgo/picgo_folder/20211011173224.png)

![20211011173235](https://cdn.jsdelivr.net/gh/RexWzh/PicBed@picgo/picgo_folder/20211011173235.png)

> 注：最优解 114 很差，由于叶子序列 [0,0,3,0,3,0,4,0] 对应二叉树的第 8 层没有节点。

# 运行效率
## 计算例子
写了一个随机生成非叶子序列的函数，用于测试，计算两个例子：
![20211011195758](https://i.loli.net/2021/10/11/SUwQ2faT5nW4DAc.png)
![20211011195700](https://i.loli.net/2021/10/11/qzOQbLycT25jaih.png)

序列较小时，运算时间还可以，一些计算步骤地方也还能改进。

而且第一遍实现算法用面向对象编程，方便观察图像，也方便调试。改用面向过程，将二叉树直接用一维列表，或者用 MMA 的函数式编程，运行可以加快几个level。

但计算随机例子时，遇到了一些极其糟糕的情况。

## 坏情况
当序列取值很大时，**考虑极端序列`[1, 2, 4, 8, 16, 26, 26, 0]`，验证数目达到 `449397407209308259968`（20位数）

随机测试 $10^6$ 个序列，大约两成的序列算法不能用。
![20211011195857](https://i.loli.net/2021/10/11/QWzi8LvREMwJqtN.png)

# 总结

1. 纯粹遍历走不通：如果问题是完全随机的，就算用对称性改进，意义也不大。
2. 正式尝试一个算法前应该先做复杂度分析，应数和基数思维挺多不同。