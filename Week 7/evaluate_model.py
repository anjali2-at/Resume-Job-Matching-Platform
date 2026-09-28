import pandas as pd


def load_dataset(file_path):
    """
    Load the evaluation dataset.
    """
    return pd.read_csv(file_path)


def show_dataset_summary(dataset):
    """
    Display basic information about the dataset.
    """

    print("\n===== Evaluation Summary =====")

    print("Total test cases:", len(dataset))

    print("\nExpected match categories:")
    print(dataset["expected_match"].value_counts())


if __name__ == "__main__":

    file_path = "Week 7/evaluation_dataset.csv"

    dataset = load_dataset(file_path)

    show_dataset_summary(dataset)