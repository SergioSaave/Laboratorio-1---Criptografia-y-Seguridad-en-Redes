import sys
import time
from scapy.all import IP, ICMP, send

def buildICMP(data, id, seq):
    # Construye un paquete ICMP con los datos especificados
    payload = data.ljust(48, ' ')
    dataICMP = bytes(payload, 'utf-8')
    packetICMP = IP(dst='127.0.0.1') / ICMP(id=id, seq=seq) / dataICMP
    # packetICMP = IP(dst='127.0.0.1', ts=round(time.time())) / ICMP(id=id, seq=seq) / dataICMP
    return packetICMP

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python icmp_sender.py <Mensaje>")
        sys.exit(1)
    message = sys.argv[1]
    id_counter = 1
    seq_counter = 1
    for char in message:
        packetICMP = buildICMP(char, id_counter, seq_counter)
        send(packetICMP)
        seq_counter += 1
        time.sleep(1)