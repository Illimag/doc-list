# How to write a "hello world" program in assembly language.

Test.asm:

	section .text
	global _start

	_start:
	    mov eax, 60

Without 

	xor edi, edi
	syscall

Causes this error when compiling:

	segmentation fault (core dumped)

Without 

	syscall

test.asm program continues to execute in memory until failure. 

So needs exit command.

	xor edi, edi

zeros out the EDI register.

EDI contains value returned when program exits.

https://stackoverflow.com/questions/39559371/assembly-nasm-segmentation-fault-what-does-it-mean

Full test.asm:

	section .text
	global _start

	_start:
	    mov eax, 60
	    xor edi, edi
	    syscall

Compiling test.asm

	sudo apt-get install nasm
	nasm -f elf64 test.asm
	ld -e _start -o test test.o

Without

	elf64

There is error:

	ld: i386 architecture of input file `test.o' is incompatible with i386:x86-64 output

Development environment is 

	x86-64

So need to have

	elf64

Also needs to have the version of hello_world program that can run on system which is linux.

Replaced all registers with 64-bit.

int 80h is replaced with syscall.


	64-bit Linux

	# ----------------------------------------------------------------------------------------
	# Writes "Hello, World" to the console using only system calls. Runs on 64-bit Linux only.
	# To assemble and run:
	#
	#     gcc -c hello.s && ld hello.o && ./a.out
	#
	# or
	#
	#     gcc -nostdlib hello.s && ./a.out
	# ----------------------------------------------------------------------------------------

	        .global _start

	        .text
	_start:
	        # write(1, message, 13)
	        mov     $1, %rax                # system call 1 is write
	        mov     $1, %rdi                # file handle 1 is stdout
	        mov     $message, %rsi          # address of string to output
	        mov     $13, %rdx               # number of bytes
	        syscall                         # invoke operating system to do the write

	        # exit(0)
	        mov     $60, %rax               # system call 60 is exit
	        xor     %rdi, %rdi              # we want return code 0
	        syscall                         # invoke operating system to exit
	message:
	        .ascii  "Hello, world\n"

Changed it into 

	hello_world.s

The

	hello.asm

still as an 

	Segmentation fault (core dumped)

error.

I don't know why.

	http://cs.lmu.edu/~ray/notes/syscalls/

## What is a system call?

The operating system is responsible for

- Process Management (starting, running, stopping processes)
- File Management(creating, opening, reading, writing, renaming files)
- Memory Management (allocating, deallocating memory)
- Other stuff (timing, scheduling, network management)

An application program makes a system call to get the operating system to preform a service for it, like reading from a file.

# One nice thing about syscalls is that you don't have to link with a C library, so your executables can be much smaller.
