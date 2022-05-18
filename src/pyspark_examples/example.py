import string
from typing import Optional

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
    counts = rdd.map(lambda word: (word, 1))
    counts = counts.reduceByKey(lambda a, b: a + b)
    return counts


def parse_words(rdd: RDD, stop_words: Optional[list] = None) -> RDD:
    """Split lines of text file into words and filter out stop words"""
    # split lines into words then remove punctuation
    words = (
        rdd.flatMap(lambda line: line.split())
        .map(lambda word: word.lower())
        .map(lambda word: word.strip(string.punctuation))
    )
    if stop_words:
        sc = rdd.context  # get the spark context for the rdd
        exclude_list = sc.broadcast(stop_words)
        words = words.filter(lambda word: word not in exclude_list.value)
    return words
