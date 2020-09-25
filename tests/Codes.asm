// label WHILE_LOOP
(WHILE_LOOP)

// push constant 5
@5
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 3
@3
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 3
@3
D = A
@SP
A = M
M = D
@SP
M = M + 1

// eq
@SP
M = M-1
A = M
D = M
// D becomes y

@SP
M = M-1
A = M
D = M-D

// D becomes x - y
@TRUE_eq_0
// Jump if x == y
D;JEQ

// Jump unconditionally
@FALSE_eq_0
0;JMP

(TRUE_eq_0)
@SP
A = M
M = -1

@END_eq_0
0;JMP

(FALSE_eq_0)
@SP
A = M
M = 0

(END_eq_0)
// SP++;
@SP
M = M + 1

// if-goto label
@SP
M = M - 1
A = M
D = M

@WHILE_LOOP
D;JLT
