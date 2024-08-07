import Calc_logic as c
import pytest

def test_add():
    assert c.add(10, 5) == 15
    assert c.add(-1, 1) == 0
    assert c.add(-2, -2) == -4

    with pytest.raises(TypeError):
        c.add("text", 1)
        c.add(1, "text")
def test_sub():
    assert c.sub(10, 5) == 5
    assert c.sub(-10, 5) == -15
    assert c.sub(-10, -5) == -5
    assert c.sub(10, -5) == 15

    with pytest.raises(TypeError):
        c.sub("text", 1)
    with pytest.raises(TypeError):
        c.sub(1, "text")

def test_multy():
    assert c.multy(10, 5) == 50
    assert c.multy(-10, 5) == -50
    assert c.multy(-10, -5) == 50
    assert c.multy(10, -5) == -50


def test_div():
    assert c.div(10, 2) ==5
    assert c.div(-10,  2) ==-5
    assert c.div(10, -2) ==-5
    assert c.div(-10, -2) == 5

    with pytest.raises(TypeError):
        c.div("text", 1)
    with pytest.raises(TypeError):
        c.div(1, "text")
    with pytest.raises(ValueError):
        c.div(10, 0)

test_add()
test_sub()
test_multy()
test_div()

print("Тесты пройдены успешно!")



