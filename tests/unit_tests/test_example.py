from pyspark_examples.example import hello_world, rdd_from_list


def test_hello_world():
    """Tests hello_world function"""
    assert hello_world() == "Hello, World."


def test_rdd_from_list(test_spark):
    """Tests the rdd_from_list function"""
    # setup
    input_list = [1, 2, 3]
    # execution
    rdd = rdd_from_list(test_spark, input_list)
    # validation
    assert rdd.count() == 3
    assert rdd.sum() == 6
