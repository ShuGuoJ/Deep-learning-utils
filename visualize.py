"""
可视化数据
"""
import torch
import numpy as np


def visualize(x, y):
    x = x.cpu().numpy() if isinstance(x, torch.Tensor) else x
    y = y.cpu().numpy() if isinstance(y, torch.Tensor) else y
    from sklearn.decomposition import PCA
    from matplotlib import pyplot as plt
    pca = PCA(2, whiten=True)
    new_x = pca.fit_transform(x)
    for i in np.unique(y):
        tmp = new_x[y == i]
        c = plt.cm.Set1(i)
        plt.scatter(tmp[:, 0], tmp[:, 1], color=c, marker='*')
    plt.show()


# from sklearn.datasets import load_iris
# data = load_iris()
# visualize(data.data, data.target)