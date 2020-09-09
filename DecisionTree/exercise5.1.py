# -*- coding: utf-8 -*-
# @Time     : 2020/9/9-15:49
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : exercise5.1.py
# @Project  : Sep-Dragon
# *************************************************

from math import log

import numpy as np
import pandas as pd


def create_data():
    datasets = [['青年', '否', '否', '一般', '否'],
                ['青年', '否', '否', '好', '否'],
                ['青年', '是', '否', '好', '是'],
                ['青年', '是', '是', '一般', '是'],
                ['青年', '否', '否', '一般', '否'],
                ['中年', '否', '否', '一般', '否'],
                ['中年', '否', '否', '好', '否'],
                ['中年', '是', '是', '好', '是'],
                ['中年', '否', '是', '非常好', '是'],
                ['中年', '否', '是', '非常好', '是'],
                ['老年', '否', '是', '非常好', '是'],
                ['老年', '否', '是', '好', '是'],
                ['老年', '是', '否', '好', '是'],
                ['老年', '是', '否', '非常好', '是'],
                ['老年', '否', '否', '一般', '否'],
                ]
    labels = [u'年龄', u'有工作', u'有自己的房子', u'信贷情况', u'类别']
    # 返回数据集和每个维度的名称
    return datasets, labels


# 熵
def calc_ent(datasets):
    data_length = len(datasets)
    label_count = {}
    for i in range(data_length):
        label = datasets[i][-1]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    ent = -sum([(p / data_length) * log(p / data_length, 2)
                for p in label_count.values()])
    return ent


# def entropy(y):
#     """
#     Entropy of a label sequence
#     """
#     hist = np.bincount(y)
#     ps = hist / np.sum(hist)
#     return -np.sum([p * np.log2(p) for p in ps if p > 0])


# 经验条件熵
def cond_ent(datasets, axis=0):
    data_length = len(datasets)
    feature_sets = {}
    for i in range(data_length):
        feature = datasets[i][axis]
        if feature not in feature_sets:
            feature_sets[feature] = []
        feature_sets[feature].append(datasets[i])
    cond_ent = sum(
        [(len(p) / data_length) * calc_ent(p) for p in feature_sets.values()])
    return cond_ent


# 信息增益
def info_gain(ent, cond_ent):
    return ent - cond_ent


def info_gain_train(datasets):
    count = len(datasets[0]) - 1
    ent = calc_ent(datasets)
    #     ent = entropy(datasets)
    best_feature = []
    for c in range(count):
        c_info_gain = info_gain(ent, cond_ent(datasets, axis=c))
        best_feature.append((c, c_info_gain))
        print('特征({}) - info_gain - {:.3f}'.format(labels[c], c_info_gain))
    # 比较大小
    best_ = max(best_feature, key=lambda x: x[-1])
    return '特征({})的信息增益最大，选择为根节点特征'.format(labels[best_[0]])


if __name__ == '__main__':
    datasets, labels = create_data()
    train_data = pd.DataFrame(datasets, columns=labels)

    print(train_data)

    res = info_gain_train(np.array(datasets))
    print(res)
