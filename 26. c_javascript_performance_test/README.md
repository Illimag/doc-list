# C and Javascript performance test

Jaemin Kim
5/26/2019

## Description

This is a test to see the difference in performance between C and Javascript in the browser.

There will be three tests:

- Compile and run C file with GCC
- Run Javascript with Node.js
- Compile C file with Emscripten and run the WASM file with Node.js

## Overview

C compiled with Emscripten and running with WebAssembly is almost twice as fast than running a similar Javascript file.

Two tests, printing the output to file, printing to console.

One thing that is unusual is why when printing the output to a file, Javascript is faster than C compiled with Emscripten and running with WebAssembly.

## Environment

A test will be run in a local machine with node.js and GCC.

## Algorithm

Both the C and Javascript algorithms are 5 nested loops that print the output.

Because the algorithms are similar we can assume that if there is a performance difference it will be because of the languages the algorithm was written in.

Also will wrap the algorithm in code that times the execution time. Then prints the execute time.

Here is the C code:

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

Here is the Javascript code:

    var start = new Date();
    function main(){
        for (a=0;a<=25;++a){
            for(b=0;b<=25;b++){
                for(c=0;c<=25;c++){
                    for(d=0;d<=25;d++){
                        for(e=0;e<=25;e++){
                            console.log(a,b,c,d,e)
                        }
                    }
                }	
            }
        }
    }
    main();
    var time = new Date() - start;
    console.log("Call to doSomething took " + (time) + " milliseconds.")

## Compiling C into WASM to run with Javascript and node.js

The development environment is WSL (Window Subsystem for Linux - Bash for Windows 10) Ubuntu 16.04. Emscripten is used to compile the C file into WASM format which is WebAssembly format, as well as a Javascript file. 

In the local Emscripten Environment run

    ./emcc test.c

The output files will be:

    a.out.wasm
    a.out.js

The files are located in:

    C/WASM

## Local machine

The two scripts will be run on the same machine. The details of the machine can be found in the machine0.txt file.

## Running scripts with Local Environment

- Compile and run C file with GCC

Compile C file with GCC

    gcc test.c -o test

Run the outputed file

    ./test

- Run Javascript with Node.js

    node --max-old-space-size=8192 test.js

- Run the WASM file with Node.js

    node --max-old-space-size=8192 a.out.js

NOTE: Without the flag:

    --max-old-space-size=8192

Will run into memory issues.

## Outcome

### First Test:

Outputted into text file:

- Compile and run C file with GCC

    1.031250 Seconds

(Buffer is being flushed after each /n)

- Run Javascript with Node.js

    120.248 Seconds

- Compile C file with Emscripten and run the WASM file with Node.js

    154.282000 Seconds
    127.466000 seconds

### Second Test:

Run in shell.

- Compile and run C file with GCC

    335.437500 Seconds

- Run Javascript with Node.js

    3519.292 Seconds

- Compile C file with Emscripten and run the WASM file with Node.js

    1846.183000 Seconds

Find a better way to times the programs instead of using clock() and CLOCKS_PER_SECOND
