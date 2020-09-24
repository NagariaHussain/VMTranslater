
// push constant 5
@5
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 7
@7
D = A
@SP
A = M
M = D
@SP
M = M + 1

// add
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
M = D + M
@SP
M = M + 1

// pop local 0
@0
D = A
@LCL
D = D + M
@SP
A = M
M = D
@SP
M = M - 1
@SP
D = M
A = A + 1
A = M
M = D

// push static 5
@Codes.5
D = M
@SP
A = M
M = D
@SP
M = M + 1

// pop argument 5
@5
D = A
@ARG
D = D + M
@SP
A = M
M = D
@SP
M = M - 1
@SP
D = M
A = A + 1
A = M
M = D
