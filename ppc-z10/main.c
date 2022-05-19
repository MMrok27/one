#include <stdio.h>

#include "LineSegment.h"
#include "point.h"
#include "Triangle.h"

int main()
{
    LineSegment hm = makeLineSegment(1,1,2,1);
    Point p1 = makePoint(2,2);
    Point p2 = makePoint(5,2);
    Point p3 = makePoint(2,4);
    LineSegment hm2 =  makeLineSegmentfromPoints(&p1,&p2);
    show2(&hm2);
    printf("\n%lf", length(&hm2));
    printf("\n");
    show2(&hm);
    movee(&hm,2,0);
    printf("\n");
    show2(&hm);

    Triangle tr1=makeTriangle(1,1,2,1,1,3);
    Triangle tr2=makeTrianglefromPoints(&p1,&p2,&p3);
    printf("\n");
    showt(&tr1);
    printf("\n");
    showt(&tr2);
    printf("\n");
    return 0;
}
