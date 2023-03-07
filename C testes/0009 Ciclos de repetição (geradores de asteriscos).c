#include <stdio.h>

int main()
{
    printf("Esse e um gerador de asteriscos\nDigite o numero de escadas de asteriscos que deseja printar\n");
    int a, x, y;
    scanf("%d", &a);

    for(x=1;x<=a;x++)
    {
        for(y=1;y<=x;y++)
        {
            printf("*");
        }
        printf("\n");
    }
    printf("\n");

    return 0;
}
