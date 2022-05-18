from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.rdd import RDD


def hello_world():
    """Hello world function"""
    return "Hello, World."


def rdd_from_list(spark: SparkSession, input_list: list) -> RDD:
    """Create an RDD from a list"""
    sc: SparkContext = spark.sparkContext
    return sc.parallelize(input_list)
