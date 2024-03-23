### Problemas y Soluciones

## 1. Desconocimiento para realizar el algoritmo Cesar
Para poder realizar y emplear el algoritmo Cesar se tuvo que recurrir a diferentes lecturas, pudiendo asi implementar el cifrado de manera exitosa. 
## 2. Mal envio de paquetes (no seq, sin payload)
Al principio no se visualizaba la data de los paquetes en el trafico, esto debido a que solo se estaba usando el metodo ICMP(), cuando habia que definir la secuencia de cada caracter con su id, una vez realizado esto se pudo realizar esta parte de la actividad (Stealth) sin problemas.
## 3. No visualizar trafico en ip loopback
Al revisar la rubrica de evaluacion se dio cuenta de que el trafico apuntaba a ip de loopback, por lo que se tuvo que cambiar de 1.1.1.1 a 127.0.0.1. Sin embargo no se visualizaban los paquetes, por lo que al buscar en la documentacion de wireshark se indico que para pode revisar el trafico de este medio era necesario indicarlo en la captura en la pagina principal.
## 4. Visualizar el doble de paquetes
Al momento de realizar el ping del paso dos (Stealth), se podian visualizar el doble de paquetes, siendo la unica diferencia el atributo 'Info' donde la mitad eran reply y otros request. Por lo que al hacer el decifrado se tuvo que indicar que solo considerara los que fueran de tipo reply, aunque se intento cambiar en el codigo para solo emitir con sr (Send and receive packets) el problema se mantuvo, por lo que fue necesario realizar lo indicado anteriormente. 

```
icmp_packets = [pkt for pkt in packets if ICMP in pkt and pkt[ICMP].type == 0]
```