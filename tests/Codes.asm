// push temp 4
@4
D = A
@5
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1

// pop temp 6
@6
D = A
@5
D = D + A
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

// push pointer 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1

// pop pointer 0
@SP
M = M - 1
A = M
D = M

@THIS 
M = D