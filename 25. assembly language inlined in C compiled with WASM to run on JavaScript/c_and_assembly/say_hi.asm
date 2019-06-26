SECTION .TEXT
	GLOBAL say_hi

say_hi:
	mov rax,4            ; write()
	mov rdi,1            ; STDOUT
	mov rsi,hello
	mov rdx,helloLen
	syscall                 ; Interrupt

	mov rax,60
	mov rdi,0
	syscall


SECTION .DATA
        hello:     db 'Hello world',10
        helloLen:  equ $-hello
