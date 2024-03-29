import pytest
from interpreter import Interpreter


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:
    interpreter = Interpreter()

    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4
    
    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")
            interpreter.eval("t+2")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")

    def test_unary_plus(self, interpreter):
        assert interpreter.eval("+3") == 3
    
    def test_unary_minus(self, interpreter):
        assert interpreter.eval("-3") == -3
        assert interpreter.eval("--3") == 3
    
    def test_mixed_unary(self, interpreter):
        assert interpreter.eval("-+3") == -3
        assert interpreter.eval("+-3") == -3
    
    def test_unary_with_binary(self, interpreter):
        assert interpreter.eval("-3 + 5") == 2
        assert interpreter.eval("--3 + 5") == 8
            
    @pytest.mark.parametrize(
            "interpreter, code", [(interpreter, "2 + 2"),
                                  (interpreter, "2 +2 "),
                                  (interpreter, " 2+2")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4
