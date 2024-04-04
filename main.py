import sys

def cifrar_cesar(texto, desplazamiento):
    texto_cifrado = ''
    for caracter in texto:
        if caracter.isalpha():  # Verifica si el carácter es una letra
            mayuscula = caracter.isupper()
            caracter = caracter.lower()  # Convertir a minúscula para hacer el cifrado
            codigo = ord(caracter) + desplazamiento
            if codigo > ord('z'):
                codigo -= 26
            elif codigo < ord('a'):
                codigo += 26
            caracter_cifrado = chr(codigo)
            if mayuscula:
                caracter_cifrado = caracter_cifrado.upper()  # Restaurar mayúsculas si es necesario
            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += caracter  # Mantener los caracteres no alfabéticos
    return texto_cifrado

def descifrar_cesar(texto_cifrado, desplazamiento):
    return cifrar_cesar(texto_cifrado, -desplazamiento)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Mal escrito el corrimiento o palabra")
        sys.exit(1)

    texto_original = sys.argv[1]
    desplazamiento = int(sys.argv[2])
    texto_cifrado = cifrar_cesar(texto_original, desplazamiento)
    texto_decifrado = descifrar_cesar(texto_cifrado, desplazamiento)
    print(texto_cifrado)
