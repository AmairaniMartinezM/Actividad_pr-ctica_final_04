from typing import Iterable, List, Dict, Union
import statistics

Number = Union[int, float]

def funcionX(datos: Iterable[Number]) -> Dict[str, Union[int, float]]:

    if not hasattr(datos, "__iter__"):
        raise ValueError("La entrada debe ser una colección iterable de números.")
    valores: List[Number] = [float(x) for x in datos]
    if not valores:
        raise ValueError("La colección no debe estar vacía.")
    return {
        "count": len(valores),
        "sum": sum(valores),
        "mean": statistics.mean(valores),
        "median": statistics.median(valores),
        "min": min(valores),
        "max": max(valores),
    }

if __name__ == "__main__":
    ejemplo = [10, 20, 30, 40, 50]
    print(funcionX(ejemplo))