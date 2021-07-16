# Convertendo segundos em dias e horas:
total_segundos = int(input('Digite o número de segundos que deseja converter: '))

dias = total_segundos // 86400
horas_restantes = total_segundos % 86400
horas = horas_restantes // 3600
segundos_restantes = horas_restantes % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

print(f'{dias} Dias, {horas} horas, {minutos} minutos, {segundos_restantes_final} segundos')

# Convertendo horas em segundos:
total_horas = int(input('Digite o total de horas para converter em segundos: '))
segundos = total_horas * 3600

print(f'{total_horas} Horas é igual a {segundos} segundos')
