#include<iostream>
using namespace std;
class shape {
protected:
    float area;
};
class triangle : public shape
{
    float b, h;
public:
    void getdetails() {
        cout << "\nEnter the breadth and height : ";
        cin >> b >> h;
        area = (b * h) / 2;
    }
    void display() {
        cout << "Area of Triangle:" << area;
    }
};
class rectangle : public shape
{
    float l, w;
public:
    void getdetails() {
        cout << "\nEnter the length and width : ";
        cin >> l >> w;
        area = w * l;
    }
    void display() {
        cout << "Area of Rectangle:" << area;
    }
};
class circle : public shape
{
    float r;
public:
    void getdetails() {
        cout << "\nEnter the radius : ";
        cin >> r;
        area = 3.14 * r * r;
    }
    void display() {
        cout << "Area of Circle:" << area;
    }
};
class square : public shape
{
    float a;
public:
    void getdetails() {
        cout << "\nEnter the area : ";
        cin >> a;
        area = a * a;
    }
    void display() {
        cout << "Area of Square:" << area;
    }
};
int main() {
    triangle t;
    t.getdetails();
    t.display();
    rectangle r;
    r.getdetails();
    r.display();
    circle c;
    c.getdetails();
    c.display();
    square s;
    s.getdetails();
    s.display();
    return 0;
}