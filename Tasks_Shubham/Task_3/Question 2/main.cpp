#include<iostream>
#include<conio.h>
#include<process.h>
using namespace std;

class shape
{
    protected:
        double b;
        double h;
    public:
        shape(double b1,double h1)
        {
            b=b1;
            h=h1;
        }
        virtual void disp_area()=0;
};

class triangle :public shape
{
    public:
        triangle(double b1, double h1):shape(b1,h1)
        {
        }
        void disp_area();
};

class rectangle:public shape
{
    public:
        rectangle(double b1,double h1):shape(b1,h1)
        {
        }
        void disp_area();
};

class square:public rectangle
{
    public:
        square(double s):rectangle(s,s)
        {
        }
        void disp_area();
};



void triangle::disp_area()
{
    double a1;
    a1=(b*h)*1/2;
    cout<<"\nTHE AREA OF TRIANGLE IS :"<<a1;
    getch();
}

void rectangle::disp_area()
{
    double a1;
    a1=b*h;
    cout<<"\nTHE AREA OF RECTANGLE IS :"<<a1;
    getch();
}



void square::disp_area()
{
    double a1;
    a1=b*b;
    cout<<"\nTHE AREA OF SQUARE IS :"<<a1;
    getch();
}
main()
{
    double b1,h1;
    //clrscr();
    cout<<"\n\nPLEASE ENTER THE TRIANGLE DETAILS\n";
    cout<<"BASE         = ";
    cin>>b1;
    cout<<"\nHYPOTENUSE   = ";
    cin>>h1;
    triangle t1(b1,h1);
    cout<<"\n\nPLEASE ENTER THE RECTANGLE DETAILS\n";
    cout<<"\nLENGTH  = ";
    cin>>b1;
    cout<<"\nBREADTH = ";
    cin>>h1;
    rectangle r1(b1,h1); 
    cout<<"\n\nPLEASE ENTER THE SQUARE DETAILS\n";
    cout<<"\nSIDE  = ";
    cin>>b1;
    square s1(b1);
    shape *list[3];
    list[0]=&t1;
    list[1]=&r1;
    list[2]=&s1;
    while(1)
    {
      //  clrscr();
        cout<<"\n\n\n\n\n------------MENU------------";
        cout<<"\n\n1. TRIANGLE AREA";
        cout<<"\n2. RECTANGLE AREA";
        cout<<"\n4. SQUARE AREA";
        cout<<"\n4. EXIT";
        cout<<"\nENTER YOUR CHOICE :";
        int ans;
        cin>>ans;
        if(ans ==1)
        {
            list[0]->disp_area();
        }
        else if(ans==2)
        {
            list[1]->disp_area();
        }
         else if(ans==3)
        {
            list[2]->disp_area();
        }
        else if(ans==4)
            exit(1);
        else
        {
            cout<<"\nINVALID CHOICE";
            getch();
            continue;

      }
  }
}