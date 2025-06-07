print(
    "Este é um treinamento de RNA Perceptron!",
    "Você deverá fornecer 3 grupos de valores X1, X2 e X3.\n" \
    "Além do valor(Y) esperado de cada grupo de valores e a taxa de aprendizado do sistema",
    "Com base nesses valores e o resultado de saída esperado, " \
    "o algoritmo irá determinar o peso(W) ideal para cada entrada(X)",
    sep="\n\n"
)

entradas = {
    'grupo 1': {
        'X1' : float(input('Grupo 1\nX1: ')),
        'X2' : float(input('X2: ')),
        'X3' : float(input('X3: ')),
        'Y'  : float(input('Valor de saída (Y) esperado (0 ou 1): '))
    },

    'grupo 2': {
        'X1' : float(input('Grupo 2\nX1: ')),
        'X2' : float(input('X2: ')),
        'X3' : float(input('X3: ')),
        'Y'  : float(input('Valor de saída (Y) esperado (0 ou 1): '))
    },

    'grupo 3': {
        'X1' : float(input('Grupo 3\nX1: ')),
        'X2' : float(input('X2: ')),
        'X3' : float(input('X3: ')),
        'Y'  : float(input('Valor de saída (Y) esperado (0 ou 1): '))
    }
}

bias = None
match input("Usará Bias?: ").upper():
    case 'S':
        bias = 1
    case 'N':
        bias = 0
    case _:
        print('inválido')


taxaAprendizagem = float(input('Digite o valor da taxa de aprendizagem: '))

w = [0.2, 0.2, 0.2, 0.2] #pesos dos Xs e o bias

fim = False
while not fim:
    erros = []
    for grupo in entradas.values():
        net = 0

        xValues = [grupo['X1'], grupo['X2'], grupo['X3'], bias]
        for i, x in enumerate(xValues): #pega cada item de x_values (x) e o índice(i)
            net += x * w[i]
            w[i] += taxaAprendizagem * erro * xValues[i] #da novo valor para os pesos
            
        y = 1 if net >= 0 else 0
        erro = grupo['Y'] - y
        erros.append(erro)
        
    if all(e == 0 for e in erros):
        fim = True
        print("Treinamento concluído!")

            

        









