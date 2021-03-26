#include<iostream>
using namespace std;

// Base class
class Shape {
	private:
		float area;
	public:
		Shape() {
			this->area = 0;
		}
		void setArea(int area){
			this->area = area;
		}
		float getArea() {
			return this->area;
		}
		virtual void acceptRecord() = 0;
		
		virtual float calculateArea() = 0;
		
		void printRecord() {
			cout<<"Area: "<<this->getArea()<<endl;
		}
};

// Derived class - circle
class Circle: public Shape {
	private:
		float radius;
	public:
		Circle() {
			this->radius = 0;
		}
		void setRadius(int radius){
			this->radius = radius;
		}
		float getRadius(){
			return this->radius;
		}
		void acceptRecord() {
			cout<<"Radius: ";
			cin>>this->radius;
		}
		float calculateArea() {
			this->setArea(3.142 * radius * radius);
			return this->getArea();
		}
};

// Derived class - Rectangle
class Rectangle: public Shape {
	private:
		float length;
		float breadth;
		
	public:
		Rectangle() {
			this->length = 0;
			this->breadth = 0;
		}
		void setBreadth(int breadth) {
			this->breadth = breadth;
		}
		void setLength(int length) {
			this->length= length;
		}
		float getBreadth() {
			return this->breadth;
		}
		float getLength() {
			return this->length;
		}
		void acceptRecord() {
			cout<<"Length: ";
			cin>>this->length;
			cout<<"Breadth: ";
			cin>>this->breadth;
		}
		float calculateArea() {
			this->setArea(this->length * this->breadth);
			return this->getArea();
		}
};

// Derived class - Triangle
class Triangle: public Shape {
	private:
		float base;
		float height;
	public:
		Triangle() {
			this->base = 0;
			this->height = 0;
		}
		void setBase(int base) {
			this->base = base;
		}
		void setHeight(int height){
			this->height= height;
		}
		float getBase() {
			return this->base;
		}
		float getHeight() {
			return this->height;
		}
		void acceptRecord() {
			cout<<"Enter Base: ";
			cin>>this->base;
			cout<<"Enter height: ";
			cin>>this->height;
		}
		float calculateArea() {
			this->setArea( (this->base * this->height)/2);
			return this->getArea();
		}
};

// Derived class - Square
class Square: public Rectangle {
	public:
		Square(){
			this->setLength(0);
		}  
		void acceptRecord() {
			int value;
			cout<<"Length: ";
			cin>>value;
			this->setLength(value);
	   }
		float calculateArea() {
			this->setArea(this->getLength() * this->getLength());
			return this->getArea();
	   }
};

int menu() {
	int choice;
	cout<<"0. Exit"<<endl;
	cout<<"1. Circle"<<endl;
	cout<<"2. Rectangle"<<endl;
	cout<<"3. Triangle"<<endl;
	cout<<"4. Square"<<endl;
	cout<<"Enter choice: ";
	cin>>choice;
	return choice;
}

int main() {
	int choice;
	while((choice = menu()) != 0) {
		Shape *ptr = NULL;
		switch( choice )
		{
		case 1:
		    ptr = new Circle();
			break;
		case 2:
			ptr = new Rectangle();
			break;
		case 3:
			ptr = new Triangle();
			break;	
		case 4:
		    ptr = new Square();
			break;
		default:
			cout<<"Wrong choice entered. Please enter again."<<endl;
			continue;
		}
		if(ptr != NULL)
		{
			ptr->acceptRecord();
			ptr->calculateArea();
			ptr->printRecord();
			delete ptr;
		}
	}
	return 0;
}
