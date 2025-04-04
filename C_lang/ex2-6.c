#include <stdio.h>

int main(void)
{
printf("%.1lf\n", 1e6); // Output real numbers in exponential form in decimal form
printf("%.7lf\n", 3.14e-5); // Output to the seventh decimal place or lower
printf("%.le\n", 0.0000314); // Print decimal numbers as a piece
printf("%.2le\n", 0.0000314); // Output to the second decimal place in exponential form

return 0;
}