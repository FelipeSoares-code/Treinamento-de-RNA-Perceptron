import os

def clear_screen():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main():
    quantObjetos = 3 #número de objetos que o usuário irá inserir
    quantEtradas = 3 #número de entradas que cada objeto terá (X1, X2, X3...)

    print(
        "Bem-vindo ao treinamento do Perceptron!",
        
        f"Você deverá fornecer {quantEtradas} valores numéricos de entrada (X) para {quantObjetos} objetos,",
        "além do valor esperado de saída (Y) para cada um deles e a taxa de aprendizado do sistema.",
        
        "Com base nesses dados, o algoritmo irá ajustar os pesos (W) de cada entrada (X),",
        "buscando encontrar os valores ideais para alcançar os resultados esperados.\n",
        sep="\n\n"
    )

    objetos = {}

    for i in range(quantObjetos):
        print(f"\nObjeto {i + 1}")
        if i + 1 not in objetos:
            objetos[i + 1] = {}

        for j in range(quantEtradas): #pega o valor de Xi
            x = input(f"Digite o valor de X{j + 1}: ") 
            while not x.replace('.', '', 1).replace('-', '', 1).isdigit(): #sem o .replace, o isdigit() não aceita números com . ou -
                print(f"Valor inválido. Digite um número válido para X{j + 1}.\n")
                x = input(f"Digite o valor de X{j + 1}: ")

            x = float(x)
            objetos[i + 1].update({f'X{j + 1}': x})
            
        y = input("Digite o valor esperado de saída (Y): ")
        while y not in ['0', '1']:
            print("Valor inválido. Digite 0 ou 1 para Y.\n")
            y = input("Digite o valor esperado de saída (Y): ")
        y = int(y)
        objetos[i + 1].update({'Y': y})     

    bias = None
    while bias == None:
        match input("Usará Bias? [S/N]: ").upper():
            case 'S':
                bias = 1
            case 'N':
                bias = 0
            case _:
                print('inválido\n')


    taxaAprendizagem = input('Digite o valor da taxa de aprendizagem: ')
    while not taxaAprendizagem.replace('.', '', 1).isdigit() or float(taxaAprendizagem) <= 0:
        print("Valor inválido!! Digite um número positivo válido para a taxa de aprendizagem.\n")
        taxaAprendizagem = input('Digite o valor da taxa de aprendizagem: ')

    taxaAprendizagem = float(taxaAprendizagem)

    clear_screen()
    print("Dados de entrada:")
    for i, objeto in enumerate(objetos.values()):
        print(f"\nObjeto {i + 1}: ")
        for j in range(quantEtradas):
            print(f"X{j + 1}: {objeto[f'X{j + 1}']}")
        print(f"Y: {objeto['Y']}")

    print(f"\nbias: {bias}")
    print(f"Taxa de aprendizagem: {taxaAprendizagem}\n")
    resp = input("Pressione Enter para iniciar o treinamento ou digite R para reiniciar: ").upper()
    if resp == 'R':
        clear_screen()
        return 1

    w = [0.2] * quantEtradas #pesos dos Xs e o bias
    w.append(0.2) if bias == 1 else None
    fim = False
    erros = [] #lista para armazenar os erros de cada iteração
    numeroIteracao = 0
    while not fim:
        numeroIteracao += 1
        print(f"\n\nIteração {numeroIteracao}")
        print("Pesos iniciais:", w)
        erros.clear() #limpa a lista de erros a cada iteração
        
        for i, objeto in enumerate(objetos.values()):
            net = 0

            xValues = [objeto[f'X{j + 1}'] for j in range(quantEtradas)]
            if bias == 1:
                xValues.append(bias)
            
            for j, x in enumerate(xValues): #pega cada item de x_values (x) e o índice(j)
                net += x * w[j]
                
            y = 1 if net > 0 else 0
            erro = objeto['Y'] - y
            erros.append(erro)
            print(f"objeto {i + 1} erro: {erro}")

            for j, x in enumerate(xValues): #pega cada item de x_values (x) e o índice(j)
                w[j] += taxaAprendizagem * erro * xValues[j] #da novo valor para os pesos


        print("Erros: ", erros)
        print("Pesos novos:", w)

        if all(e == 0 for e in erros):
            fim = True
            print(f"\n\nTreinamento concluído!\nForam realizadas {numeroIteracao} iterações")

    print("\n\nPesos finais: ")
    for i, peso in enumerate(w):
        if i < quantEtradas:
            print(f"W{i + 1}: {peso}")
        else:
            print(f"WBias: {peso}")

    resp = input("\nPressione Enter para sair do programa ou R para reiniciar: ").upper()
    if resp == 'R':
        clear_screen()
        return 1
    else: 
        return 0

while True:
    if main() == 1:
        continue
    else:
        break
    



            

        









