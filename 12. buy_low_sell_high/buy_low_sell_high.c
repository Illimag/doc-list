/* 
	Buy Low Sell High
	
	Jaemin Kim
*/

#include "external_data_variables.h"
#include "buy_mechanism/buying_mechanism.c"
#include "custom_lib/custom_0.h"
#include <stdio.h>


int main(){
	printf("Current prices\n");
	printf("XLM:%f\n",XLM);
	printf("BAT:%f\n",BAT);
	printf("ZRX:%f\n",ZRX);
	printf("LINK:%f\n",LINK);
	printf("MOBI:%f\n",MOBI);
	printf("XRP:%f\n",XRP);	
	
	int yes = 1;
	int no = 0;

	int trigger = 0; // default trigger set to 0


		for(int y=0;y<=5;y++){ // 1 1 0 1 1 1
			trigger = currency_pair_charge[y];

            if(trigger==0){
                printf("not buy, next pair\n");
            }else if(trigger==1){
            	// This will trigger the main_buy function from
            	// "buy_mechanism/buying_mechanism.c"
                main_buy();
            }else{
                printf("error, next pair\n");
            }

			}
			return(0);

}

