### 一句结果求信息熵

### 然后计算信息增益（利用结果-其余每一个特征的信息熵）

### 获取根结点，从而更新根熵的Gain

### 不断递归，当根结点出现gain=0,这个节点不再分裂


### 改进版本c4.5

对每一列的特征进行去重复，构成字典的key,value就是含有该Key的每一条数据

分别计算当前key下的占比*含当前key的信息熵，在进行求和

获取信息增益