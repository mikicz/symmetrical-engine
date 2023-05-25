import time

import pytest


def generate_fixture(someparam):
    @pytest.fixture(scope="class")
    def my_fixture(self):
        return someparam

    return my_fixture


def generate_tests_cls_parametrize(cls: type, parameter_names: list[str], values: list[list], ids: list[str]):
    base_cls_name = "Test" + cls.__name__.removeprefix("Base").removesuffix("Test")
    for test_values, test_id in zip(values, ids, strict=True):
        cls_name = base_cls_name + test_id
        globals()[cls_name] = type(
            cls_name,
            (cls,),
            {
                parameter_name: generate_fixture(value)
                for parameter_name, value in zip(parameter_names, test_values, strict=True)
            },
        )


class BaseSomethingTest:
    @pytest.fixture(scope="class", autouse=True)
    def some_fixture(self, variant):
        time.sleep(10)  # generate the object using the variant fixture
        pass

    def test_1(self, some_fixture):
        pass

    def test_2(self, some_fixture):
        pass


generate_tests_cls_parametrize(
    BaseSomethingTest,
    ["variant"],
    [["a"], ["b"]],
    ["A", "B"],
)
