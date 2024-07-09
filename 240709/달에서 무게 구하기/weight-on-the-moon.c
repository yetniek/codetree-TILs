#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    int weight = 13;
    double gravity = 0.165;
    double res = weight * gravity;

    printf("%d * %lf = %.6lf", weight, gravity, res);
    return 0;
}