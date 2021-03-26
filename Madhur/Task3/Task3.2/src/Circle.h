/*
 * Circle.h
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#ifndef CIRCLE_H_
#define CIRCLE_H_

#include "Point.h"
#include "Shape.h"

class Circle : public Shape
{
	public:
		Circle(const Point &l1,int radius);
		double getArea()const;

	private:
		int r;
		Point p;
};




#endif /* CIRCLE_H_ */
