#include <stdio.h>
#include "A_Z/A_Z.c"

int NameOfGod(int number);

int main(){
    NameOfGod(9);
}

int NameOfGod(int number){
    if(number==0){
        return(1);
    }else{
            printf("%d",array_test[number-1]);
            NameOfGod(--number);
    }
}







