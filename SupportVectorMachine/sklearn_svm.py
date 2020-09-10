# -*- coding: utf-8 -*-
# @Time     : 2020/9/10-07:15
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : sklearn_svm.py
# @Project  : Sep-Dragon
# *************************************************
# https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])

clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(X, y)
print(clf.predict([[-0.8, -1]]))
