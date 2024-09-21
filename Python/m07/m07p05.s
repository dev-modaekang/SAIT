	.file	"m07p05.c"
	.text
	.globl	_funptr
	.data
	.align 4
_funptr:
	.long	1975641597
	.globl	_program
	.align 4
_program:
	.ascii "calc.exe\0"
	.def	___main;	.scl	2;	.type	32;	.endef
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB28:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	_funptr, %eax
	movl	$2, 4(%esp)
	movl	$_program, (%esp)
	call	*%eax
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE28:
	.ident	"GCC: (MinGW.org GCC-8.2.0-3) 8.2.0"
