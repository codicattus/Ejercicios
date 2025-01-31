from decoradores.decoradores_00 import suma_nums

def test_decoradores():
    assert suma_nums(10, 20, 30) == 30
    assert suma_nums(10, 10, 10) == 0