# -*- coding: utf-8 -*-
# @Time     : 2020/9/10-07:30
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : sklearn_lg.py
# @Project  : Sep-Dragon
# *************************************************
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
clf = LogisticRegression(random_state=0).fit(X, y)
clf.predict(X[:2, :])

proba = clf.predict_proba(X[:2, :])

score = clf.score(X, y)
print(proba, score)
