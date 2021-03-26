/*
 * Polygon.cpp
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#include "Polygon.h"
#include "Shape.h"
#include "Point.h"
#include <cmath>



double Polygon::getDist(const Point &p1,const Point &p2)
{

    double distX = ((p1.getX() - p2.getX()) * (p1.getX() - p2.getX()));
    double distY = ((p1.getY() - p2.getY()) * (p1.getY() - p2.getY()));
    double distXY = sqrt(distX + distY);
    return distXY;
}

