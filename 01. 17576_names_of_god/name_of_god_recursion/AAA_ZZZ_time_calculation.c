// https://stackoverflow.com/questions/44397474/convert-nested-loop-to-recursion

#include <stdio.h>
char a,b,c;
char start_letter = 'A';
char end_letter = 'Z';

void rec_c(char a,char b,char c,char end_letter) { // k-loop
    if (!(c <= end_letter)) return;
    printf("%c%c%c\t",a,b,c);
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

