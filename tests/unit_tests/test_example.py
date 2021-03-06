from pyspark_examples import example


def test_hello_world():
    """Tests hello_world function"""
    assert example.hello_world() == "Hello, World."


def test_rdd_from_list(test_spark):
    """Tests the rdd_from_list() function"""
    # setup
    input_list = [1, 2, 3]
    # execution
    rdd = example.rdd_from_list(test_spark, input_list)
    # validation
    assert rdd.count() == 3
    assert rdd.sum() == 6


def test_word_count(test_spark):
    """Tests the word_count() function"""
    # setup
    input_list = ["a", "b", "c", "a", "a", "b", "c", "d"]
    expected = {("a", 3), ("c", 2), ("d", 1), ("b", 2)}
    rdd = example.rdd_from_list(test_spark, input_list)
    # execution
    counts = example.word_count(rdd)
    # validation
    assert counts.count() == 4
    assert set(counts.collect()) == expected


def test_parse_words(test_spark):
    """Test the parse_words() function"""
    # setup
    input_text = [
        "A b,  c",
        "f B d. e",
        " a c a?",
    ]
    stop_words = ["e", "f"]
    rdd = example.rdd_from_list(test_spark, input_text)
    # execution
    output = example.parse_words(rdd, stop_words).collect()
    # validation
    for word in output:
        assert word in ["a", "b", "c", "d"]
