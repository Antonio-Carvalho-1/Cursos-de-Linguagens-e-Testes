#include <stdio.h>
int main(){
    char nome[60];

    printf("Qual e o seu nome? \n");
    scanf("%s", &nome);
    printf("Muito prazer em te conehcer %s!", nome);

    return 0;
}
