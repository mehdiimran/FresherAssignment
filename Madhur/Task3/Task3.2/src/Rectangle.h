/*
 * Rectanglr.h
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#ifndef RECTANGLE_H_
#define RECTANGLE_H_

#include "Point.h"
#include "Polygon.h"

class Rectangle:public Polygon
{
    public:
		Rectangle(const Point &l, const Point &r) ;
		double getArea()const;

    private:
        Point topLeft;
        Point bottomRight;
        int length ,width;
};



#endif /* RECTANGLE_H_ */
