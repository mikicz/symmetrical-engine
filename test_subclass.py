import abc
import time
import pytest


class BaseSomethingTest(abc.ABC):
    @property
    @abc.abstractmethod
    def variant(self):
        pass

    @pytest.fixture(scope="class", autouse=True)
    def some_fixture(self):
        time.sleep(10)  # generate the object using self.variant
        pass

    def test_1(self, some_fixture):
        pass

    def test_2(self, some_fixture):
        pass


class TestSomethingA(BaseSomethingTest):
    variant = "a"


class TestSomethingB(BaseSomethingTest):
    variant = "b"
