
// pop local 3
@3
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

// pop local 3
@3
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
