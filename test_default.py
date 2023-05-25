import pytest
import time


class TestSomething:
    @pytest.fixture(scope="class", autouse=True)
    def some_fixture(self):
        time.sleep(10)  # let's say this takes ten seconds, e.g. creating some object in the database
        pass

    def test_1(self, some_fixture):
        pass

    def test_2(self, some_fixture):
        pass
