# 函数汇总及说明

## 类对象
1. BTree 新增属性
   - .depth  # 节点深度，根节点为0
   - .position = 1 # 节点序数
   - ._max_depth = 0 # 总深度，只有根节点具有该属性
2. node 自带属性
   - .left
   - .right
   - .value 
3. 新增方法
   - .new_tree_by_list # 将最后一层指定的位置展开 
4. @property
   - .max_depth # 获取最长深度。一般用遍历更新，但由于经常用，这里使用隐藏变量 ._max_depth
   - .last_layer # 返回最后一层节点
5. @staticmethod/@classmethod
   - .add_left_to_node(node,value) # 左节点，附带属性 depth 和 position
   - .add_right_to_node(node,value) # 由节点，附带属性同上
   - .add_left_right_to_node(node) # 添加节点，附带属性同上，赋值为0
   - .position_tree(tree) # 返回相同形状的树，结点显示值为位置
   - .list_to_tree(positions) # 列表数据转化为树
   - .random_binary_tree(depth,max_value=30) # 生成深度为 depth 的随机树，叶子取值范围为 [0,max_value]
   - .tree_to_list(tree,depth=None) # 树 -> 列表，默认取树的深度
   - .node_to_list(tree,depth) # 节点导出树 -> 列表，需指定深度

5. 特别注意
   - 根节点所在层 depth = 0
   - 根节点的位置 position = 1

## 函数工具
1. choose(data,n) # 从 data 中取 n 个元素
2. get_nodes_cost(tree) # 记录非叶节点和叶节点开销的字典，只记录非0开销
3. main(positions,leaves)->((sep,com),min_cost) # 打包函数
4. get_operations(old,new)->(sep,com) # 获取树的变动信息
5. is_nonleaves(nonleaves) # 检查非叶序列良定义
6. leaves_to_nonleaves(leaves) # 叶子序列 -> 非叶子序列
7. nonleaves2leaves(nonleaves) # 非叶序列 -> 叶子序列
8. random_nonleaves_seq(n) # 随机生成长为 n 的非叶节点序列
9. random_leaves_seq # 随机生成 n 层叶节点序列
10. next_level(tree,nonleaves,nonleaf_cost,leaf_cost) # 过程函数-忽略

11. save_vari(v,name) # 保存变量，需 pickle 库
12. read_vari(name) # 读取变量，需 pickle 库