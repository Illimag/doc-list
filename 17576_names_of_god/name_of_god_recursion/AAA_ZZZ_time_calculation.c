#include <stdio.h>
char first_letter,second_letter,third_letter;

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



    for (first_letter = start_letter; first_letter <= end_letter; first_letter++) {
        for (second_letter = start_letter; second_letter <= end_letter; second_letter++) {
            for (third_letter = start_letter; third_letter <= end_letter; third_letter++) {

            }
        }
    }





void rec_c(char a,char b,char c,char end_letter) { // k-loop
    if (!(c <= end_letter)) return;

    rec_c(a,b,c+1,end_letter); // recurse
}

void rec_b(char a,char b,char end_letter, char end_letter) { // j-loop
    if (!(b <= end_letter)) return;
    rec_c(a,b,start_letter,end_letter); // inner loop
    rec_b(a,b+1,end_letter); // recurse
}

void rec_a(char a, char end_letter) { // i-loop
    if (!(a <= end_letter)) return;
    rec_b(a,start_letter,end_letter); // inner loop
    rec_a(a+1,end_letter); // recurse
}
...
rec_a(start_letter,end_letter);




for (i = 0; i < q; i++) {
        for (j = 0; j < p; j++) {
            for (k = 0; k < r; k++) {

            }
        }
    }



void rec_k(int k,int r,int i,int j) { // k-loop
    if (!(k<r)) return;

    rec_k(k+1,r,i,j); // recurse
}

void rec_j(int j,int p,int i,int r) { // j-loop
    if (!(j<p)) return;
    rec_k(0,r,i,j); // inner loop
    rec_j(j+1,p,i,r); // recurse
}

void rec_i(int i,int q,int p,int r) { // i-loop
    if (!(i<q)) return;
    rec_j(0,p,i,r); // inner loop
    rec_i(i+1,q,p,r); // recurse
}
...
rec_i(0,q,p,r);






