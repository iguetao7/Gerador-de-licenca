import random
import os



fonte = 'ABCDEFGHIJKLMNOPQRSTUVWYZ0123456789'
licencas_geradas = 0
quantidade_licencas = int(input('Quantas licenças dever ser geradas? '))
licencas = []

while licencas_geradas < quantidade_licencas:
    licenca = (f'{random.choices(fonte, k=5)}-{random.choices(fonte, k=5)}-{random.choices(fonte, k=5)}-'
               f'{random.choices(fonte, k=5)}-{random.choices(fonte, k=5)}')

    licenca_limpa = (licenca.replace('[', '').replace(']', '').replace(',', '')
                     .replace("'", "").replace(' ', ''))

    licencas_geradas += 1
    licencas.append(licenca_limpa)

    with open('licenca.txt', 'w', newline='') as arquivo:
        arquivo.writelines(os.linesep.join(licencas))

    print('Finalizado')
