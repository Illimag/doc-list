#ifndef A_Z_H
#define A_Z_H

#include <stdio.h>
#include <stdlib.h>

// https://stackoverflow.com/questions/44397474/convert-nested-loop-to-recursion
char a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
char start_letter = 'A';
char end_letter = 'Z';





void rec_z(char a,char b,char c,char end_letter) {
    if (!(c <= end_letter)) return;
    printf("%c%c%c\t",a,b,c);
    rec_z(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z+1,end_letter);
}


void rec_y(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char r,char s,char t,char u,char v,char w,char x,char z,char end_letter){
    if (!(y <= end_letter)) return;
    rec_z(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,start_letter,end_letter);
    rec_y(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y+1,end_letter);
}

void rec_x(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char r,char s,char t,char u,char v,char w,char x,char end_letter){
    if (!(x <= end_letter)) return;
    rec_y(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,start_letter,end_letter);
    rec_x(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x+1,end_letter);
}

void rec_w(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char r,char s,char t,char u,char v,char w,char end_letter){
    if (!(w <= end_letter)) return;
    rec_x(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,start_letter,end_letter);
    rec_w(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w+1,end_letter);
}

void rec_v(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char r,char s,char t,char u,char v,char end_letter){
    if (!(v <= end_letter)) return;
    rec_w(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,start_letter,end_letter);
    rec_v(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v+1,end_letter);
}

void rec_u(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char r,char s,char t,char u,char end_letter){
    if (!(u <= end_letter)) return;
    rec_v(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,start_letter,end_letter);
    rec_u(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u+1,end_letter);
}

void rec_t(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char r,char s,char t,char end_letter){
    if (!(t <= end_letter)) return;
    rec_u(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,start_letter,end_letter);
    rec_t(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t+1,end_letter);
}

void rec_s(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char r,char s,char end_letter){
    if (!(s <= end_letter)) return;
    rec_t(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,start_letter,end_letter);
    rec_s(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s+1,end_letter);
}

void rec_r(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char r,char end_letter){
    if (!(r <= end_letter)) return;
    rec_s(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,start_letter,end_letter);
    rec_r(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r+1,end_letter);
}

void rec_q(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char q,char end_letter){
    if (!(q <= end_letter)) return;
    rec_r(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,start_letter,end_letter);
    rec_q(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q+1,end_letter);
}

void rec_p(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char p,char end_letter){
    if (!(p <= end_letter)) return;
    rec_q(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,start_letter,end_letter);
    rec_p(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p+1,end_letter);
}

void rec_o(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char o,char end_letter){
    if (!(o <= end_letter)) return;
    rec_p(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,start_letter,end_letter);
    rec_o(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o+1,end_letter);
}

void rec_n(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char n,char end_letter){
    if (!(n <= end_letter)) return;
    rec_o(a,b,c,d,e,f,g,h,i,j,k,l,m,n,start_letter,end_letter);
    rec_n(a,b,c,d,e,f,g,h,i,j,k,l,m,n+1,end_letter);
}

void rec_m(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char m,char end_letter){
    if (!(m <= end_letter)) return;
    rec_n(a,b,c,d,e,f,g,h,i,j,k,l,m,start_letter,end_letter);
    rec_m(a,b,c,d,e,f,g,h,i,j,k,l,m+1,end_letter);
}

void rec_l(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char l,char end_letter){
    if (!(l <= end_letter)) return;
    rec_m(a,b,c,d,e,f,g,h,i,j,k,l,start_letter,end_letter);
    rec_l(a,b,c,d,e,f,g,h,i,j,k,l+1,end_letter);
}

void rec_k(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char k,char end_letter){
    if (!(k <= end_letter)) return;
    rec_l(a,b,c,d,e,f,g,h,i,j,k,start_letter,end_letter);
    rec_k(a,b,c,d,e,f,g,h,i,j,k+1,end_letter);
}

void rec_j(char a,char b,char c,char d,char e,char f,char g,char h,char i,char j,char end_letter){
    if (!(j <= end_letter)) return;
    rec_k(a,b,c,d,e,f,g,h,i,j,start_letter,end_letter);
    rec_j(a,b,c,d,e,f,g,h,i,j+1,end_letter);
}

void rec_i(char a,char b,char c,char d,char e,char f,char g,char h,char i,char end_letter){
    if (!(i <= end_letter)) return;
    rec_j(a,b,c,d,e,f,g,h,i,start_letter,end_letter);
    rec_i(a,b,c,d,e,f,g,h,i+1,end_letter);
}

void rec_h(char a,char b,char c,char d,char e,char f,char g,char h,char end_letter){
    if (!(h <= end_letter)) return;
    rec_i(a,b,c,d,e,f,g,h,start_letter,end_letter);
    rec_h(a,b,c,d,e,f,g,h+1,end_letter);
}

void rec_g(char a,char b,char c,char d,char e,char f,char g,char end_letter){
    if (!(g <= end_letter)) return;
    rec_h(a,b,c,d,e,f,g,start_letter,end_letter);
    rec_g(a,b,c,d,e,f,g+1,end_letter);
}

void rec_f(char a,char b,char c,char d,char e,char f,char end_letter){
    if (!(f <= end_letter)) return;
    rec_g(a,b,c,d,e,f,start_letter,end_letter);
    rec_f(a,b,c,d,e,f+1,end_letter);
}

void rec_e(char a,char b,char c,char d,char e, char end_letter){
    if (!(e <= end_letter)) return;
    rec_f(a,b,c,d,e,start_letter,end_letter);
    rec_e(a,b,c,d,e+1,end_letter);
}

void rec_d(char a,char b,char c,char d,char end_letter){
    if (!(d <= end_letter)) return;
    rec_e(a,b,c,d,start_letter,end_letter);
    rec_d(a,b,c,d+1,end_letter);
}

void rec_c(char a,char b,char c,char end_letter){
    if (!(c <= end_letter)) return;
    rec_d(a,b,c,start_letter,end_letter);
    rec_c(a,b,c+1,end_letter);
}

void rec_b(char a,char b,char end_letter) {
    if (!(b <= end_letter)) return;
    rec_c(a,b,start_letter,end_letter);
    rec_b(a,b+1,end_letter);
}

void rec_a(char a, char end_letter) {
    if (!(a <= end_letter)) return;
    rec_b(a,start_letter,end_letter);
    rec_a(a+1,end_letter);
}

int main(){
    rec_a(start_letter,end_letter);
}


#endif