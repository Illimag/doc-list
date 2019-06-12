### Assembly language inlined in C compiled with WASM to run on JavaScript.

## Whats the relationship between assembly language and machine language

https://stackoverflow.com/questions/1253272/whats-the-relationship-between-assembly-language-and-machine-language

Machine language is the "Bit encoding" of a CPU's opcodes or the actual bits used to control the processor in the computer, usually viewed as a sequence of hexadecimal numbers (typically bytes).

Assembly language is the "Symbolic encoding" of a CPU's opcode or a more human readable view of machine language. Instead of representing the machine language as numbers, the instructions and registers are given names (typically abbreviated words, or mnemonics, eg ld means "load"). 

Here is a program written in Assembly language that says "Hello".

Important to note that this program is written on an development environment that is 64-bit Linux.

As so will need to use:

	elf64

to compile with:

	nasm

If nasm isn't installed it can be installed with this command:

	sudo apt-get install nasm

All registers are 64-bit.

	SECTION .text
	    GLOBAL test

	    test:
	        ; print name
	        mov rax,1     ; sys_write
	        mov rdi,1     ; stdout
	        mov rsi,name  ; start address of name
	        mov rdx,7 ; length
	        syscall

	        ; exit program
	        mov rax,60    ; sys_exit
	        mov rdi,0     ; success
	        syscall

	SECTION .data
	    name DB "Hello",10

Save this file as:

	test.asm

Compile the program with this command:

	nasm -f elf64 test.asm

It will output file:

	test.o

Now link the file and the exe with this command:

	ld -o test test.o

We can run the program that says "Hello" with this command:

	./test

This is assembly program that we will inline inside the C file.

Now create a new file called:

	example.c

We will write a simple C program that will call the Assembly program:

	#include <stdio.h>

	int main() {
	        int test();
	        test();
	}

Compile and link the C program to test if the assembly program runs from the C program.

	gcc example.c test.o -o hello

Run the script.

	./hello

## Installing Emscripten which compiles C/C++ code into JavaScript.

The development environment we will be installing on is WSL (Window Subsystem for Linux - Bash for Windows 10) Ubuntu 16.04.

First we need to have Python2.7, nodejs, CMake, Java, git installed.

	sudo apt-get install python2.7 nodejs cmake default-jre git-core
 
Remember to update as well:

	sudo apt-get update

Now we can clone the git repo:

	git clone https://github.com/juj/emsdk.git

Make sure to clone the repository in the directory that you want Emscripten to be hosted on your local machine.

	cd emsdk

### Download and install the latest SDK tools.

	./emsdk install latest

### Make the "latest" SDK "active" for the current user. (writes ~/.emscripten file)

	./emsdk activate latest

### Activate PATH and other environment variables in the current terminal

	source ./emsdk_env.sh

Now if everything is correctly installed we can do a test to compile a "hello world" written in C into a WASM file that can run with JavaScript.

If there are any issues it can because of some type of installation issue, that can be solved by looking for a solution over google and stackoverflow.

From the emsdk dir

	cd emscripten
	
### Version

	cd 1.38.12

	cd test_file

Let's make a C file named hello_world.c

	#include <stdio.h>
	int main(){
	printf("Hello, World");
	return(0);
	}

Now compile the C file with emcc

	../.././emcc hello_world.c

There will be three outputted files:

	a.out.js
	a.out.js.map
	a.out.wasm

We can run the js file with node:

	node a.out.js

It should print out:

	Hello, World

### Turns out we can't compile Assembly Language with Web Assembly

x86-specific register names won't work when compiling to portable platform-neutral / architecture-neutral web assembly instead of directly to x86 asm.

A browser running on an ARM CPU won't have those registers available when JITing webasm into native code. Even a browser compiled for 32-bit x86 won't have those registers.

Also, a browser running on x86-64 Windows will have those registers available, but Linux system-call ABIs won't work.

AFAIK, you can't wrap target-specific inline asm and specific registers in web-asm even if your only intended target is one where they would work. The web-asm language isn't designed to support it.

When you run gcc or clang, the target is WASM, not x86.

https://stackoverflow.com/questions/53137018/web-assembly-compile-c-file-with-inline-assembly-language-error

