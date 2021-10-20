# 说明
一道图论问题，表述简单且不需要什么理论背景，写一个试试。

# 示例和测试
## 示例

1. 导入模块
   ```py
   from btree import *
   ```

2. 输入初始树和叶节点信息
   ```py
   n = 8
   positions = [None for i in range(2**n-1)] # 旧树
   pos = [1, 
         2,3, 
         4,5, 
         8,9,10,11, 
         16,17,18,19,22,23,
         32,33,44,45,
         88,89,90,91,
         176,177]
   value = [0,
           0,0,
           0,0,
           0,0,0,0,
           0,35,40,0,0,0,
           10,20,0,0,
           0,50,20,10,
           10,5]
   for p,v in zip(pos,value):
       positions[p-1] = v
   leaves = [0,0,2,0,3,2,3,26]
   ```

3. 运行主函数 `main`，并打印计算结果
   ```py
   optimal,cost = main(positions,leaves)
   print("操作开销",cost)
   old = BTree.list_to_tree(positions)
   sep,com = get_operations(old,optimal)
   print("拆开位置",sep,"合并位置",com)
   ```
   显示如下
   ```py
   操作开销 0
   拆开位置 {19, 10, 3} 合并位置 set()
   ```

## 随机测试
随机生成叶子序列，测试运行速度，初始树的数据同上。

```py
import time
t = time.time()
for i in range(1000):
    leaves = random_leaves_seq(n)
    optimal,cost = main(positions,leaves)
print("用时 %.3fs"%(time.time()-t))
```

计算 1000 个数据，用时 1.520s。速度比较慢，但也还能接受。慢主要因为一些操作用类实现方便，但实现过程比较绕，改用对列表操作更直接更快。但这没必要了，因为**算法本身也有缺陷**。

## 坏情况测试
当初始树或叶子序列有一方性质好时，计算时间短。但如果初始树和序列都取到坏情况，运行就吃力了。
1. 坏情形的初始树
    ```py
    n = 8
    positions = [0]*(2**(n-1)-1) + list(range(2**(n-1)))
    ```

2. 配合性质稍差的叶子序列 `[0, 1, 0, 0, 5, 2, 5, 6]`
    ```py
    leaves = [0, 1, 0, 0, 5, 2, 5, 6] # 18 秒
    t = time.time()
    optimal,cost = main(positions,leaves)
    print("计算用时 %.3fs"%(time.time()-t))
    print("操作开销",cost)
    old = BTree.list_to_tree(positions)
    sep,com = get_operations(old,optimal)
    print("拆开位置",sep,"合并位置",com)
    ```
3. 运行结果
   - 计算用时 18.280s
   - 操作开销 7381
   - 拆开位置 set() 
   - 合并位置 {121, 2, 58, 122, 59, 123, 120, 124, 24, 25, 26, 27, 28}

计算已经开始勉强了，如果考虑最坏情形的叶子序列 `[0, 0, 0, 0, 0, 6, 26, 52]`，这个算法就完全不能用了。

# 写在后边
图论问题用穷举很容易碰壁，这次例子限定了 8 层，刚开始觉得可以穷举，就设计了算法。但直到算法实现，做随机测试才发现哪怕只有 8 层，算法也不能通用。
个人在这方面的经验还是太少了，尝试算法前应先分析复杂度，真正确定可以了，再落实到代码实现层面。