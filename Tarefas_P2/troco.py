def troco():
    #verificando condições do input e armazenando na variável "valor"(float)
    while True:
        try:
            valor = float(input('valor: '))
            break
        except ValueError:
            print('input inválido')
          
    #criando as listas de notas e moedas disponíveis
    notas = [100,50,20,10,5,2]
    moedas = [1,0.50,0.25,0.10,0.05,0.01]

    #removendo o "." da variável "valor"(float) para separar-lá 
    #em outras duas variáveis: "reais" e "centavos"
    reais = int(str(valor).split('.')[0])
    centavos = valor - reais

    
    print('Notas:')
    #iterando sobre a lista notas para verificar quantas notas podem
    #ser usadas para o troco
    for i in range(len(notas)):
        if reais >= notas[i]:
            num_notas = reais//notas[i]
            reais -= notas[i]*num_notas
            print(f'{num_notas} notas(s) de R${float(notas[i]):.2f}')
        else:
            num_notas = 0
            print(f'{num_notas} notas(s) de R${float(notas[i]):.2f}')
    
    print('\nMoedas:')
    #iterando sobre a lista notas para verificar quantas notas podem
    #ser usadas para o troco
    for i in range(len(moedas)):
        if reais != 0:
            num_moedas = 1
            reais -= 1
            print(f'{num_moedas} moeda(s) de R${moedas[i]:.2f}')
        elif centavos >= moedas[i]:
            num_moedas = centavos//moedas[i]
            centavos -= moedas[i]*num_moedas
            print(f'{int(num_moedas)} moeda(s) de R${moedas[i]:.2f}')
        else:
            num_moedas = 0
            print(f'{num_moedas} moedas(s) de R${moedas[i]:.2f}')
    
troco()
