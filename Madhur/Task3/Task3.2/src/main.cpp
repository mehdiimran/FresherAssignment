//============================================================================
// Name        : 2.cpp
// Author      : Madhur
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

/* create a shape class and inherit different shapes from it like shape-> triangle , -> rectangle , circle , shape-> rectangle->square.
and implement a display area function for the provided co ordinates of each shape. */

#include "Point.h"
#include "Shape.h"
#include "Triangle.h"
#include "Circle.h"
#include "Polygon.h"
#include "Rectangle.h"
#include <iostream>
//#include <typeinfo>

using namespace std;

int main()
{
	int count = 0;
	while(1)
	{
		int x1, y1, x2, y2, radius;
		cout << "Enter First Point: " << endl;
		cout << "x1: ";
		cin >> x1;
		cout << "y1: ";
		cin >> y1;
		cout << "Enter Second Point: " << endl;
		cout << "x2: ";
		cin >> x2;
		cout << "y2: ";
		cin >> y2;
		cout << "radius: ";
		cin >> radius;
		cout << endl;

		Point O(0, 0);
		Point A(x1, y1);
		Point B(x2, y2);
		Shape *shapes[] = { new Rectangle(A, B), new Triangle(O, A, B), new Circle(O, radius) };

		for (int i = 0; i < 3; ++i)
		{
			shapes[i]->shapeName(i);
			cout << " Area = " << shapes[i]->getArea() <<" sq.units."<< endl;
		}
		cout << endl;
		for (int i = 0; i < 3; ++i)
			delete shapes[i];

		if(count > 1000)
			break;
	}
    return 0;
}



