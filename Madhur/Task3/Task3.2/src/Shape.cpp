/*
 * Shape.cpp
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#include "Shape.h"
#include <iostream>
using namespace std;

void Shape::shapeName(int i)
{
	if(i == 0)
	{
		cout << "Rectangle";
	}
	else if(i == 1)
	{
		cout << "Triangle";
	}
	else
		cout << "Circle";
}
