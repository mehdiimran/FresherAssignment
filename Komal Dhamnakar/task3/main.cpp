/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include<iostream>
using namespace std;

#include<iostream>
#include<string>
using namespace std;

class shape
{
protected:
string name;
public:
shape(string n) { name = n; };
void setName(string n) { name = n; };
string getName() const { return name; };
virtual double getArea() const = 0;

};

class circle: public shape
{
private:
double radius;
public:
circle(string n, double r) : shape(n) { radius = r; };
void setName(string n) { name = n; };
void setRadius(double r) { radius = r; };
double getRadius() { return radius; };
double getArea() const { return 3.14*radius*radius; };
};

class Rectangle :public shape
{
private:
double a, b;
public:
Rectangle(string n, double aa, double bb) :shape(n) { a = aa; b = bb; };
void setA(double aa) { a = aa; };
void setB(double bb) { b = bb; };
double getA() const { return a; };
double getB() const { return b; };
double getArea() const { return 2*a * b; };

};
class Square :public shape
{
private:
double a, b;
public:
Square(string n, double aa, double bb) :shape(n) { a = aa; b = bb; };
void setA(double aa) { a = aa; };
void setB(double bb) { b = bb; };
double getA() const { return a; };
double getB() const { return b; };
double getArea() const { return a * b; };

};
class Triangle :public shape
{
private:
double a, h;
public:
Triangle(string n, double aa, double hh) :shape(n) { a = aa; h = hh; }
void setA(double aa) { a = aa; };
void setH(double hh) { h = hh; };
double getA() const { return a; };
double getH() const { return h; };
double getArea() const { return 0.5*a*h; };

};


int main()
{
shape *a[4] = { new circle("circle", 4), new Rectangle("Rectangle",2,8), new Triangle("Triangle",9,11) ,new Square("square",2,2) };

for (int i = 0; i < 4; i++)
{
cout << a[i]->getName() << " " << a[i]->getArea() << endl;
}

return 0;
}