'''Programa para calculo de emissão de CO² e geração de creditos de carbono'''

#Funções
def ver(a,b):    #função para verificar se a string fornecida é valida
    if a in b:
        return True
    else:
        return False


def dados (a):   # função para entrada de dados da frota na biblioteca
    frota[veiculo]['qtdVeiculo'] = int(input('Qual a quantidade de veiculos na sua frota?: ')) 
    frota[veiculo]['consumoKml'] = float(input('Qual a média de consumo por veiculo em km/l?: '))
    frota[veiculo]['kmRodado'] = float(input('Qual a média de km mensal percorrido por veiculo?: '))
    frota[veiculo]['emissao'] = ((frota[veiculo]['qtdVeiculo'] * frota[veiculo]['kmRodado']) / frota[veiculo]['consumoKml'])*a    #processamento da emissão de CO² da frota      


#programa principal
opcFim = ('S','N')


while opcFim != 'N': #lopping pricipal para repetição de calculo caso desejado
    emissao = 0
    frota = {'moto':{'co2L':0, 'qtdVeiculo': 0, 'consumoKml': 0, 'kmRodado': 0, 'emissao': 0},
              'carro':{'co2L': 0, 'qtdVeiculo': 0, 'consumoKml': 0, 'kmRodado': 0, 'emissao': 0},
                'onibus': {'co2L': 0, 'qtdVeiculo': 0,'consumoKml': 0, 'kmRodado': 0, 'emissao': 0},
                  'caminhao': {'co2L': 0, 'qtdVeiculo': 0,'consumoKml': 0, 'kmRodado': 0, 'emissao': 0}
                  }
    print('''
    =========================================================================
    ||           C A L C U L O    DE    E M I S S Ã O   DE   CO²           ||
    =========================================================================''')

    while addVeic != 'N':

        print('''
    ==============================
    |      Veiculo utilizado     |
    |        na sua frota        |
    |----------------------------|
    |       1 -  moto            | 
    |       2 -  carro           |
    |       3 -  onibus          |
    |       4 -  caminhão        |
    ==============================''')  #menu de opcçoes de veiculo
    
    
        while True:    #atribuição de emissão de co2 por litro de combustivel queimado
            opcVeiculo = int(input('Digite uma opção de veiculo para calculo: '))
            print('=' * 72)
            match opcVeiculo:
                case 1:
                    veiculo = 'moto'
                    frota[veiculo]['co2L'] = 2.40
                    dados(frota[veiculo]['co2L'])
                    break
                case 2:
                    veiculo = 'carro'
                    print('''
    ==============================
    |   O combustivel utilizado  | 
    |  na sua frota de carros é: |
    |----------------------------|
    |       1 - gasolina         |
    |       2 -  etanol          |
    |============================| 
                            ''')  #menu de opçções de combustivel para carro
                    while True:
                        combustivelC = int(input('Digite uma opção de combustivel: '))
                        match combustivelC:
                            case 1:
                                frota[veiculo]['co2L'] = 1.70
                                dados(frota[veiculo['co2L']])
                                break
                            case 2: 
                                frota[veiculo]['co2L'] = 0.9
                                dados(frota[veiculo['co2L']])
                                break
                            case _:
                                print('Opção invalida!')
                case 3:
                    frota[veiculo]['co2L'] = 3.20
                    dados(frota[veiculo['co2L']])
                    break
                case 4:
                    frota[veiculo]['co2L'] = 3.20
                    dados(frota[veiculo['co2L']])
                    break
                case _:
                    print('Opção invalida!')

        while True:
            print('=' * 72)
            addVeic = input('Sua frota possui algum outro tipo de veiculo? [S/N]: ').strip().upper()[0]
            print('=' * 72)
            if ver(addVeic,opcFim) == True:     #verificação de opção valida
                if addVeic == 'N':
                    break
            else:
                print('Opção invalida!')
                
    
''' print('-' * 73)     #apresentação da emissão da frota 
    print(f'A quantidade média de CO² emitida pela sua frota é de {emissao/1000 if emissao > 1000 else emissao:.0f}','tonelada(s)' if emissao > 1000 else 'quilo(s)', 'por mês.') 
    print('=' * 72)'''

    opcMeta = input('Você possui uma meta de redução? [S/N]: ').strip().upper()[0] #Questionamento para iniciar segunda parte do código
    print('=' * 72)
    
    while True:    #lopping da segunda parte do código

        if ver(opcMeta,opcFim) == True:     #verificação de opção valida
            if opcMeta == 'N':
                break
                print('-' * 73)
            
            
            else:       #coleta de dados
                metaImposta = float(input('Digite sua meta imposta em %: '))
                metaDesejada = float(input('Digite a que você  imagina que ira alcaçar em %: '))
 
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
    
    
    fimCodigo = input('Gostaria de fazer um novo calculo de emissão? [S/N]: ').strip().upper()[0]  #opção de novo calculo caso desejado
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
