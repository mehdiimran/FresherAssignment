/*
 * Point.cpp
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */
#include <iostream>
#include "Point.h"

Point::Point()
{
    setX(0);
    setY(0);
}

Point::Point(int x,int y )
{
 setX(x);
 setY(y);
}

void Point::setX(int x)
{
    if(x < 0)
    {
        std::cout << "Invalid value for x, Setting to default\n";
        this->x = 0;
    }
    else
        this->x = x;
}

void Point::setY(int y)
{
    if(y < 0)
    {
        std::cout << "Invalid value for y, Setting to default\n";
        this->y = 0;
    }
    else
        this->y = y;
}

int Point::getX() const
{
    return x;
}

int Point::getY() const
{
    return y;
}

void Point::print() const
{
        std::cout << "X:" << this->x << "  " << "Y:" << this->y ;
}
