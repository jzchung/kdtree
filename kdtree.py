import numpy as np
import math

# input: data set X(d by n) where d is the number of dimensions of
# features, and n denotes the number of samples.


def kd_tree(x):
    # construct root
    '''这里求中位数尚有疑问：根据书本所说取的应该是两个最中间的数中的其中一个（这里可以固定取右侧的数），这样能保证每次
    递归的根节点都有内容。故先这样实现，而不是使用真正的中位数'''

    median_num = x[0][math.ceil(len(x) / 2)]
    print(median_num)

    #选出所有特征大小的样本作为root的content属性

    #root的left和right_child属性则使用递归来实现

# call function
x = [[1, 2, 3, 4], [5, 6, 7, 8]]
kd_tree(x)
