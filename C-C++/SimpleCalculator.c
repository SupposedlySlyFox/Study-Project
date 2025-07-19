#include <stdio.h>

typedef struct {
    int number1;
    char symbol;
    int number2;
} MathVariables;

void UserMath(int first, char symbol, int second) {
    switch (symbol) {
        case '+':
            printf("A soma é: %i\n", first + second);
            break;
        case '-':
            printf("A subtração é: %i\n", first - second);
            break;
        case '*':
            printf("A multiplicação é: %i\n", first * second);
            break;
        case '/':
            if (second != 0)
                printf("A divisão é: %.2f\n", (float)first / second);
            else
                printf("Erro: divisão por zero\n");
            break;
        default:
            printf("Operador inválido: %c\n", symbol);
            break;
    }
}

int main() {
    MathVariables mv;

    printf("Digite a operação (ex: 2 + 2): ");
    scanf("%i %c %i", &mv.number1, &mv.symbol, &mv.number2);

    UserMath(mv.number1, mv.symbol, mv.number2);

    return 0;
}
