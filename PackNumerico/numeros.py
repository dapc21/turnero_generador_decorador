def turno(codigo):
    numero = 1

    while True:
        yield f"{codigo}-{numero}"
        numero += 1


def saludo_en_turno(generador):

    def saludo_turnero():
        print("===========================")
        print("     FARMACIA PYTHON")
        print("===========================")
        print("      Su turno es:")
        turno_actual = next(generador)
        print(f"          {turno_actual}")
        print("  Aguarde y será atendido")
        print("===========================")
    return saludo_turnero
