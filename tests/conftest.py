import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session", name="test_spark")
def fixture_spark_context():
    """Creates a SparkContext for testing"""
    spark = SparkSession.builder.appName("TestApp").getOrCreate()
    yield spark
    print("Stopping spark session")
    spark.stop()
