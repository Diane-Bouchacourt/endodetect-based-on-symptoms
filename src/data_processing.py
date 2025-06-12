import pandas as pd


def prepare_data():
    data = pd.read_excel("../data/dataset.xlsx")

    y = data["label"].values
    data = data.drop(data.columns[0], axis=1)  # remove first columns
    data = data.drop(["row", "label"], axis=1)
    return data


def create_macros_symptoms(data):
    pass


if __name__ == "__main__":

    data = prepare_data()
