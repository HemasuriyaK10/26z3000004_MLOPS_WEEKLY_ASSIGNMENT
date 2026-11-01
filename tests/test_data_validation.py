import pandas as pd

df = pd.read_csv("data/iris.csv")


def test_columns_exist():

    expected_columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species"
    ]

    assert list(df.columns) == expected_columns


def test_no_missing_values():

    assert df.isnull().sum().sum() == 0


def test_feature_ranges():

    assert df["sepal_length"].between(0, 10).all()
    assert df["sepal_width"].between(0, 10).all()
    assert df["petal_length"].between(0, 10).all()
    assert df["petal_width"].between(0, 10).all()


def test_species_exists():

    assert df["species"].nunique() == 3
