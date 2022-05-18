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


def word_count(rdd: RDD) -> RDD:
    """Finds the frequency of each item in the RDD"""
    counts = (
        rdd.map(lambda word: word.lower())  # make lowercase to avoid dupes
        .map(lambda word: (word, 1))  # map words to 1 to sum frequency
        .reduceByKey(lambda a, b: a + b)  # sum the frequencies of each word
    )
    return counts
