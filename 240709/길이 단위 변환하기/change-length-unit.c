#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.
    double ft = 30.48;
    int mi = 160934;

    double ft2cm = ft * 9.2;
    double mi2cm = mi * 1.3;

    printf("9.2ft = %.1lfcm\n1.3mi = %.1lfcm", ft2cm, mi2cm);
    return 0;
}