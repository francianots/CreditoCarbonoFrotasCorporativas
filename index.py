'''Programa para calculo de emição de poluentes e creditos de carbono'''


def ver(a,b):
    if a in b:
        return True
    else:
        return False



opcFim = ['S','N']
veiculo = [1,2,3,4]
while opcFim != 'N':

    print('''=========================================================================
||           C A L C U L O    DE    E M I S S Ã O   DE   CO²           ||
=========================================================================''')



    print('''==============================
|    1 -  moto               | 
|    2 -  carro  (gasolina)  |
|    3 -  carro  (etanol)    | 
|    4 -  onibus             |
|    5 -  caminhão           |
==============================''')
    while True:
        opcVeiculo = int(input('Digite uma opção de veiculo para calculo: '))
        match opcVeiculo:
            case 1:
                co2 = 2.40
                break
            case 2:
                co2 = 1.70
                break
            case 3:
                co2 = 0.9
                break
            case 4:
                co2 = 3.20
                break
            case 5:
                co2 = 3.20
                break
            case _:
                print('Opção invalida!')
    print('-' * 73)
    qtdVeiculo = int(input('Qual a quantidade de veiculos na sua frota?: '))
    consumoKml = float(input('Qual a média de consumo por veiculo em km/l?: '))
    kmRodado = float(input('Qual a média de km mensal percorrido por veiculo?: '))
    emissao = ((qtdVeiculo * kmRodado) / consumoKml)*co2
    print('-' * 73)
    print(f'A quantidade média de CO² emitida pela sua frota é de {emissao/1000 if emissao > 1000 else emissao:.0f}','tonelada(s)' if emissao > 1000 else 'quilo(s)', 'por mês.')
    print('-' * 73)
    opcMeta = input('Você possui uma meta de redução? [S/N]: ').strip().upper()[0]
    while True:
        print('-' * 73)
        if ver(opcMeta,opcFim) == True:
            if opcMeta == 'N':
                break
                print('-' * 73)
            else:
                print('-' * 73)
                metaImposta = float(input('Digite sua meta em %: '))
                metaDesejada = float(input('Digite a sua méta desejada em %: '))
                metaImposta = (emissao/100)*metaImposta
                metaDesejada = (emissao/100)*metaDesejada
                print(f'Você precisa reduzir sua emissão de CO² em {metaImposta:.2f}Kg')
                if metaDesejada > metaImposta:
                    print(f'Caso atinja a meta desejada você terá um salde de {(metaDesejada-metaImposta)/1000:.2f} creditos de carbono.')
                elif metaDesejada < metaImposta:
                    print(f'Caso atinja somente a meta desejaja ficara com uma divida de {(metaImposta-metaDesejada)/1000:.2f} creditos de carbono. ')
                print('-' * 73)
                break
        else:
            print('Opção invalida!')
            opcMeta = input('Você possui uma meta de redução? [S/N]: ').strip().upper()[0]
    fimCodigo = input('Gostaria de repetir? [S/N]: ').strip().upper()[0]
    while True:
        if ver(fimCodigo,opcFim) == True:
            if fimCodigo == 'N':
                opcFim = 'N'
                break
            else:
                break
        else:
            print('Opção invalida!')
            fimCodigo = input('Gostaria de repetir? [S/N]: ').strip().upper()[0]
