from binarytree import Node
from copy import deepcopy
from random import randint

### 类函数
class BTree(Node):
    """二叉树，继承 Node 的显示功能
    根节点位置记为1，深度记为0
    """
    def __init__(self, value = 0):
        """更新旧的初始化"""
        Node.__init__(self, value) # 使用原初始化
        # 新增属性
        self.depth = 0 # 根节点深度
        self.position = 1 # 序数表述
        self._max_depth = 0 # 总深度
        
    def trees_by_k_nonleaves(self,k):
        """ 最后一层叶节点取 k 个拆开 -> 所有可能的新树"""
        num = len(self.last_layer)
        indexs = choose(list(range(num)),k)
        print(indexs,num,k)
        return [self._new_tree_by_index(index) for index in indexs]
    
    def _new_tree_by_index(self,index):
        """将指定节点展开，得到新树
        输入为索引，不建议外部调用"""
        # 复制对象
        tree = deepcopy(self)
        # 获取最后一层
        last_layer = tree.last_layer
        for i in index:
            # 调用方法：添加左右节点
            self.add_left_right_to_node(last_layer[i])
        tree._max_depth += 1 # 总深度+1
        return tree
    
    @property
    def last_layer(self):
        """返回最后一层节点"""
        return [l for l in self.leaves if l.depth==self._max_depth]
    
    @classmethod
    def add_left_right_to_node(cls,node) -> None:
        """给 node 添加左右子结点"""
        cls.add_left_to_node(node) # 左节点
        cls.add_right_to_node(node) # 右节点
    
    @staticmethod
    def add_left_to_node(node,value=0) -> None:
        """给 node 添加左节点，设置了 depth 和 position 属性"""
        left = Node(value)
        left.depth = node.depth + 1
        left.position = 2 * node.position
        node.left = left
    
    @staticmethod
    def add_right_to_node(node,value=0) -> None:
        """给 node 添加右节点，设置了 depth 和 position 属性"""
        right = Node(value)
        right.depth = node.depth + 1
        right.position = 2 * node.position + 1
        node.right =  right
    
    def position_tree(self):
        """返回相同形状的树，结点显示值为位置"""
        tree = deepcopy(self)
        for node in tree:
            node.value = node.position
        return tree
    
    @classmethod
    def list_to_tree(cls,positions):
        """一维列表 -> 树，空节点用 None 表示"""
        n = len(positions)
        assert n, "输入列表不能为空"
        assert positions[0] is not None,"根节点不能为空"
        # 初始化根节点
        tree = BTree(positions[0])
        while True:
            last_layer = tree.last_layer
            flag = False # 标记是否有新节点
            for node in last_layer:
                # 检查两个叶节点是否非 None
                pos = 2 * node.position
                # 左节点
                if pos>n: continue
                if positions[pos-1] is not None:
                    flag = True
                    cls.add_left_to_node(node,positions[pos-1])
                # 右节点
                if pos+1>n: continue
                if positions[pos] is not None:
                    flag = True
                    cls.add_right_to_node(node,positions[pos])
            if flag: # 有新节点生成
                tree._max_depth += 1
            else:
                break
        return tree
    
def choose(data,n):
    """从 data 中取 n 个元素"""
    if n > len(data): return []
    if n == 1: return [[i] for i in data]
    if n == len(data): return [data]
    omitlast = choose(data[:-1],n)
    takelast = [ i+[data[-1]] for i in choose(data[:-1],n-1)]
    return omitlast+takelast




### 其他函数 ###

def is_nonleaves(nonleaves):
    """检查非叶节点序列"""
    if len(nonleaves)==0:return False
    if len(nonleaves)==1:return True
    return all([2*i>=j for i,j in zip(nonleaves[:-1],nonleaves[1:])])

def nonleaves_to_trees(nonleaves):
    """非叶节点序列 -> 所有可能的树"""
    # 新树集合
    assert is_nonleaves(nonleaves), "非叶序列输入有误"
    trees = [BTree()]
    for ak in nonleaves:
        if ak == 0: # 后续没有节点了
            break
        new_trees = [] # 新一层
        for tree in trees: # 对上层遍历
            new_trees.extend(tree.trees_by_k_nonleaves(ak))
        trees = new_trees
    return new_trees

def leaves_to_nonleaves(leaves):
    """叶节点序列 -> 非叶节点序列"""
    assert len(leaves)>0, "输入不能为空列表"
    # 非叶节点序列和总节点序列
    nonleaves,nodes = [1-leaves[0]],[1]
    for i in leaves[1:]:
        nodes.append(2*nonleaves[-1]) # 总节点数
        nonleaves.append(nodes[-1]-i) # 可用根节点数
    # 检查未项是否只剩叶节点
    assert nonleaves[-1]==0,"输入叶节点序列不完整"
    return nonleaves
    
def choose(data,n):
    """从 data 中取 n 个元素"""
    if n > len(data): return []
    if n == 1: return [[i] for i in data]
    if n == len(data): return [data]
    omitlast = choose(data[:-1],n)
    takelast = [ i+[data[-1]] for i in choose(data[:-1],n-1)]
    return omitlast+takelast

def is_child(node,combine):
    """检验 node 是否为 combine 中元素的后代"""
    while node != 0:
        node //= 2
        if node in combine:
            return True
    return False

def random_nonleaves_seq(n):
    """随机生成 n 层非叶节点序列"""
    assert n>0, "层数至少为1"
    if n==1: return [0]
    seq = [1]
    while len(seq)!=n-1:
        total = seq[-1] * 2
        seq.append(randint(1,total))
    return seq+[0]

def binary_tree_cost(positions,nonleaves):
    """求二叉树变形的最优解"""
    old_tree = BTree.list_to_tree(positions)
    old_nodes = {node.position for node in old_tree}
    old_leafs = {node.position for node in old_tree.leaves}
    new_trees = nonleaves_to_trees(nonleaves)
    min_cost = sum(positions[i-1] for i in old_leafs) # 最小开销
    optimals = [] # 最优解
    operates = [] # 最优操作
    for new_tree in new_trees:
        # 新树信息
        new_leafs = {node.position for node in new_tree.leaves}
        new_nodes = {node.position for node in new_tree}
        # 获取操作
        com = old_nodes.difference(old_leafs).intersection(new_leafs)
        sep = new_nodes.difference(new_leafs).intersection(old_leafs)
        # 计算开销
        com_leafs = {leaf for leaf in old_leafs if is_child(leaf,com)}
        nodes = sep.union(com_leafs) # 被修改的节点
        cost = sum(positions[i-1] for i in nodes)
        if cost == min_cost and (sep,com) not in operates:
            optimals.append(new_tree)
            operates.append((sep,com))
        elif cost < min_cost:
            min_cost = cost
            optimals= [new_tree]
            operates = [(sep,com)]
    return operates,optimals,min_cost