#Escreva um programa que leia um valor em metros e o exiba convertido.

#Armazena a distância
distancia = float(input('Forneça uma distância em metros: '))

#Faz as conversões das medidas
km = distancia * 0.001
hm = distancia * 0.01
dam = distancia * 0.1
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

#Exibe a resposta para o usuário
print(f'A distância de {distancia}m corresponde a:\n{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm')