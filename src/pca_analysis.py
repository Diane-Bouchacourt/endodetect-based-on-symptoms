import pandas as pd
from sklearn.decomposition import PCA
import matplotlib
import matplotlib.pyplot as plt
import data_processing
from data_processing import MACROS_SYMPTOMS
import pdb 

if __name__ == "__main__":

    data = data_processing.prepare_data()
    macro_data = data_processing.create_macros_symptoms(data) # label is already removed

    y = data["label"].values
    data = data.drop(["label"], axis=1)
    pca = PCA(n_components=10)
    pca.fit(data)
    X_t = pca.transform(data)

    print("explained variance ratio : %s" % str(pca.explained_variance_ratio_))

    colors = ['green','red']

    for s in MACROS_SYMPTOMS:
        plt.figure()
        for color, label in zip(colors, [0,1]):
            y2 = macro_data[s].values
            symptomatic = ((y == label) & (y2 == 1))
            asymptomatic = ((y == label) & (y2 == 0))  
            plt.scatter(
                X_t[symptomatic, 0],
                X_t[symptomatic, 1],
                marker='+',
                color = color,
                alpha=0.5,
                label = label
            )
            plt.scatter(
                X_t[asymptomatic, 0],
                X_t[asymptomatic, 1],
                marker='s',
                color = color,
                alpha=0.5,
            )
        plt.title(s)
        plt.legend()
        plt.show()

 