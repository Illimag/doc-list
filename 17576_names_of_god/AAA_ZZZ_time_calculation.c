#include <stdio.h>
#include <time.h>
 
int main() {
    char a,b,c;
    clock_t start, end;
    /* Store start time here */
    start = clock();

    for(a='A';a<='Z';++a){
            for(b='A';b<='Z';++b){
                for(c='A';c<='Z';++c){
                    printf("%c%c%c\t",a,b,c);
                }
            }
        }
        

    end = clock();
    /* Get the time taken by program to execute in seconds */
    double duration = ((double)end - start)/CLOCKS_PER_SEC;
     
    printf("Time taken to execute in seconds : %f", duration);
    return 0;
}


