/*
 * Triangle.h
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#ifndef TRIANGLE_H_
#define TRIANGLE_H_

#include "Point.h"
#include "Polygon.h"

class Triangle : public Polygon
{
	public:
		Triangle(const Point &p1, const Point &p2, const Point &p3);
		double getArea()const;
		Point p1;
		Point p2;
		Point p3;
		double edgeA, edgeB, edgeC;
};



#endif /* TRIANGLE_H_ */
