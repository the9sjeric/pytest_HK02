import pytest

from calc_code.calculator import Calculator

#创建测试类 TestCalc.
class TestCalc:

    # 实例化类,生成类的对象
    def setup_class(self):
        self.calc = Calculator()

    #  测试加法，为测试用例预设参数（参数化）
    @pytest.mark.parametrize("a,b,expected", [(3, 7, 10), (-1, -8, -9), (14, -6, 8),(0.5, 1.6, 2.1), (5, 5 , 9)],
                             ids=("Posi", "Nega", "Posi&Nega", "Float", "Errortestcase"))
    @pytest.mark.run(order=1)
    # 调用fixture函数,以及预设参数
    def test_add(self, testadd, a, b, expected):
        # 调用add函数,返回的结果保存在result里面（下同）
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值（下同）
        assert result == expected

    # 测试除法，，为测试用例预设参数（参数化）
    @pytest.mark.parametrize("a,b,expected", [(20, 5, 4), (-24, -2, 12), (36, -9, -4), (8.8, 1.6, 5.5), (5, 0, 9)],
                             ids=("Posi", "Nega", "Posi&Nega", "Float", "Errortestcase"))
    @pytest.mark.run(order=4)
    # 调用fixture函数,以及预设参数
    def test_div(self, testdiv, a, b, expected):
        result = self.calc.div(a, b)
        assert result == expected

    # 测试减法，，为测试用例预设参数（参数化）
    @pytest.mark.parametrize("a,b,expected", [(66, 22, 44), (-11, -19, 8), (-6, 9, -15), (8.5, 5.5, 3), (5, 5 , 9)],
                             ids=("Posi", "Nega", "Posi&Nega", "Float", "Errortestcase"))
    # 使用fixture装饰器
    @pytest.mark.usefixtures('testsub')
    @pytest.mark.run(order=2)
    def test_sub(self, a, b, expected):
        result = self.calc.sub(a, b)
        assert result == expected

    # 测试乘法，，为测试用例预设参数（参数化）
    @pytest.mark.parametrize("a,b,expected", [(3, 7, 21), (-3, -8, 24), (14, -6, -84), (0.5, 9.6, 4.8), (5, 5 , 9)],
                             ids=("Posi", "Nega", "Posi&Nega", "Float",  "Errortestcase"))
    # 使用fixture装饰器
    @pytest.mark.usefixtures('testmul')
    @pytest.mark.run(order=3)
    def test_mul(self, a, b, expected):
        result = self.calc.mul(a, b)
        assert result == expected

