#include <stdio.h>
char a,b,c,d,e,f,g,h,i;
char start_letter = 'A';
char end_letter = 'Z';

int NameOfGod(int number);

int main(){
    NameOfGod(9);
}

int NameOfGod(int number){
    if(number==0){
        void last_iteration(char a,char b,char end_letter) {
            if (!(b <= end_letter)) return;
            printf("%c%c%c%c%c%c%c%c%c\t",a,b,c,d,e,f,g,h,i);
            last_iteration(a,b+1,end_letter);
        }
    }else{
        void rec_a(char a, char end_letter) {
            if (!(a <= end_letter)) return;
            rec_number+1(a,start_letter,end_letter);
            rec_number(a+1,end_letter);
        }
        NameOfGod(--number);
    }
}

