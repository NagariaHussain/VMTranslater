
// push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 11
@11
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push local 10
@10
D = A
@LCL 
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push static 5
@Codes.5
D = M
@SP
A = M
M = D
@SP
M = M + 1

// pop static 2
@SP
M = M - 1
A = M
D = M

@Codes.2
M = D
