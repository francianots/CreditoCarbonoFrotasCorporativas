'''Programa para calculo de emissão de CO² e geração de creditos de carbono'''

#Funções
def ver(a,b):    #função para verificar se a string fornecida é valida
    if a in b:
        return True
    else:
        return False


#programa principal
opcFim = ('S','N')


while opcFim != 'N': #lopping pricipal para repetição de calculo caso desejado

    print('''
=========================================================================
||           C A L C U L O    DE    E M I S S Ã O   DE   CO²           ||
=========================================================================''')



    print('''
==============================
|    1 -  moto               | 
|    2 -  carro  (gasolina)  |
|    3 -  carro  (etanol)    | 
|    4 -  onibus             |
|    5 -  caminhão           |
==============================''')  #menu de opcçoes de veiculo
   
   
    while True:    #atribuição da emição de cada tipo de veiculo para calculo
        opcVeiculo = int(input('Digite uma opção de veiculo para calculo: '))
        print('=' * 72)
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


    qtdVeiculo = int(input('Qual a quantidade de veiculos na sua frota?: ')) #entrada de dados da frota 
    consumoKml = float(input('Qual a média de consumo por veiculo em km/l?: '))
    kmRodado = float(input('Qual a média de km mensal percorrido por veiculo?: '))

    emissao = ((qtdVeiculo * kmRodado) / consumoKml)*co2    #processamento da emissão de CO² da frota   


    print('-' * 73)     #apresentação da emissão da frota 
    print(f'A quantidade média de CO² emitida pela sua frota é de {emissao/1000 if emissao > 1000 else emissao:.0f}','tonelada(s)' if emissao > 1000 else 'quilo(s)', 'por mês.') 
    print('=' * 72)


    opcMeta = input('Você possui uma meta de redução? [S/N]: ').strip().upper()[0] #Questionamento para iniciar segunda parte do código
    print('=' * 72)
    
    while True:    #lopping da segunda parte do código

        if ver(opcMeta,opcFim) == True:     #verificação de opção valida
            if opcMeta == 'N':
                break
                print('-' * 73)
            
            
            else:       #coleta de dados
                metaImposta = float(input('Digite sua meta em %: '))
                metaDesejada = float(input('Digite a sua méta desejada em %: '))


                metaImposta = (emissao/100)*metaImposta     #processamento de dados
                metaDesejada = (emissao/100)*metaDesejada
                
                
                print(f'Você precisa reduzir sua emissão de CO² em {metaImposta if metaImposta < 1000 else metaImposta/1000:.0f}', 'tonelada(s)' if metaImposta > 1000 else 'quilos(s)')        #apresentação da redução de emissão necessaria 
                
                
                if metaDesejada > metaImposta:      #apresentação do saldo de creditos caso atinja números esperados
                    print(f'Caso atinja a meta desejada você terá um saldo de {(metaDesejada-metaImposta)/1000:.2f} creditos de carbono.')
                
                
                elif metaDesejada < metaImposta:        #apresentação da divida em creditos caso atinja números esperados
                    print(f'Caso atinja somente a meta desejaja ficara com uma divida de {(metaImposta-metaDesejada)/1000:.2f} creditos de carbono. ')
                
                
                print('-' * 73)
                break
       
        
        else:
            print('Opção invalida!')
            opcMeta = input('Você possui uma meta de redução? [S/N]: ').strip().upper()[0]
    
    
    fimCodigo = input('Gostaria de fazer um novo calculo de emissão? [S/N]: ').strip().upper()[0]  #opção de novo calculo c aso desejado
    while True:
        if ver(fimCodigo,opcFim) == True:       #verificação de opção valida
            if fimCodigo == 'N':
                opcFim = 'N'
                break
            else:
                break
        else:
            print('Opção invalida!')
            fimCodigo = input('Gostaria de fazer um novo calculo de emissão? [S/N]: ').strip().upper()[0]
