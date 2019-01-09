#include <stdio.h>
int NameOfGod(int number);
// char a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
// char array[26]={a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
// char name = "finished";
int array_test[26]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26};

int main(){
    NameOfGod(9);
}

int NameOfGod(int number){
    if(number==0){
        return(0);
    }else{
        printf("%d\n",array_test[number-1]);
        NameOfGod(--number);
    }
}
