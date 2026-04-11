from igraph import *

arestas = []
pesos = []

with open("grafo.txt", "r") as f:
    for linha in f:
        origem, destino, peso = map(int, linha.split())   #lendo as ligacoes do grafo
        origem -= 1
        destino -= 1     #diminuindo em 1 porque o igraph usa indice comecando em 0
        arestas.append((origem, destino))   #guardando as arestas como tuplas de vertices
        pesos.append(peso)     #guardando o peso (a tupla arestas[i] tem peso = peso[i])


num_vertices = 0                #pegando o numero de vertices
for u, v in arestas:
    num_vertices = max(num_vertices, max(u, v));      #acha o numero de vertices achando o vertice de maior numero, exemplo(se o maior vertice é o vertice 4, significa que o grafo tem 4 vertices)

num_vertices += 1      #aumenta porque estamos tratando ele indo de 0 ate n-1 ; se nao, um grafo de 5 vertices por exemplo, ele marcaria como 4 vertices, 0->4

g = Graph(directed = True)  

g.add_vertices(num_vertices)
g.add_edges(arestas)                                                                 #Cria o grafo com tudo que foi lido
g.es['weight'] = pesos
menordistancia = [float("inf")]*num_vertices                                                            
vertice = int(input("digite o vertice que voce quer saber as distancias para todos os outros: \n")) #vertice que querem descobrir a distancia dos outros
pivoinicial = vertice
if(vertice > num_vertices+1 or vertice <= 0):
    print("esse vertice nao existe no grafo\n")
vertice -= 1                       #pra se adaptar a nossa implementacao
menordistancia[vertice] = 0     #distancia dele ate ele mesmo = 0 (menordistancia[i] = menor distancia do pivoinicial->vertice i)
visitados = set()       #guarda os visitados num hash set
for i in range(num_vertices):    #percorre num_vertices vezes
    vizinhos = []
    vizinhos = g.neighbors(vertice, mode = "out") #cria a lista de vizinhos do pivo atual
    for j in vizinhos:
        if(j in visitados):
            continue       #se ja foi visitado vai pro proximo vizinho
        aresta = g.get_eid(vertice, j)
        peso = g.es[aresta]["weight"]        #pega o peso da aresta que liga o pivo com o vizinho atual
        if((menordistancia[vertice] + peso) < menordistancia[j]):         #verifica se a distancia é menor que a atual
            menordistancia[j] = (menordistancia[vertice] + peso)          
    menor = float("inf")
    proxvertice = -1
    visitados.add(vertice)            #salva como visitado no hashset o pivo atual
    for j in range(num_vertices):
        if j not in visitados and menordistancia[j] < menor:
            menor = menordistancia[j]                            #o proximo pivo, é o nao visitado com menor distancia
            proxvertice = j
    vertice = proxvertice
    if proxvertice == -1:            #nao tem proximo pivo, acaba o algoritmo
        break
for i in range(num_vertices):
    print(f"Menor distancia do vertice {pivoinicial} -> {i+1} = {menordistancia[i]}\n")










