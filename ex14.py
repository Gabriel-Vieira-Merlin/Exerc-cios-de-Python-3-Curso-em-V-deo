#Armazena a temperatura em Celsius
temperaturaC = float(input('Informe a temperatura em Celsius (ºC): '))

#Converte as temperaturas em Farenheit
temperaturaF = temperaturaC * 1.8 + 32

#Converte as temperaturas em Kelvin
temperaturaK = temperaturaC + 273.15

print(f'{temperaturaC}ºC equivale a {temperaturaF}ºF e {temperaturaK}K.')