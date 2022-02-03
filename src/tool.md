# 函数汇总及说明

## 类对象
1. Node 自带属性
   - .left
   - .right
   - .value 
   - .max_leaf_depth # 节点往下的最长深度
2. Node 新增属性和方法（更自然的方法是用 property + setter）
   - .depth  # 节点深度，根节点为0
   - .position = 1 # 节点序数
   - .is_leaf # 判断是否叶子
   - .add_left_to_node(value) # 添加左节点，同时设置属性 depth 和 position
   - .add_right_to_node(value) # 右节点，属性同上
   - .add_left_right_to_node() # 左右节点，属性同上，赋值0
3. BTree 属性和方法
   - .new_tree_by_list # 将最后一层指定的位置展开 
   - .last_layer # 返回最后一层节点
4. 特别注意
   - 根节点所在层 depth = 0
   - 根节点的位置 position = 1

## 树工具
1. position_tree(tree) # 返回相同形状的树，结点显示值为位置
2. list_to_tree(positions) # 列表数据转化为树
3. random_binary_tree(depth,max_value=30) # 生成深度为 depth 的随机树，叶子取值范围为 [0,max_value]
4. tree_to_list(tree,depth=None) # 树 -> 列表，默认取树的深度
5. node_to_list(tree,depth=None) # 节点导出树 -> 列表，需指定深度
6. get_operations(old,new)->(sep,com) # 获取树的变动信息
7. get_nodes_cost(tree) # 记录非叶节点和叶节点开销的字典，只记录非0开销

## 叶序列工具
1. is_nonleaves(nonleaves) # 检查非叶序列良定义
2. leaves_to_nonleaves(leaves) # 叶子序列 -> 非叶子序列
3. nonleaves2leaves(nonleaves) # 非叶序列 -> 叶子序列
4. random_leaves_seq # 随机生成 n 层叶节点序列
5. random_nonleaves_seq(n) # 随机生成长为 n 的非叶节点序列

## 其他工具及主函数
1. choose(data,n) # 从 data 中取 n 个元素
2. save_vari(v,name) # 保存变量，需 pickle 库
3. read_vari(name) # 读取变量，需 pickle 库
4. main(positions,leaves)->((sep,com),min_cost) # 打包函数
5. next_level(tree,nonleaves,nonleaf_cost,leaf_cost) # 过程函数-忽略
