#include <time.h>
#include <stdio.h>
int main(){
    clock_t tic = clock();
    char a,b,c,d,e;
    for(a='A';a<='Z';++a){
        for(b='A';b<='Z';++b){
            for(c='A';c<='Z';++c){
                for(d='A';d<='Z';++d){
                    for(e='A';e<='Z';++e){
                                printf("%c%c%c%c%c\n",a,b,c,d,e);
                    }
                }
            }
        }
    }
    clock_t toc = clock();
    printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);
    return 0;
}