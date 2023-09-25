import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_training_data():
    # column_names = ['feature1', 'feature2', 'feature3', ..., 'gesture_name', 'gesture_id', 'candidate']
    feature_names = [f"feature_{i}" for i in range(1, 243)]  # 242 feature columns
    data = pd.read_csv('datasets/train-final.csv', header=None, names=feature_names)
    data.rename(columns={
        data.columns[-2]: 'gesture name',
        data.columns[-1]: 'gesture ID'

    }, inplace=True)
    return data


def load_test_data():
    # Give the columns names
    feature_names = [f"feature_{i}" for i in range(1, 243)]  # 242 feature columns
    data = pd.read_csv('datasets/test-final.csv', header=None, names=feature_names)
    data.rename(columns={
        data.columns[-2]: 'gesture name',
        data.columns[-1]: 'gesture ID'

    }, inplace=True)
    return data


def check_missing_values(_input: pd.DataFrame):
    missing_values = _input.isnull().sum()
    columns_with_missing_values = missing_values[missing_values > 0]
    print("Missing values")
    print(columns_with_missing_values)


def print_heatmap(_input: pd.DataFrame, _name: str):
    plt.figure(figsize=(12, 5))
    sns.heatmap(_input.isnull(), cmap='viridis', cbar=True, yticklabels=False)
    plt.title(_name)
    plt.show()


def plot_boxplot(_input: pd.DataFrame, _name: str):
    _input.boxplot(figsize=(12, 8))
    plt.xticks(rotation=90)  # Rotate x labels
    plt.title(_name)
    plt.show()


if __name__ == '__main__':
    # Load the training data
    train_d = load_training_data()
    # convert into dataFrame
    train_data = pd.DataFrame(train_d)

    # load the test data
    test_d = load_test_data()
    # convert to dataFrame
    test_data = pd.DataFrame(test_d)

    # Check for missing values
    print("Checking train_data")
    check_missing_values(train_data)
    print_heatmap(train_data, "Missing data points in train-final.csv")
    print("Check test_data")
    check_missing_values(test_data)
    print_heatmap(test_data, "Missing data points in test-final.csv")

    # Assign data for training
    X = train_data.drop(columns=['gesture name', 'gesture ID'])
    y = train_data['gesture ID']  # gesture ID as the target label
    X.fillna(X.mean(), inplace=True)
    # X.dropna(inplace=True)

    # Assign data for testing
    test_data.dropna(inplace=True)  # Just drop rows missing testdata
    X_test = test_data.drop(columns=['gesture name', 'gesture ID'])
    y_test = test_data['gesture ID']  # gesture ID as  target label
    X_test.fillna(X.mean(), inplace=True)

    positions_data = X.iloc[:, :60]  # first 60 columns
    cosine_angles_data = X.iloc[:, 60:120]  # next 60 columns
    mean_positions_data = X.iloc[:, 120:180]  # next 60 columns
    std_positions_data = X.iloc[:, 180:240]  # next 60 columns

    # Print out a plot
    plot_boxplot(positions_data, 'positions data')
    plot_boxplot(cosine_angles_data, 'cosine angles data')
    plot_boxplot(mean_positions_data, 'mean positions data')
    plot_boxplot(std_positions_data, 'std positions data')

