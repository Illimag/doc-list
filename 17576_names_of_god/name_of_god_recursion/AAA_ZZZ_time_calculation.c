#include <stdio.h>
char a,b,c;
char start_letter = 'A';
char end_letter = 'Z';

/*
void rec_c(int c,int b,int a) { // k-loop
    if (!(c<='Z')) return;
    printf("%c%c%c\n",a,b,c);
    rec_c(c+1,a,b); // recurse
}

void rec_b(int b,int a, int c) { // j-loop
    if (!(b<='Z')) return;
    rec_c(0,a,b); // inner loop
    rec_b(b+1,a,c); // recurse
}

void rec_a(int a,int b,int c) { // i-loop
    if (!(a<='Z')) return;
    rec_b(0,a,b); // inner loop
    rec_a(a+1,b,c); // recurse
}

int main(){
    rec_a(a,b,c);
}
 */


/*
    for (a = start_letter; a <= end_letter; a++) {
        for (b = start_letter; b <= end_letter; b++) {
            for (c = start_letter; c <= end_letter; c++) {

            }
        }
    }
*/




void rec_c(char a,char b,char c,char end_letter) { // k-loop
    if (!(c <= end_letter)) return;
    printf("%c%c%c\n",a,b,c);
    rec_c(a,b,c+1,end_letter); // recurse
}

void rec_b(char a,char b,char end_letter) { // j-loop
    if (!(b <= end_letter)) return;
    rec_c(a,b,start_letter,end_letter); // inner loop
    rec_b(a,b+1,end_letter); // recurse
}

void rec_a(char a, char end_letter) { // i-loop
    if (!(a <= end_letter)) return;
    rec_b(a,start_letter,end_letter); // inner loop
    rec_a(a+1,end_letter); // recurse
}

int main(){
    rec_a(start_letter,end_letter);
}







