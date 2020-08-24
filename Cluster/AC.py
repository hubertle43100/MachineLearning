import numpy as np
import pandas as pd
from scipy import ndimage
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from matplotlib import pyplot as plt
from sklearn import manifold, datasets
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_blobs

X1, y1 = make_blobs(n_samples = 1500, centers = [[-2,3],[1,-3], [5,6],[-3,-3]], cluster_std = 1.0)

plt.scatter(X1[:, 0], X1[:, 1], marker = 'o')

k = 4
agg = AgglomerativeClustering(n_clusters = k, linkage = 'average')

agg.fit(X1, y1)

plt.figure(figsize = (6,4))

x_min, x_max = np.min(X1, axis = 0), np.max(X1, axis = 0)
X1 = (X1 - x_min)/(x_max - x_min)

for i in range(X1.shape[0]):
    plt.text(X1[:, 0], X1[:, 1], str(y1[i]),
    color = plt.cm.nipy_spectral(agg.labels_[i]/ 10),
    fontdict = {'weight': 'bold', 'size': 9 })

plt.xticks([])
plt.yticks([])

plt.scatter(X1[:, 0], X1[:, 1], marker = '.')
plt.show()

dist_matrix = distance_matrix(X1, X1)
print(dist_matrix)

Z = hierarchy.linkage(dist_matrix, 'complete')
dendro = hierarchy.dendrogram(Z)
