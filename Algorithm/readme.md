#### 新建一个链表头
l.head.next = Node(1)
包括value和next，并且把自身的地址给头节点的next

#### 插入列表
l.init_list([9, 7, 5, 3, 1])  
新建节点，上一个节点的next改成当前节点

#### 尾部插入
l.append(11) 
遍历。next只要不空，一直循环，出现空，把next改成当前节点

#### 头部插入
l.head_insert(66) 
修改当前节点的next为头节点的next

然后把头节点的next改成当前节点

#### 指定位置插入
l.index_insert(3, 77)  
先遍历3次，如果每一个节点的next不空

当前节点的next改成，遍历到此节点的next

遍历到此节点的next改成当前节点的地址

#### 超出位置插入最后
l.index_insert(20, 13)  

#### 插入在开头
l.index_insert(-20, 11)  

#### 删除指定数据节点(只删除第一个出现的)
l.delete_val(77) 
节点。next！=None and 节点。value！=value
遍历到此节点，p.next=p.next,next

#### 删除指定位置节点
l.delete_index(1)  

p.next=p.next.next()

#### 删除开头元素
l.delete_index(-100) 

#### 超出最大位置不删除
l.delete_index(10)  
每次只要验证node.next!=None即可确定是否超界

#### 有序链表(从小到大)中插入单个节点,保证链表依然有序
l.index_val(4)  
循环（next不空，值小于当前值）
node.next=p.next
p.next=node

#### 链表 数据节点从小到大排序
l.up_list()  
有序链表的插入排序

#### 遍历链表
l.show()  

#### 按索引查询
l.index_variables(0)

遍历这个参数，确保链表不在尾部即可
