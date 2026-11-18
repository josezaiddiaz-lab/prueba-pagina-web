import random

def lanzar_dado():
    resultado = random.randint(1, 6)
    print(f"¡El código funciona! Has sacado un: {resultado}")

if __name__ == "__main__":
    lanzar_dado()
