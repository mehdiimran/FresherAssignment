/*
 * Shape.h
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#ifndef SHAPE_H_
#define SHAPE_H_

#include "Point.h"
#include <iostream>


class Shape
{
  	public:
		virtual double getArea()const = 0;
		void shapeName(int i);
		virtual ~Shape(){};
};



#endif /* SHAPE_H_ */
