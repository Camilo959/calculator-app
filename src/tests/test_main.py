from src.main import sumar, restar, multiplicar

# Comentario para las pruebas
def test_sumar():
    resultado = sumar(5, 10)
    assert resultado ==  15

def test_restar():
    resultado = restar(10, 6)
    assert resultado ==  4

def test_multiplicar():
    resultado = multiplicar(5, 5)
    assert resultado ==  25