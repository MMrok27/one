#ifndef LINESEGMENT_H
#define LINESEGMENT_H

#include "point.h"
#include <stdbool.h>

typedef struct LineSegment {
    Point a;
    Point b;
} LineSegment;

LineSegment makeLineSegment(int ax,int ay,int bx,int by);

LineSegment makeLineSegmentfromPoints(const Point *a, const Point *b);

void show2(const LineSegment *s);

double length(const LineSegment*s);

bool parallel(const LineSegment*s1,const LineSegment*s2);

bool perpendicular(const LineSegment*s1,const LineSegment*s2);

void movee(LineSegment *s,int deltaX,int deltaY);
#endif
