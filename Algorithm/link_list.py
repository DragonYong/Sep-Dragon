# -*- coding: utf-8 -*-
# @Time     : 2020/9/10-09:44
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : link_list.py
# @Project  : Sep-Dragon
# *************************************************
class Node:
    """
    思路:将自定义的类视为节点的生成类,实例对象中
        包含数据部分和指向下一个节点的next
    """

    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 循环链接下一个节点关系


class LinkList:
    """
    思想:单链表类,生成对象可以进行增删改查操作

    """

    # 创建数据为空的一个链表头
    def __init__(self):
        """
        初始化链表,标记一个链表的开端,以便于获取后续的节点
        :param val:
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        p = self.head  # p作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历列表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next  # p向后移动

    # 判断链表为空
    def is_emply(self):
        if self.head.next is None:  # head后面一个节点没有,判断为空
            return True
        else:
            return False

    # 清空链表
    def clear_list(self):
        self.head.next = None

    # 索引列表(读取指定列表元素)
    def index_variables(self, index_):
        p = self.head
        for item in range(index_ + 1):
            if p.next == None:
                # 超出位置最大范围跳出循环,提示错误
                raise IndexError("list index out of range")
            p = p.next
        return p.val

    # 尾部插入
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_insert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 索引插入(指定位置插入)
    def index_insert(self, index_, val):
        p = self.head
        for item in range(index_):
            if p.next == None:
                # 超出位置最大范围跳出循环
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除指定数据的节点
    def delete_val(self, val):
        p = self.head
        # 结束循环必然两个条件其一为假
        while p.next and p.next.val != val:
            p = p.next
        if p.next is None:
            print("x not in linklist")
        else:
            p.next = p.next.next

    # 删除指定位置节点
    def delete_index(self, index_):
        p = self.head
        for item in range(index_):
            if p.next == None:
                # 超出位置最大范围跳出循环
                break
            p = p.next
        if p.next == None:
            pass  # 超出最大位置不删除
        else:
            p.next = p.next.next

    # 有序链表(从小到大)中插入单个节点,保证链表依然有序
    def index_val(self, val):
        # 这个类似数组的插入排序，每次拿出一个放到有序中合适的位置
        p = self.head
        while p.next != None and p.next.val < val:
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 节点数据从小到大排序
    def up_list(self):
        """
        将链表数据从小到大排列
        :return:
        """
        p = self.head
        l_re = LinkList()  # 新建一个链表，用来从小到大存放节点
        while p.next != None:
            l_re.index_val(p.next.val)  # 加第一个
            p = p.next  # 删第一个
        self.head = l_re.head


if __name__ == "__main__":
    l = LinkList()  # 新建一个链表头
    l.head.next = Node(1)
    print(l.head.next.val)
    print("------------------------")
    l.init_list([9, 7, 5, 3, 1])  # 插入列表
    l.append(11)  # 尾部插入
    l.head_insert(66)  # 头部插入
    l.index_insert(3, 77)  # 指定位置插入
    l.index_insert(20, 13)  # 超出位置插入最后
    l.index_insert(-20, 11)  # 插入在开头
    l.delete_val(77)  # 删除指定数据节点(只删除第一个出现的)
    l.delete_index(1)  # 删除指定位置节点
    l.delete_index(-100)  # 删除开头元素
    l.delete_index(10)  # 超出最大位置不删除
    l.index_val(4)  # 有序链表(从小到大)中插入单个节点,保证链表依然有序
    l.up_list()  # 链表 数据节点从小到大排序

    l.show()  # 遍历链表

    l.index_variables(0)
