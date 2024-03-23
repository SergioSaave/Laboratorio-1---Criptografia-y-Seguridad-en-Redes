import sys
from scapy.all import *
from colorama import init, Fore

def decrypt_cesar(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            if char.isupper():
                decrypted_char = chr(((char_code - 65 - shift) % 26) + 65)
            else:
                decrypted_char = chr(((char_code - 97 - shift) % 26) + 97)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

# Comprobar si se proporciona la ubicación del archivo pcapng
if len(sys.argv) != 2:
    print("Uso: python3 decrypt_pcap.py archivo.pcapng")
    sys.exit(1)

# Leer el archivo pcapng
file_path = sys.argv[1]
packets = rdpcap(file_path)

icmp_packets = [pkt for pkt in packets if ICMP in pkt and pkt[ICMP].type == 0]

# Obtener el primer byte de los paquetes ICMP y concatenarlos
message_bytes = b"".join([pkt[Raw].load[:1] for pkt in icmp_packets])

init()
init(autoreset=True)

for shift in range(26):
    decrypted_message = decrypt_cesar(message_bytes.decode(), shift)
    if(decrypted_message == "criptografia y seguridad en redes"): 
        print( Fore.GREEN + f"{shift}: {decrypted_message}")
    else: 
        print(f"{shift}: {decrypted_message}")