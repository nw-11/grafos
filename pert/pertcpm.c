#include <stdio.h>
#define MAX 40

typedef struct{
    int inicio;
    int fim;
    int tempo;
}atividades;

int main(){
    
FILE *arq = fopen("grafo.txt", "r");
atividades atv[MAX];
int numero_nos = 0;
int numero_atividades = 0;

while(fscanf(arq, "%d %d %d", 
        &atv[numero_atividades].inicio, 
        &atv[numero_atividades].fim, 
        &atv[numero_atividades].tempo) == 3){
    if(atv[numero_atividades].fim > numero_nos){
        numero_nos = atv[numero_atividades].fim;
    }
    numero_atividades++;
}
numero_nos++;
fclose(arq);
int tempomaiscedo[MAX];
int tempomaistarde[MAX];

//forward pass

for(int i = 0; i < numero_nos; i++){
    tempomaiscedo[i] = 0;
}
for(int i = 0; i < numero_atividades; i++){
    int j = atv[i].inicio;
    int k = atv[i].fim;
    if(tempomaiscedo[j] + atv[i].tempo > tempomaiscedo[k]){
        tempomaiscedo[k] = tempomaiscedo[j] + atv[i].tempo;
    }
}

int duracaototal = tempomaiscedo[numero_nos-1];

//fim do forward pass


//backward pass

for(int i = 0; i < numero_nos; i++){
    tempomaistarde[i] = duracaototal;
}

for(int i = numero_atividades -1; i >= 0; i--){
    int j = atv[i].inicio;
    int k = atv[i].fim;
    if(tempomaistarde[k] - atv[i].tempo < tempomaistarde[j]){
        tempomaistarde[j] = tempomaistarde[k] - atv[i].tempo;
    }
}
    printf("Atividades: \n");
    for(int i = 0; i < numero_atividades; i++){
        int j = atv[i].inicio;
        int k = atv[i].fim;

        int cedo_inicio = tempomaiscedo[j];
        int cedo_fim = tempomaiscedo[k];
        int tarde_inicio = tempomaistarde[j];
        int tarde_fim = tempomaistarde[k];
        int folga = tarde_fim - cedo_fim;

        printf("Atividade %d -> %d | ", j, k);
        printf("Folga: %d ", folga);
        if(folga == 0){
            printf(" -> Linha Critica!!");
        }
        printf("\n");
    }
}
