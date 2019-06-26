# The 17,576 Names of God

"In the Short short story 'The Nine Billion Names of God', author Arthur C. Clarke
writes about a group of monks who are determined to figure out the names of
God. They have devised a phonetic alphabet and have written down various
combinations of sounds, but they can work only so fast. So, they hire a computer
company to install a system that can quickly create 9 billion permutations
of the sounds, one of which is likely to be the Name of God. The idea is that,
after God's name is known, the world will end.

It's a charming story, all the more so because desktop computers can now
also calculate the name of God, as long as you properly code them with the
monk's alphabet, write the program, and then sit and wait for the output to
compile.

The following program uses three nested loops to generate every possible
3-letter combination using the common English alphabet. This example isn't
sufficient to produce the Name of God, so the world doesn't end when you run
the program."

Here is the program that does 17,576 of the 9 billion:

    #include <stdio.h>

    int main(){
        char a,b,c;
        /* Test to see total number of combinations
        int i = 1; 
        */
        for(a='A';a<='Z';++a){
            for(b='A';b<='Z';++b){
                for(c='A';c<='Z';++c){
                    printf("%c%c%c\t",a,b,c);
                    /* This will print the current number of the combination
                    printf("%d",i);
                    ++i;
                    */
                }
            }
        }
        return(0);
    }

What if we need to find all 9 billion?

? - ? = 9,000,000,000


    A - Z = 26
    AA - ZZ = 676
    AAA - ZZZ = 17,576

    26*26*26 = 17,576
    or 
    26^3 = 17,576

    or

    x = log26(17,576)
    x = 3

    so

    x = log26(9,000,000,000)
    x = around 7 

AAAAAAA - ZZZZZZZ = 9,000,000,000 (it's way closer to 8,000,000,000 but let's just say 9,000,000,000)

Here is the program that does 9 billion:

    #include <stdio.h>

    int main(){
        char a,b,c,d,e,f,g;
        /* Test to see total number of combinations
        int i = 1; 
        */
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
        return(0);
    }

The program that measure the time it takes to find 17,576 is here:

    AAA_ZZZ_time_calculation.c

The program that measure the time it takes to find 9 billion is here:

    AAAAAAA_ZZZZZZZ_time_calculation.c

