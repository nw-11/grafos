# Algoritmo Genético para o Problema do Caixeiro Viajante (PCV)

Este projeto implementa um Algoritmo Genético para resolver o Problema do Caixeiro Viajante. O objetivo é encontrar a menor distância possível para percorrer todas as cidades e retornar à cidade de origem, utilizando conceitos de seleção natural, cruzamento e mutação.

O arquivo `grafo.txt` é onde guardamos a matriz de adjacência que representa as cidades, onde o `grafo[n][m]` armazena a distância da cidade "n" até a cidade "m".

### Matriz utilizada para testes (15 cidades):
```text
0 29 20 21 16 31 100 12 4 31 18 40 42 7 47
29 0 15 29 28 46 9 39 12 30 18 31 14 30 46
20 15 0 15 48 35 15 23 20 20 22 17 38 41 21
21 29 15 0 28 32 32 18 44 23 37 20 19 28 17
16 28 48 28 0 46 39 45 42 22 28 39 37 36 29
31 46 35 32 46 0 16 11 41 49 19 32 37 11 42
100 9 15 32 39 16 0 38 41 33 37 38 43 45 44
12 39 23 18 45 11 38 0 28 39 29 33 24 14 12
4 12 20 44 42 41 41 28 0 10 32 13 25 31 43
31 30 20 23 22 49 33 39 10 0 24 43 42 18 20
18 18 22 37 28 19 37 29 32 24 0 17 19 44 14
40 31 17 20 39 32 38 33 13 43 17 0 28 35 34
42 14 38 19 37 37 43 24 25 42 19 28 0 23 41
7 30 41 28 36 11 45 14 31 18 44 35 23 0 18
47 46 21 17 29 42 44 12 43 20 14 34 41 18 0
```

**voce pode editar o arquivo caso queira testar outro grafo**


## Pré-requisitos e Instalação

O projeto foi desenvolvido em Python e utiliza a biblioteca **NumPy** para manipulação de matrizes e leitura dos dados do grafo.

Comando para instalar a biblioteca:

```bash
pip install numpy 
 #OU
python -m pip install numpy
```


