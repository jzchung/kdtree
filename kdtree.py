from typing import List, Any

import numpy as np
import math

# input: data set X(d by n) where d is the number of dimensions of
# features, and n denotes the number of samples.


def kd_tree(x, depth):
    # construct root
    if depth >= len(x):  # 递归层数不会大于维度数
        return {'content': x}
    if len(x) == 0:
        return
    xt = np.transpose(x)
    sortedx = np.sort(x[depth])
    median_num = sortedx[math.floor(len(xt) / 2)]
    content = []  # 放根节点的内容
    left = []  # 放左子区的节点
    right = []  # 放右子区的节点
    # 选出所有特征大小的样本作为root的content属性
    for i in range(len(xt)):
        if x[depth][i] == median_num:  # 等于切分点，放入根节点
            content.append(xt[i, :].tolist())
        elif x[depth][i] < median_num:  # 小于切分点，放入左子区
            left.append(xt[i, :].tolist())
        elif x[depth][i] > median_num:  # 大于切分点，放入右子区
            right.append(xt[i, :].tolist())
    # root的left和right_child属性则使用递归来实现
    print('content: ', content, ' left: ', left, ' right: ', right)
    root = {'content': np.transpose(content)}
    root['right-child'] = kd_tree(np.transpose(right), depth + 1)
    root['left-child'] = kd_tree(np.transpose(left), depth + 1)
    return root

# call function
x = [[2, 5, 9, 4, 8, 7], [3, 4, 6, 7, 1, 2]]
kd_tree(x, 0)
