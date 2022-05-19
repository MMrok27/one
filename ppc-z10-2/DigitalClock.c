#include "DigitalClock.h"
#include <stdio.h>
#include <stdlib.h>
unsigned checkg(unsigned g)
{
    g=g%24;
    return g;
}

unsigned checkm(unsigned m)
{
    m=m%60;
    return m;
}
unsigned checkilm(unsigned m)
{
    unsigned il=0;
    while(m>60)
    {
        m=m-60;
        il++;
    }
    return il;
}
unsigned zmniej()
{

}
unsigned zmniejil()
{

}
DigitalClock makeDigitalClock(unsigned godzina,unsigned minuta)
{
    DigitalClock temp;
    unsigned il=checkilm(minuta);
    minuta=checkm(minuta);
    godzina+=il;
    godzina=checkg(godzina);
    temp.godzina = godzina;
    temp.minuta = minuta;
    return temp;
}

void showTime(DigitalClock*d)
{
    printf("%d:%d", d->godzina, d->minuta);
}

void increment(DigitalClock*d,unsigned ileMinut)
{
    d->minuta += ileMinut;
    unsigned il=checkilm(d->minuta);
    d->minuta =checkm(d->minuta);
    d->godzina +=il;
    d->godzina = checkg(d->godzina);

}

void increment1(DigitalClock*d)
{
    d->minuta += 1;
    unsigned il=checkilm(d->minuta);
    d->minuta =checkm(d->minuta);
    d->godzina +=il;
    d->godzina = checkg(d->godzina);
}

void decrement(DigitalClock*d,unsigned ileMinut)
{
    d->minuta -= ileMinut;

    unsigned il=checkilm(d->minuta);
    d->minuta =checkm(d->minuta);
    d->godzina +=il;
    d->godzina = checkg(d->godzina);
}

void decrement1(DigitalClock*d)
{

}
