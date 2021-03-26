/*
 * Triangle.cpp
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#include <cmath>
#include <iostream>
#include "Triangle.h"


Triangle::Triangle(const Point &x, const Point &y,const Point &z)
{
    p1 = x;
    p2 = y;
    p3 = z;
    edgeA = getDist(p1, p2);
    edgeB = getDist(p2, p3);
    edgeC = getDist(p1, p3);
}

double Triangle::getArea()const
{
    double area,temp;
    temp= (edgeA + edgeB + edgeC) * (edgeA + edgeB - edgeC) * (edgeA + edgeC - edgeB) * (edgeB + edgeC - edgeA);
    area = sqrt(temp);
    area = area * 0.25;
    return area ;
}
