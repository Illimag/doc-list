#include <stdio.h>
 
int main() {
    char a,b,c;
    char name;
    for(a='A';a<='Z';++a){
            for(b='A';b<='Z';++b){
                for(c='A';c<='Z';++c){
                    name = a + b + c;
                    printf("%c\t",name);
                }
            }
        }
}


