# -*- coding: utf-8 -*-
# @Time     : 2020/9/10-10:29
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : tree_recursion.py
# @Project  : Sep-Dragon
# *************************************************


# 二叉树类
class BTree(object):

    # 初始化
    def __init__(self, data=None, left=None, right=None):
        self.data = data  # 数据域
        self.left = left  # 左子树
        self.right = right  # 右子树

    # 前序遍历
    def preorder(self):

        if self.data is not None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历
    def inorder(self):

        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()

    # 后序遍历
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')

    # 层序遍历
    def levelorder(self):

        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None

        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None

        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.data is not None:
            level_order.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].data

        return level_order

    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 二叉树的叶子节点
    def leaves(self):

        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()


# 利用列表构造二叉树
# 列表中至少有一个元素
def create_BTree_By_List(array):
    i = 1
    # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
    level_order = []
    sum = 1

    while sum < len(array):
        level_order.append(array[i - 1:2 * i - 1])
        i *= 2
        sum += i
    level_order.append(array[i - 1:])

    # print(level_order)

    # BTree_list: 这一层所有的节点组成的列表
    # forword_level: 上一层节点的数据组成的列表
    def Create_BTree_One_Step_Up(BTree_list, forword_level):

        new_BTree_list = []
        i = 0
        for elem in forword_level:
            root = BTree(elem)
            if 2 * i < len(BTree_list):
                root.left = BTree_list[2 * i]
            if 2 * i + 1 < len(BTree_list):
                root.right = BTree_list[2 * i + 1]
            new_BTree_list.append(root)
            i += 1

        return new_BTree_list

    # 如果只有一个节点
    if len(level_order) == 1:
        return BTree(level_order[0][0])
    else:  # 二叉树的层数大于1

        # 创建最后一层的节点列表
        BTree_list = [BTree(elem) for elem in level_order[-1]]

        # 从下往上，逐层创建二叉树
        for i in range(len(level_order) - 2, -1, -1):
            BTree_list = Create_BTree_One_Step_Up(BTree_list, level_order[i])

        return BTree_list[0]


if __name__ == '__main__':
    # 构造二叉树, BOTTOM-UP METHOD
    right_tree = BTree(6)
    right_tree.left = BTree(2)
    right_tree.right = BTree(4)

    left_tree = BTree(5)
    left_tree.left = BTree(1)
    left_tree.right = BTree(3)

    tree = BTree(11)
    tree.left = left_tree
    tree.right = right_tree

    left_tree = BTree(7)
    left_tree.left = BTree(3)
    left_tree.right = BTree(4)

    right_tree = tree  # 增加新的变量
    tree = BTree(18)
    tree.left = left_tree
    tree.right = right_tree

    print('先序遍历为:')
    tree.preorder()
    print()

    print('中序遍历为:')
    tree.inorder()
    print()

    print('后序遍历为:')
    tree.postorder()
    print()

    print('层序遍历为:')
    level_order = tree.levelorder()
    print(level_order)
    print()

    height = tree.height()
    print('树的高度为%s.' % height)

    print('叶子节点为：')
    tree.leaves()
    print()

    # 使用数据进行输入
    # array = list(range(1,19))
    array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tree = create_BTree_By_List(array)

    print('先序遍历为:')
    tree.preorder()
    print()

    height = tree.height()
    print('\n树的高度为%s.\n' % height)

    print('层序遍历为:')
    level_order = tree.levelorder()
    print(level_order)
    print()

    print('叶子节点为：')
    tree.leaves()
