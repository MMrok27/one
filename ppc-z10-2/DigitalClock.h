#ifndef POINT_H
#define POINT_H

typedef struct DigitalClock {
    unsigned godzina;
    unsigned minuta;
} DigitalClock;

DigitalClock makeDigitalClock(unsigned godzina,unsigned minuta);

void showTime(DigitalClock*d);

void increment(DigitalClock*d,unsigned ileMinut);

void increment1(DigitalClock*d);

void decrement(DigitalClock*d,unsigned ileMinut);

void decrement1(DigitalClock*d);


#endif
