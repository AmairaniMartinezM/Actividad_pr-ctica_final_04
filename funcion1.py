def funcion1(valor):

    if isinstance(valor, (list, tuple)):
        return sum(valor)
    try:
        return float(valor)
    except (TypeError, ValueError):
        raise ValueError("Entrada no válida para funcion1")
    
if __name__ == "__main__":
    print(funcion1([1, 2, 3]))