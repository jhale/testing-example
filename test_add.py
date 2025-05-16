import pytest
from add import add
import time

@pytest.mark.parametrize("a,b,result", ((3, 9, 12), (-4, -8, -12), (-20, -40, -60)))
def test_add(a, b, result):
    assert add(a, b) == result

def test_failure_on_string():
    with pytest.raises(TypeError):
        c = add(4, "b")

@pytest.mark.slow
def test_slow_test():
   time.sleep(5) 
