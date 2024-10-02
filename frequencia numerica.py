def frequencia_numeros():
    numeros = []
  #verifica os inputs e armazena os numeros inteiros na lista "numeros"
    while True:
        num = input("Numero: ")
        if num == 'f':
            break
        else:
            try:
                num = int(num)
                numeros.append(num)
            except ValueError:
                pass
    numeros.sort()

  #faz a contagem dos inteiros da lista "numeros"
    for i in range(len(numeros)):
        try:
            if numeros[i] != numeros[i+1]:
                contagem = numeros.count(numeros[i])
                if contagem > 1:
                    print(f'{numeros[i]} aparece {contagem} vezes')
                else:
                    print(f'{numeros[i]} aparece {contagem} vez')
        except IndexError:
            contagem = numeros.count(numeros[i])
            if contagem > 1:
                print(f'{numeros[i]} aparece {contagem} vezes')
            else:
                print(f'{numeros[i]} aparece {contagem} vez')


frequencia_numeros()
