#include <stdio.h>

char a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
char array[26]={a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z};
char name;

int NameOfGod(int number);

int main(){
    NameOfGod(9);
}

int NameOfGod(int number){
    iteration();
}

int iteration(){
    for(number=number;number>0;number--){
        if(number>0){
            for(array[number]='A';array[number]<='Z';++array[number]){
                name = array[number] + name;
                NameOfGod(number--);
            }
        }else{
            printf("%c\n",name);
        }
    }
}
