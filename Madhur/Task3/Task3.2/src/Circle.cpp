/*
 * Circle.cpp
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#include "Circle.h"
#include "Point.h"
#include <iostream>

#define M_PI 3.1428571428

Circle::Circle(const Point &l1, int radius)
{
    r = radius;
    p = l1;
}

double Circle::getArea()const
{
    return r * r * M_PI;
}



