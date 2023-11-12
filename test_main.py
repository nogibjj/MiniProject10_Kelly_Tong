"""
PySpark Application Test Suite for Car Data
"""
from pyspark.sql.session import SparkSession
import pytest
from mylib.lib import (
    initiate_spark_session,
    read_dataset,
    describe,
    transform_origin,
)


@pytest.fixture(scope="session")
def spark_session():

    session = initiate_spark_session("TestWomenDataProcessing")
    yield session
    session.stop()


def test_data_loading(spark_session: SparkSession):
    data_path = "data/women_stem.csv"
    women_df = read_dataset(spark_session, data_path)
    assert women_df is not None and women_df.count() > 0


def test_data_describe(spark_session: SparkSession):
    women_df = read_dataset(spark_session, "data/women_stem.csv")
    description_data = describe(women_df)
    assert description_data is not None


def test_data_transform(spark_session: SparkSession):
    women_df = read_dataset(spark_session, "data/women_stem.csv")
    transformed_women_df = transform_origin(women_df)
    assert transformed_women_df is not None
    assert "Major_category" in transformed_women_df.columns


def run_tests():
    session = spark_session()
    test_data_loading(session)
    test_data_loading(session)
    test_data_transform(session)


if __name__ == "__main__":
    run_tests()
