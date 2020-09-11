# -*- coding: utf-8 -*-
# @Time     : 2020/9/11-11:13
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : em.py
# @Project  : Sep-Dragon
# *************************************************

# reference: https://blog.csdn.net/u010866505/article/details/77877345
# 模拟两个正态分布的均值估计

import numpy as np
import random
import copy

SIGMA = 6
EPS = 0.0001


# 生成方差相同,均值不同的样本
def generate_data():
    Miu1 = 20
    Miu2 = 40
    N = 1000
    X = np.mat(np.zeros((N, 1)))
    for i in range(N):
        temp = random.uniform(0, 1)
        if (temp > 0.5):
            X[i] = temp * SIGMA + Miu1
        else:
            X[i] = temp * SIGMA + Miu2
    return X


# EM算法
def EM(X):
    k = 2
    N = len(X)
    Miu = np.random.rand(k, 1)
    Posterior = np.mat(np.zeros((N, 2)))
    dominator = 0
    numerator = 0
    # 先求后验概率
    for iter in range(1000):
        for i in range(N):
            dominator = 0
            for j in range(k):
                dominator = dominator + np.exp(-1.0 / (2.0 * SIGMA ** 2) * (X[i] - Miu[j]) ** 2)
            print(dominator, -1 / (2 * SIGMA ** 2) * (X[i] - Miu[j]) ** 2, 2 * SIGMA ** 2, (X[i] - Miu[j]) ** 2)
            # return
            for j in range(k):
                numerator = np.exp(-1.0 / (2.0 * SIGMA ** 2) * (X[i] - Miu[j]) ** 2)
                Posterior[i, j] = numerator / dominator
        oldMiu = copy.deepcopy(Miu)
        # 最大化
        for j in range(k):
            numerator = 0
            dominator = 0
            for i in range(N):
                numerator = numerator + Posterior[i, j] * X[i]
                dominator = dominator + Posterior[i, j]
            Miu[j] = numerator / dominator
        print((abs(Miu - oldMiu)).sum())
        # print '\n'
        if (abs(Miu - oldMiu)).sum() < EPS:
            print(Miu, iter)
            break


if __name__ == '__main__':
    X = generate_data()
    EM(X)

# import math
# class EM:
#     def __init__(self, prob):
#         self.pro_A, self.pro_B, self.pro_C = prob
#
#     # e_step
#     def pmf(self, i):
#         pro_1 = self.pro_A * math.pow(self.pro_B, data[i]) * math.pow(
#             (1 - self.pro_B), 1 - data[i])
#         pro_2 = (1 - self.pro_A) * math.pow(self.pro_C, data[i]) * math.pow(
#             (1 - self.pro_C), 1 - data[i])
#         return pro_1 / (pro_1 + pro_2)
#
#     # m_step
#     def fit(self, data):
#         count = len(data)
#         print('init prob:{}, {}, {}'.format(self.pro_A, self.pro_B,
#                                             self.pro_C))
#         for d in range(count):
#             _ = yield
#             _pmf = [self.pmf(k) for k in range(count)]
#             pro_A = 1 / count * sum(_pmf)
#             pro_B = sum([_pmf[k] * data[k] for k in range(count)]) / sum(
#                 [_pmf[k] for k in range(count)])
#             pro_C = sum([(1 - _pmf[k]) * data[k]
#                          for k in range(count)]) / sum([(1 - _pmf[k])
#                                                         for k in range(count)])
#             print('{}/{}  pro_a:{:.3f}, pro_b:{:.3f}, pro_c:{:.3f}'.format(
#                 d + 1, count, pro_A, pro_B, pro_C))
#             self.pro_A = pro_A
#             self.pro_B = pro_B
#             self.pro_C = pro_C
#
#
#
# if __name__ == '__main__':
#     data = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1]
#     em = EM(prob=[0.4, 0.6, 0.7])
#     f = em.fit(data)
#     next(f)
#     # 第一次迭代
#     f.send(1)
#     # 第二次
#     f.send(2)
