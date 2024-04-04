import os
import sys
import time
import struct
import datetime
from scapy.all import IP, ICMP, send, IPOption_Timestamp

def buildICMP(data, id, seq):
    icmp_data = bytes(data + '\x00\x00', 'utf-8')
    icmp_data += b'\x00\x00\x00\x00\x00'
    
    # Obtener timestamp actual en formato UTC
    timestamp_utc = int(time.time())
    
    # Convertir el timestamp a hexadecimal y luego invertir el orden (big-endian)
    timestamp_hex = hex(timestamp_utc)[2:]
    timestamp_bytes = bytes.fromhex(timestamp_hex.rjust(32, '0'))
    timestamp_bytes = timestamp_bytes[::-1]
    
    # Añadir el timestamp antes del payload
    icmp_data = timestamp_bytes + icmp_data
    
    icmp_data += bytes(range(0x10, 0x38))
    payload = icmp_data
    
    packetICMP = IP(dst='127.0.0.1') / ICMP(id=id, seq=seq) / payload
    return packetICMP

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Parametros mal ingresados")
        sys.exit(1)
    message = sys.argv[1]
    id_counter = 1
    seq_counter = 1
    for char in message:
        packetICMP = buildICMP(char, id_counter, seq_counter)
        send(packetICMP)
        id_counter += 1
        seq_counter += 1
        # time.sleep(1)
