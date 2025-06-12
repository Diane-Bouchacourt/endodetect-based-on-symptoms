import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

if __name__ == "__main__":

    data = pd.read_excel("../data/dataset.xlsx")

    y = data["label"].values
    data = data.drop(data.columns[0], axis=1)  # remove first columns
    data = data.drop(["row", "label"], axis=1)
    pca = PCA(n_components=10)
    pca.fit(data)
    X_t = pca.transform(data)

    print("explained variance ratio : %s" % str(pca.explained_variance_ratio_))

    colors = ["navy", "turquoise"]

    plt.figure()

    for color, i in zip(colors, [0, 1]):
        plt.scatter(
            X_t[y == i, 0],
            X_t[y == i, 1],
            color=color,
            alpha=0.8,
        )

    plt.show()
