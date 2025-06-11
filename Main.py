print(
    "Bem-vindo ao treinamento do Perceptron!",
    
    "Você deverá fornecer os valores numéricos de X1, X2 e X3 para 3 objetos,",
    "além do valor esperado de saída (Y) para cada um deles e a taxa de aprendizado do sistema.",
    
    "Com base nesses dados, o algoritmo irá ajustar os pesos (W) de cada entrada (X),",
    "buscando encontrar os valores ideais para alcançar os resultados esperados.\n",
    sep="\n\n"
)

entradas = {
    'objeto 1': {
        'X1' : float(input('objeto 1\nX1: ')),
        'X2' : float(input('X2: ')),
        'X3' : float(input('X3: ')),
        'Y'  : float(input('Valor de saída (Y) esperado (0 ou 1): '))
    },

    'objeto 2': {
        'X1' : float(input('objeto 2\nX1: ')),
        'X2' : float(input('X2: ')),
        'X3' : float(input('X3: ')),
        'Y'  : float(input('Valor de saída (Y) esperado (0 ou 1): '))
    },

    'objeto 3': {
        'X1' : float(input('objeto 3\nX1: ')),
        'X2' : float(input('X2: ')),
        'X3' : float(input('X3: ')),
        'Y'  : float(input('Valor de saída (Y) esperado (0 ou 1): '))
    }
}

bias = None
while bias == None:
    match input("Usará Bias? [S/N]: ").upper():
        case 'S':
            bias = 1
        case 'N':
            bias = 0
        case _:
            print('inválido\n')


taxaAprendizagem = float(input('Digite o valor da taxa de aprendizagem: '))

w = [0.2, 0.2, 0.2] #pesos dos Xs e o bias
w.append(0.2) if bias == 1 else None
fim = False
erros = [] #lista para armazenar os erros de cada iteração
numeroIteracao = 0
while not fim:
    numeroIteracao += 1
    print(f"\n\nIteração {numeroIteracao}")
    erros.clear() #limpa a lista de erros a cada iteração
    
    for i, objeto in enumerate(entradas.values()):
        net = 0

        xValues = [objeto['X1'], objeto['X2'], objeto['X3'], bias]
        xValues.pop() if bias == 0 else None
        
        for j, x in enumerate(xValues): #pega cada item de x_values (x) e o índice(i)
            net += x * w[j]
            
        y = 1 if net > 0 else 0
        erro = objeto['Y'] - y
        erros.append(erro)
        print(f"objeto {i + 1} erro: {erro}")

        for j, x in enumerate(xValues): #pega cada item de x_values (x) e o índice(i)
            w[j] += taxaAprendizagem * erro * xValues[j] #da novo valor para os pesos


    print("Erros: ", erros)
    print("Pesos novos:", w)

    if all(e == 0 for e in erros):
        fim = True
        print(f"\n\nTreinamento concluído!\nForam realizadas {numeroIteracao} iterações")

print("\n\nPesos finais:", w)
input("Pressione Enter para sair...")

            

        









