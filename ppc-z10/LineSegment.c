#include <stdio.h>
#include <math.h>
#include <string.h>
#include "LineSegment.h"

LineSegment makeLineSegment(int ax,int ay,int bx,int by)
{
    LineSegment temp;
    temp.a.x = ax;
    temp.a.y = ay;
    temp.b.x = bx;
    temp.b.y = by;
    return temp;
}
LineSegment makeLineSegmentfromPoints(const Point *a, const Point *b)
{
    LineSegment temp;
    temp.a.x = a->x;
    temp.a.y = a->y;
    temp.b.x = b->x;
    temp.b.y = b->y;

    return temp;
}

void show2(const LineSegment *s)
{
    printf("<%d, %d> <%d, %d>",s->a.x,  s->a.y, s->b.x,  s->b.y);
}


double length(const LineSegment*s)
{
    return sqrt(square(s->b.x - s->a.x) + square(s->b.y - s->a.y));
}

void movee(LineSegment *s,int deltaX,int deltaY)
{
    s->a.x += deltaX;
    s->b.x += deltaX;
    s->a.y += deltaY;
    s->b.y += deltaY;
}



