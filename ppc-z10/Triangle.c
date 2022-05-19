#include <stdio.h>
#include <math.h>
#include "Triangle.h"

Triangle makeTriangle(int ax,int ay,int bx,int by,int cx,int cy)
{
    Triangle temp;
    temp.a.x = ax;
    temp.a.y = ay;
    temp.b.x = bx;
    temp.b.y = by;
    temp.c.x = cx;
    temp.c.y = cy;
    return temp;
}
Triangle makeTrianglefromPoints(const Point*a,const Point*b,const Point*c)
{
    Triangle temp;
    temp.a.x = a->x;
    temp.a.y = a->y;
    temp.b.x = b->x;
    temp.b.y = b->y;
    temp.c.x = c->x;
    temp.c.y = c->y;
    return temp;
}
void showt(const Triangle*s)
{
    printf("<%d, %d> <%d, %d> <%d, %d>",s->a.x,  s->a.y, s->b.x,  s->b.y,s->c.x,  s->c.y);
}

void movet(Triangle*s,int deltaX,int deltaY)
{
    s->a.x += deltaX;
    s->b.x += deltaX;
    s->c.x += deltaX;
    s->a.y += deltaY;
    s->b.y += deltaY;
    s->c.y += deltaY;
}
