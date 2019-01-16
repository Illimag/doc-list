/*
Jae Min Kim
9/21/2018
This is an implementation of the Gregory-Leibniz series formula to find the closest value of pi.
The formula is pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
*/

#include <stdio.h>

long double pi;
long double current;
long double x;
int a;

int main()
{
	for(x=1;x=x;x+=2)
	{//pi = (4/x) ...
		if(a){// true
			current = (4/x);
			pi = pi - current;
		a = a - 1;
		//printf("true"); 
		}else{ // false
			current = (4/x);
			pi = pi + current;
		a = a + 1;
		//printf("false");
		}
		printf("%.100Lf\n",pi);
	}
}
