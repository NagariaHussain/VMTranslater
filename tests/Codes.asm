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
// pop local 5
@5
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
