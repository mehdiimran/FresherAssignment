#include<iostream>
using namespace std;
class Shape
{
protected:
	float area;
public:
	Shape( void )
	{
		this->area = 0;
	}

	virtual void acceptRecord( void ) = 0;

	virtual float calculateArea( void ) = 0;

	void printRecord( void )const
	{
		cout<<"Area	:	"<<this->area<<endl;
	}
};
class Rectangle : public Shape
{
private:
	float breadth;
protected:
    float length;
public:
	Rectangle( void )
	{
		this->length = 0;
		this->breadth = 0;
	}
	void acceptRecord( void )
	{
		cout<<"Length	:	";
		cin>>this->length;
		cout<<"Breadth	:	";
		cin>>this->breadth;
	}
	float calculateArea( void )
	{
		this->area = this->length * this->breadth;
		return this->area;
	}
};


class Circle : public Shape
{
private:
	float radius;
public:
	Circle( void )
	{
		this->radius = 0;
	}
	void acceptRecord( void )
	{
		cout<<"Radius	:	";
		cin>>this->radius;
	}
	float calculateArea( void )
	{
		this->area = 3.142 * radius * radius;
		return this->area;
	}
};
class Triangle:public Shape{
private:
	float base;
	float height;
public:
	Triangle( void )
	{
		this->base = 0;
		this->height = 0;
	}
	void acceptRecord( void )
	{
		cout<<"Enter Base	:	";
		cin>>this->base;
		cout<<"Enter height	:	";
		cin>>this->height;
	}
	float calculateArea( void )
	{
		this->area = (this->base * this->height)/2;
		return this->area;
	}	
};
class Square : public Rectangle{
public:
    Square(){
        this->length=0;
    }  
    void acceptRecord( void )
	{
		cout<<"Length	:	";
		cin>>this->length;
	}
	float calculateArea( void )
	{
		this->area = this->length * this->length;
		return this->area;
	}
};

class ShapeFactory
{
public:
	static Shape* getInstance( int choice )
	{
        Shape *basePtr = NULL;
		switch( choice )
		{
		case 1:
			basePtr = new Rectangle( );	
			break;
		case 2:
			basePtr = new Circle( );	
			break;
		case 3:
			basePtr = new Triangle( );	
			break;	
		case 4:
		    basePtr = new Square();
		}
		return basePtr;
	}
	static int menuList( void )
	{
		int choice;
		cout<<"0.Exit"<<endl;
		cout<<"1.Rectangle"<<endl;
		cout<<"2.Circle"<<endl;
		cout<<"3.Triangle"<<endl;
	    cout<<"4.Square"<<endl;
		cout<<"Enter choice	:	";
		cin>>choice;
		return choice;
	}
};
int main( void )
{
	int choice;
	while( ( choice = ShapeFactory::menuList() ) != 0 )
	{
		Shape *basePtr =  ShapeFactory::getInstance(choice);
		if( basePtr != NULL )
		{
			basePtr->acceptRecord( );	
			basePtr->calculateArea( );	
			basePtr->printRecord( );
			delete basePtr;
		}
	}
	return 0;
}

