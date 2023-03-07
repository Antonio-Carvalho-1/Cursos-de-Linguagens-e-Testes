#include <stdio.h>

int main(){

    int x, mod;
    scanf("%d", &x);

    mod = x%2; // resto da divisão por 2

    if(mod==1) //decisão de arcodo com o resto do número.
    {
        printf("O numero %d e impar", x);
    }else
    {
        printf("O numero %d e par", x);
    }


    return 0;
}
