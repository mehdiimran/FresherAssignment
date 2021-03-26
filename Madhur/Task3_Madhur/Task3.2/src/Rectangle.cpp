/*
 * Rectangle.cpp
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#include <iostream>
#include "Rectangle.h"

Rectangle::Rectangle(const Point &l, const Point &r)
{
    topLeft = l;
    bottomRight = r;

    Point tempP = topLeft;
    tempP.setY(topLeft.getY());
    tempP.setX(bottomRight.getX());

    length = getDist(topLeft,tempP);
    width = getDist(tempP,bottomRight);
}

double Rectangle::getArea()const
{
    return length * width;
}
