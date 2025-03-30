#include <stdio.h>

int main(void)
{
    printf("%d\n", 10);  //%d 위치에 정수출력 
    printf("%lf\n", 3.4);  //%lf 위지에 소수점 6자리 출력
    printf("%.1lf\n", 3.45);  //소수점 이하 첫째자리 까지 출력(둘째자리 반올림)
    printf("%.10lf\n", 3.4);  //소수점 이하 열째자리 까지 출력

    printf("%d과 %d의 합은 %d 입니다.\n", 10, 20, 10+20);
    printf("%.1lf - %.1lf = %.1lf\n ", 1.2, 3.4, 1.2+3.4);

    return 0;
}