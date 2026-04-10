from igraph import *

arestas = []
pesos = []

with open("grafo.txt", "r") as f:
    for linha in f:
        origem, destino, peso = map(int, linha.split())
        origem -= 1
        destino -= 1     #diminuindo em 1 porque o igraph usa indice comecando em 0
        arestas.append((origem, destino))
        pesos.append(peso)


num_vertices = 0                #pegando o numero de vertices
for u, v in arestas:
    num_vertices = max(num_vertices, max(u, v));
num_vertices += 1

g = Graph(directed = True)

g.add_vertices(num_vertices)
g.add_edges(arestas)
g.es['weight'] = pesos
menordistancia = [float("inf")]*num_vertices
vertice = int(input("digite o vertice que voce quer saber as distancias para todos os outros: \n"))
pivoinicial = vertice
if(vertice > num_vertices+1 or vertice <= 0):
    print("esse vertice nao existe no grafo")
vertice -= 1
menordistancia[vertice] = 0
visitados = set()
for i in range(num_vertices):
    vizinhos = []
    vizinhos = g.neighbors(vertice, mode = "out")
    for j in vizinhos:
        if(j in visitados):
            continue
        aresta = g.get_eid(vertice, j)
        peso = g.es[aresta]["weight"]
        if((menordistancia[vertice] + peso) < menordistancia[j]):
            menordistancia[j] = (menordistancia[vertice] + peso)
    menor = float("inf")
    proxvertice = -1
    visitados.add(vertice)
    for j in range(num_vertices):
        if j not in visitados and menordistancia[j] < menor:
            menor = menordistancia[j]
            proxvertice = j
    vertice = proxvertice
    if proxvertice == -1:
        break
for i in range(num_vertices):
    print(f"Menor distancia do vertice {pivoinicial} -> {i+1} = {menordistancia[i]}\n")










