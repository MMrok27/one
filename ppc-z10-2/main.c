#include <stdio.h>
#include <stdlib.h>
#include "DigitalClock.h"
int main()
{
    DigitalClock czas = makeDigitalClock(21,36);
    showTime(&czas);
    printf("\n");
    increment(&czas,140);
    showTime(&czas);
    printf("\n");
    decrement(&czas,140);
    showTime(&czas);
    printf("\n");
    increment1(&czas);
    showTime(&czas);
    printf("\n");
    decrement1(&czas);
    showTime(&czas);
    printf("\n");
    return 0;
}
