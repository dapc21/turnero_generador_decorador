import os
from PackNumerico import  numeros

# Generadores únicos
turno_perfumeria = numeros.turno("P")
turno_farmacia = numeros.turno("F")
turno_cosmetica = numeros.turno("C")

# Funciones decoradas
turno_p = numeros.saludo_en_turno(turno_perfumeria)
turno_f = numeros.saludo_en_turno(turno_farmacia)
turno_c = numeros.saludo_en_turno(turno_cosmetica)

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pausa para volver al menú
def pausar():
    input("\nPresiona Enter para volver al menú...")

def inicio():

    # Loop principal del programa
    while True:
        # Limpiar pantalla
        limpiar_pantalla()

        print("\nEscoja la categoría para generar un ticket: ")
        print("1. Perfumería")
        print("2. Farmacia")
        print("3. Cosmética")
        print("4. Salir\n")

        try:

            opcion = int(input("Elige una opción: "))

            limpiar_pantalla()

            if opcion == 1:
                turno_p()
                pausar()

            elif opcion == 2:
                turno_f()
                pausar()

            elif opcion == 3:
                turno_c()
                pausar()

            elif opcion == 4:
                print("¡Gracias por usar nuestro turnero de Farmacia Python!")
                break

            else:
                print("Opción no válida. Elige un número del 1 al 4.")
                pausar()

        except ValueError:
            limpiar_pantalla()
            print("Error: Debes ingresar un número válido.")
            pausar()

# Para ejecutar el programa
if __name__ == "__main__":
    inicio()