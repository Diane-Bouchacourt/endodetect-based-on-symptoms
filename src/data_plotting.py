import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from itertools import combinations
from scipy.spatial.distance import jaccard
import data_processing


def plot_spearson(data):

    spearson_matrix = data.corr()

    plt.figure(figsize=(10, 10))
    plt.title("Spearson correlation coefficient between symptoms")

    # Create a heatmap
    sns.heatmap(
        spearson_matrix,
        annot=False,
        cmap=sns.color_palette("viridis", as_cmap=True),
        xticklabels=True,
        yticklabels=True,
    )

    plt.xticks(rotation=90, fontsize=6)
    plt.yticks(rotation=0, fontsize=6)
    print(len(data.columns))
    plt.tight_layout()
    path = os.path.join("../figures", "jaccard_heatmap.svg")
    # plt.savefig(path)
    plt.show()


def plot_jaccard(data):
    jaccard_matrix = pd.DataFrame(index=data.columns, columns=data.columns, dtype=float)
    for pair in combinations(data.columns, 2):
        jaccard_index = 1 - jaccard(data[pair[0]], data[pair[1]])
        jaccard_matrix.at[pair[0], pair[1]] = jaccard_index
        jaccard_matrix.at[pair[1], pair[0]] = jaccard_index

    for col in data.columns:
        jaccard_matrix.at[col, col] = 1

    plt.figure(figsize=(10, 10))
    plt.title("Jaccard Indices between Symptom Vectors")

    # Create a heatmap
    sns.heatmap(
        jaccard_matrix,
        annot=False,
        cmap=sns.color_palette("viridis", as_cmap=True),
        xticklabels=True,
        yticklabels=True,
    )

    plt.xticks(rotation=90, fontsize=6)
    plt.yticks(rotation=0, fontsize=6)
    print(len(data.columns))
    plt.tight_layout()
    path = os.path.join("../figures", "jaccard_heatmap.svg")
    # plt.savefig(path)
    plt.show()


if __name__ == "__main__":

    data = data_processing.prepare_data()
    plot_spearson(data)
