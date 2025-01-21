import figuras as fg

def test_cubo():
    assert fg.Cubo(3).volumen() == 27
    assert fg.Cubo(0).volumen() == 0
    assert fg.Cubo(-1).volumen() == 0
    assert fg.Cubo(3).area() == 54
    assert fg.Cubo(0).area() == 0
    assert fg.Cubo(-1).area() == 0

def test_cuboide():
    assert fg.Cuboide(3,4,5).volumen() == 60
    assert fg.Cuboide(0,4,5).volumen() == 0

def test_esfera():
    assert round(fg.Esfera(4).volumen(),2) == 268.08
    assert fg.Esfera(0).volumen() == 0
    assert fg.Esfera(-1).volumen() == 0