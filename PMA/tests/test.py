import pytest


class Test_Pytest():
    def test_one(self):
        print("Test method 1 implementation")

    assert 2 == 2

    def test_two(self):
        print("Test method 2 implementation")

    def test_three(self):
        print("Test method 2 implementation")


if __name__ == "__main__":
    pytest.main(['app.py'])

