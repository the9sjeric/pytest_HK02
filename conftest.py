import pytest

@pytest.fixture(scope="function")
def testadd():
    print("\n--->加法add测试__开始计算")
    yield
    print("\n--->加法add测试__结束计算")

@pytest.fixture(scope="function")
def testsub():
    print("\n--->减法sub测试__开始计算")
    yield
    print("\n--->减法sub测试__结束计算")

@pytest.fixture(scope="function")
def testmul():
    print("\n--->乘法mul测试__开始计算")
    yield
    print("\n--->乘法mul测试__结束计算")

@pytest.fixture(scope="function")
def testdiv():
    print("\n--->除法div测试__开始计算")
    yield
    print("\n--->除法div测试__结束计算")



