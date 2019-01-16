section     .text
global      _start                              ;must be declared for linker (ld)

_start:                                         ;tell linker entry point

    mov     rax,len                             ;message length
    mov     rdi,msg                             ;message to write
    mov     rsi,1                               ;file descriptor (stdout)
    mov     rdx,4                               ;system call number (sys_write)
    xor edi, edi                                ;call kernel
    syscall

    mov     rax,1                               ;system call number (sys_exit)
    mov rdi, 0
    xor edi, edi                              ;call kernel
    syscall

section     .data

msg     db  'Hello, world',0xa                 ;our dear string
len     equ $ - msg                             ;length of our dear string
