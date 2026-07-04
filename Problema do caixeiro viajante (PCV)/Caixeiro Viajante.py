import random
import numpy as np


def criar_populacao(ncidades, tam_populacao):
    populacao = []
    cidades_base = []
    for i in range(ncidades):
        cidades_base.append(i)

    for i in range(tam_populacao):
        novarota = cidades_base.copy()
        random.shuffle(novarota)    #cria uma rota aleatoria e insere na populacao
        populacao.append(novarota)

    return populacao


def calcularfitness(matriz_distancias, rota):
    n = len(rota)
    soma = 0
    for i in range(n-1):
        soma += matriz_distancias[rota[i]][rota[i+1]]

    soma += matriz_distancias[rota[n-1]][rota[0]]
    nota = 1/soma    #uma nota, quanto menor a distancia maior a nota
    return nota

def selecao_roleta(populacao, matriz_distancias):
    fitness_populacao = []

    for rota in populacao:
        nota = calcularfitness(matriz_distancias, rota)
        fitness_populacao.append(nota)

    escolhido = random.choices(populacao, weights=fitness_populacao, k=1)    #fitness_populacao é o peso que cada elemtno tem na roleta, as suas notas
    
    return escolhido[0] #como a funcao retorna uma lista, mesmo que k=1,  precisamos acessar o indice 0

def cruzamento(pai1, pai2):
    n = len(pai1)
    # Cria um filho "vazio" preenchido com -1
    filho = [-1] * n  

    pt1, pt2 = sorted(random.sample(range(n), 2))   #sorteia o range do pedaco que o filho vai ter do pai1 nas mesmas posicoes
    aux1 = pt1     
    aux2 = pt2
    while(aux1 <= aux2):
        filho[aux1] = pai1[aux1]
        aux1 += 1
    
    pos_filho = (pt2 + 1) % n
    pos_pai2 = (pt2 + 1) % n

    while -1 in filho:              #preenche as posicoes restantes com as do pai2
        cidade_pai2 = pai2[pos_pai2]

        if cidade_pai2 not in filho:
            filho[pos_filho] = cidade_pai2
            pos_filho = (pos_filho + 1) % n

        pos_pai2 = (pos_pai2 + 1) % n

    return filho

def mutacao(rota, tava_mutacao):
    numero_sorteado = random.random() #vai sortear um numero entre 0.0 e 1.0

    if(numero_sorteado < tava_mutacao):
        n = len(rota)

        indice1 = random.randint(0, n-1)
        indice2 = random.randint(0, n-1) #sorteia duas cidades aleatorias
        while indice1 == indice2:
            indice2 = random.randint(0, n-1)
        aux = rota[indice1]
        rota[indice1] = rota[indice2]   #troca a posicao das cidades
        rota[indice2] = aux

    return rota


def main():
    matriz_distancias = np.loadtxt('grafo.txt')
    ncidades = matriz_distancias.shape[0]
    TAM_POPULACAO = 50
    TAXA_CRUZAMENTO = 0.8
    TAXA_MUTACAO = 0.05
    GERACOES = 100

    populacao = criar_populacao(ncidades, TAM_POPULACAO)

    for g in range(GERACOES):
        fitness_populacao = []

        for rota in populacao:
            nota = calcularfitness(matriz_distancias, rota)
            fitness_populacao.append(nota)

        indice_do_melhor = np.argmax(fitness_populacao) #np.argmax da biblioteca numpy vai escolher a maior nota, e retorna o indice dela
        melhor_rota_da_geracao = populacao[indice_do_melhor]
        menor_distancia_da_geracao = 1/fitness_populacao[indice_do_melhor]  #transforma o fitness de volta pra distancia pra conseguirmos ler

        #imprime o progresso na tela
        if (g + 1) % 10 == 0 or g == 0: #a cada 10 geracoes
            print(f"Geração {g+1} | Menor Distância: {menor_distancia_da_geracao:.2f} km")

        nova_populacao = []
    
        #aplicando o elitismo
        nova_populacao.append(melhor_rota_da_geracao.copy())

        while len(nova_populacao) < TAM_POPULACAO:          #preenche a nova populacao com filhos
            pai1 = selecao_roleta(populacao, matriz_distancias)
            pai2 = selecao_roleta(populacao, matriz_distancias)
            if random.random() < TAXA_CRUZAMENTO:
                filho = cruzamento(pai1, pai2)
            else:
                filho = pai1.copy()

            filho = mutacao(filho, TAXA_MUTACAO)
            
            nova_populacao.append(filho)

        # a populacao antiga e substituida pela nova populacao de filhos
        populacao = nova_populacao

    print("\n    EVOLUÇÃO CONCLUÍDA    ")
    print(f"Melhor rota encontrada: {melhor_rota_da_geracao}")
    print(f"Distância final: {menor_distancia_da_geracao:.2f} km")

main()
