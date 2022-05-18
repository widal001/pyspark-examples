from pyspark_examples.example import hello_world


def test_hello_world():
    """Tests hello_world function"""
    assert hello_world() == "Hello, World."
