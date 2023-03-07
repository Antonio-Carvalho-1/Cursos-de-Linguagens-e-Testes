#include <stdio.h>
int main()
{
    int  x=0, aux, soma=0;

    while(x!=-1)
    {
        printf("Digite um numero nao negativo\n");
        printf("para encerrar o programna digite -1\n");
        scanf("%d", &x);
        soma += x;



    }

    return 0;
}
