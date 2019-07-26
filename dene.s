	global start

	section .text

start:
	mov rbp, rsp
	lea rax, [rel retmain]
	push rax
	push rbp
	mov rbp, rsp
	jmp __label0
retmain:
	pop rdi
	mov rax, 0x2000001
	syscall
__label0:
	push 10
	lea rsp, [rbp - 8]
	lea rsp, [rbp - 8]
	push qword [rbp - 8]
	push 15
	pop rbx
	pop rax
	mov rcx, 0
	cmp rax, rbx
	setg cl
	push rcx
	pop rax
	cmp rax, 0
	je __label2
	push 3
	mov rax, [rbp + 8]
	pop rbx
	mov [rbp + 8], rbx
	lea rsp, [rbp + 8]
	mov rbp, [rbp]
	jmp rax
	jmp __label1
__label2:
	push qword [rbp - 8]
	push 5
	pop rbx
	pop rax
	mov rcx, 0
	cmp rax, rbx
	setl cl
	push rcx
	pop rax
	cmp rax, 0
	je __label4
	push 2
	mov rax, [rbp + 8]
	pop rbx
	mov [rbp + 8], rbx
	lea rsp, [rbp + 8]
	mov rbp, [rbp]
	jmp rax
	jmp __label3
__label4:
	push qword [rbp - 8]
	push 10
	pop rbx
	pop rax
	mov rcx, 0
	cmp rax, rbx
	setne cl
	push rcx
	pop rax
	cmp rax, 0
	je __label6
	push 4
	mov rax, [rbp + 8]
	pop rbx
	mov [rbp + 8], rbx
	lea rsp, [rbp + 8]
	mov rbp, [rbp]
	jmp rax
	jmp __label5
__label6:
	push 0
	mov rax, [rbp + 8]
	pop rbx
	mov [rbp + 8], rbx
	lea rsp, [rbp + 8]
	mov rbp, [rbp]
	jmp rax
__label5:
__label3:
__label1:
	lea rsp, [rbp - 8]
	push 1
	mov rax, [rbp + 8]
	pop rbx
	mov [rbp + 8], rbx
	lea rsp, [rbp + 8]
	mov rbp, [rbp]
	jmp rax

	section .data
var:	db 0