#!/usr/bin/env python3
import sys

def exponenciacion_binaria(M, e, n):
    """
    Calcula C = M^e mod n usando el algoritmo de exponenciación binaria.
    """
    e_bin = bin(e)[2:]  # Convertir exponente a binario
    k = len(e_bin)
    
    # Inicialización
    C = M if e_bin[0] == '1' else 1
    
    for i in range(1, k):
        C = (C * C) % n
        if e_bin[i] == '1':
            C = (C * M) % n
            
    return C

def obtener_entrada():
    """
    Obtiene los valores M, e, n desde argv o stdin.
    Devuelve tupla (M, e, n) o None si hay error.
    """
    # Intentar desde argumentos
    if len(sys.argv) == 4:
        try:
            return int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        except ValueError:
            return None
    else:
        # Intentar desde stdin
        try:
            linea = input().strip()
            return tuple(map(int, linea.split()))
        except Exception:
            return None

def main():
    entrada = obtener_entrada()
    if entrada is None or len(entrada) != 3:
        # Entrada inválida → imprimimos 0 (o un valor que no cause error)
        print(0)
        return

    M, e, n = entrada
    resultado = exponenciacion_binaria(M, e, n)
    print(resultado)

if __name__ == "__main__":
    main()