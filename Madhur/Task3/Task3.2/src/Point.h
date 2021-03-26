/*
 * Point.h
 *
 *  Created on: Mar 25, 2021
 *      Author: madhurb
 */

#ifndef POINT_H_
#define POINT_H_

class Point
{
	public:
		Point();
		Point(int x, int y);

		int getX() const;
		int getY() const;

		void setX(int x);
		void setY(int y);

		void print() const;

	private:
		int x, y;
};



#endif /* POINT_H_ */
