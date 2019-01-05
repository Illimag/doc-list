#include <stdio.h>
#include <time.h>
 
int main() {
    char a,b,c,d,e,f,g;
    clock_t start, end;
    /* Store start time here */
    start = clock();

    for(a='A';a<='Z';++a){
            for(b='A';b<='Z';++b){
                for(c='A';c<='Z';++c){
                    for(d='A';d<='Z';++d){
                        for(e='A';e<='Z';++e){
                            for(f='A';f<='Z';++f){
                                for(g='A';g<='Z';++g){
                                    printf("%c%c%c%c%c%c%c\t",a,b,c,d,e,f,g);
                                    /* This will print the current number of the combination
                                    printf("%d",i);
                                    ++i;
                                    */
                                }
                            }
                        }
                    }
                }
            }
        }
        

    end = clock();
    /* Get the time taken by program to execute in seconds */
    double duration = ((double)end - start)/CLOCKS_PER_SEC;
     
    printf("Time taken to execute in seconds : %f", duration);
    return 0;
}


