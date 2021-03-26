/*
 * Polygon.h
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#ifndef POLYGON_H_
#define POLYGON_H_

#include "Shape.h"

class Polygon :public Shape
{
	public:
		double getDist(const Point &p1,const Point &p2);
};


#endif /* POLYGON_H_ */
