from decimal import Decimal, InvalidOperation

def validar_calificacion(valor):
    # TODO: rechazar valores nulos, booleanos, texto no numérico, NaN, Infinity, fuera de 0..100 y >2 decimales.
    # No redondear entradas incorrectas.
    if valor is None or isinstance(valor, bool):
        raise ValueError("Calificación inválida")
    if isinstance(valor, str):
        if not valor.strip() or valor != valor.strip():
            raise ValueError("Calificación inválida")
    elif not isinstance(valor, (int, float, Decimal)):
        raise TypeError("Tipo de calificación inválido")

    try:
        calificacion = Decimal(str(valor))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError("Calificación inválida") from exc

    if not calificacion.is_finite():
        raise ValueError("Calificación inválida")

    if calificacion < Decimal("0") or calificacion > Decimal("100"):
        raise ValueError("Calificación fuera de rango")

    if calificacion.as_tuple().exponent < -2:
        raise ValueError("Demasiados decimales")

    return calificacion
