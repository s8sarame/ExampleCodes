from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

import numpy as np

class pca():
    def __init__(self):
        self.calc_pca("pca_toy.txt")


    def calc_pca(self, file):
        #store data to ndarray
        data = np.loadtxt(file, skiprows=1)

        #store headers as labels for plot
        f = open(file, 'r')
        lines = f.read().splitlines()
        l = lines[0].split('\t')
        labels = [i for i in l]

        #standardize
        x = StandardScaler().fit_transform(data)

        #apply PCA
        pca = PCA(n_components=2)
        pca_data = pca.fit_transform(x)

        # print the %variance from the two components
        print(pca.explained_variance_ratio_)

        #plot the data
        self.plot_pca(pca_data, np.transpose(pca.components_), labels)

    def plot_pca(self,data, transpose, labels):
        #plot principal components w.r.t. transformed data

        x_ = data[:, 0]
        y_ = data[:, 1]


        x = 1.0 / (x_.max() - x_.min())
        y = 1.0 / (y_.max() - y_.min())

        plt.scatter(x_ * x, y_ * y, s=5)

        #plot both the observations and variables of multivariate data(PC1,PC2)
        for i in range(transpose.shape[0]):
            plt.arrow(0, 0, transpose[i, 0], transpose[i, 1], color='r', alpha=0.5)


            plt.text(transpose[i, 0] * 1.15, transpose[i, 1] * 1.15, labels[i], color='black', ha='center', va='center')
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.grid()
        plt.show()









a = pca()