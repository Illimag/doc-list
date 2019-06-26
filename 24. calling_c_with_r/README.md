# Using R - To call C code

From this URL:

    http://mazamascience.com/WorkingWithData/?p=1067

"One of the reasons R has so much functionality is that people have incorporated a lot of academic code written in C, C++, Fortran and Java into various packages.

Libraries written in these languages are often both robust and fast.

If you are using R to support people in a particular field, you may be called upon to incorporate some outside code into your R environment.

Unfortunately, much of the documentation on how to do this is written at a very high level.

In this post we will distil some of the available infor on calling C code from R into three "Hello World" examples.

Most programmers have some experience with the C language.

C is low level, quite fast and is often used to write other programming languages including about 50% of R and most of the Python Standard Library.

Many Libraries of C code exist that can greatly enchance the speed and functionality of R for a particular use case.

Most of the time, C code will be used to speed up algorithms involving loops which can be very slow in R, but there are other reasons to link R with existing C libraries.

Baby steps."

### Birth of C code.

Here is a simple hello world script in C.

### helloA.c

    #include <stdio.h>

    int main()
    {
        printf("Hello World!\n");
    }

On Unix/Linux systems you can combile with:

    make

Which will take care of starting up the complier with the right complier flags and arguements.

    $ make helloA
    cc     helloA.c   -o helloA
    $ ./helloA
    Hello World!

I'm currently using Ubuntu 16 subsystem on Windows 10.

Also you can compile the code with:

    gcc helloA.c -o helloA

To make this executable easier to run from our R session, we'll create a file named:

    wrappers.R

where we will put a wrapper function that will invoke this C code:

    # Wrapper function to invoke "helloA" at the shell.
    helloA <- function() {
    system(paste(getwd(),"helloA",sep="/"))
    }

Now we can start up R and try out our new function.

I don't know why RStudio isn't printing out "Hello World".

At first it would give me this error: 

    Error in +helloA <- function() { : object 'helloA' not found

Turns out I need to run the program from source or have the file system at the folder with the files in it.

But still doesn't work, it runs but doesn't print.

Here's a different version of hello world.

### hello.c

    #include <R.h>

    void hello(int *n)
    {
        int i;

        for(i=0;i<*n;i++){
            Rprintf("Hello, world!\n");
        }
    }

### There is no main function. 

Since we arnt really trying to write a C program just a C function, there is no need for a separate main function.

The function Rprintf is exactly like the standard printf function in C except that Rprintf sends its output to the R console so that you can see it when running R.

### Also instead of stdio.h we include R.h.

The wrapper to run the C progam is:

    hello2 <- function(n){
        .C("hello", as.integer(n))
    }

The first argument to .C is a quoted string containing the name of the C function to be called.

Recall that in the file hello.c we named out C function hello.

Therefore the first arguement to .C in this case should be ''hello''.

The rest of the arguements to .C are arguments that need to be passed to the C function.

The C function only has one arguement, the number of times to print "Hello, world!", so we pass in the variable n (after coercing it to an integer).

The type to which you coerce the variables passed to the C function and the types in the prototype of your C function should match (as well as the order of the variables passed).

Notice that we coerce n to integer type using as.integer and in the C functuon we have set n to be type int* (rememeber that variables are always passed as pointers when using .C).

### Running the hello2 program

The first thing you must do is write the code!

We put the R code in a file called

    hello.R 

and the C code in a file called 

    hello.c

having done that we must then compile the C code.

At the command line (in your terminal window), we can type

    R CMD SHLIB hello.c

Ok got it to work on Ubuntu 16 Windows 10 subsystem.

With RStudio on Windows there is an error when:

    LoadLibrary failure:  %1 is not a valid Win32 application.

So I installed r-base-core on linux with this command:

    sudo apt install r-base-core

This allowed me to run:

    R CMD SHLIB hello.c

Which complies and outputs the .so file.

Then I installed r-cran-littler:

    sudo apt install r-cran-littler

Which allows us to run r from the terminal with:

    R "need to be capitalized"

From the R shell:

    source("hello.R")
    dyn.load("hello.so")
    hello2(5)

Output:

    Hello, world!
    Hello, world!
    Hello, world!
    Hello, world!
    Hello, world!
    [[1]]
    [1] 5

Quit R shell with:

    q()