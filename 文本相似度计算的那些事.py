#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/9/3-22:37
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : 文本相似度计算的那些事.py
# @Project  : Sep-Dragon
# *************************************************

import numpy as np


# 计算欧几里德距离：
def euclidean(p, q):
    # 如果两数据集数目不同，计算两者之间都对应有的数
    same = 0
    for i in p:
        if i in q:
            same += 1

    # 计算欧几里德距离,并将其标准化
    e = sum([(p[i] - q[i]) ** 2 for i in range(same)])
    return 1 / (1 + e ** .5)


def pearson(p, q):
    # 只计算两者共同有的
    same = 0
    for i in p:
        if i in q:
            same += 1

    n = same
    # 分别求p，q的和
    sumx = sum([p[i] for i in range(n)])
    sumy = sum([q[i] for i in range(n)])
    # 分别求出p，q的平方和
    sumxsq = sum([p[i] ** 2 for i in range(n)])
    sumysq = sum([q[i] ** 2 for i in range(n)])
    # 求出p，q的乘积和
    sumxy = sum([p[i] * q[i] for i in range(n)])
    # print sumxy
    # 求出pearson相关系数
    up = sumxy - sumx * sumy / n
    down = ((sumxsq - pow(sumxsq, 2) / n) * (sumysq - pow(sumysq, 2) / n)) ** .5
    # 若down为零则不能计算，return 0
    if down == 0: return 0
    r = up / down
    return r


# 计算曼哈顿距离：
def manhattan(p, q):
    # 只计算两者共同有的
    same = 0
    for i in p:
        if i in q:
            same += 1
    # 计算曼哈顿距离
    n = same
    vals = range(n)
    distance = sum(abs(p[i] - q[i]) for i in vals)
    return distance


# 计算jaccard系数
def Jaccrad(x, y):  # terms_reference为源句子，terms_model为候选句子
    temp = 0
    for i in x:
        if i in y:
            temp = temp + 1
    fenmu = len(y) + len(x) - temp  # 并集
    jaccard_coefficient = float(temp / fenmu)  # 交集
    return jaccard_coefficient


def tanimoto(p, q):
    c = [v for v in p if v in q]
    return float(len(c) / (len(p) + len(q) - len(c)))


def cosine_similarity(x, y, norm=False):
    assert len(x) == len(y), "len(x) != len(y)"
    zero_list = [0] * len(x)
    if x == zero_list or y == zero_list:
        return float(1) if x == y else float(0)

    res = np.array([[x[i] * y[i], x[i] * x[i], y[i] * y[i]] for i in range(len(x))])
    cos = sum(res[:, 0]) / (np.sqrt(sum(res[:, 1])) * np.sqrt(sum(res[:, 2])))

    return 0.5 * cos + 0.5 if norm else cos


def cosine_similarity(x, y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom


if __name__ == '__main__':
    x = np.random.randint(0, 100, 20)
    y = np.random.randint(0, 100, 20)
    cosine_similarity(x, y)
    cosine_similarity(x, y)
    euclidean(x, y)
    pearson(x, y)
    manhattan(x, y)
    Jaccrad(x, y)
