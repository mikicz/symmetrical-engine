import time
import pytest


@pytest.mark.parametrize("variant", ["a", "b"])
class TestSomething:
    @pytest.fixture(autouse=True)
    def some_fixture(self, variant):
        time.sleep(10)  # generate the object using the variant fixture
        pass

    def test_1(self, some_fixture):
        pass

    def test_2(self, some_fixture):
        pass
