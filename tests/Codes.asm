
// function SimpleFunction.test 2     
(SimpleFunction.test)
@2   
D = A
(SimpleFunction.test$local$loop)

@SimpleFunction.test$local$end
D;JLE

@SP
A = M
M = 0
@SP
M = M + 1

@SimpleFunction.test$local$loop
D = D - 1
0;JMP
(SimpleFunction.test$local$end)

// push local 0
@0
D = A
@LCL 
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push local 1
@1
D = A
@LCL 
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1

// add
@SP
M=M-1
A=M
D = M
@SP
M = M - 1
A = M
M = D + M
@SP
M = M + 1

// not
// neg
@SP
M = M - 1
A = M
M = !M

@SP
M = M + 1     

// push argument 0
@0
D = A
@ARG 
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1

// add
@SP
M=M-1
A=M
D = M
@SP
M = M - 1
A = M
M = D + M
@SP
M = M + 1

// push argument 1
@1
D = A
@ARG 
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1

// sub
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
M = M - D
@SP
M = M + 1

// return

// endFrame = LCL
@LCL
D = M

@R13
M = D

// retAddr = *(endFrame - 5)
@5
D = D - A
A = D
D = M

@R14
M = D

// *ARG = pop()
@SP
M = M - 1
A = M
D = M

@ARG
A = M
M = D

// SP = ARG + 1
@ARG
D = M

@SP
M = D + 1

// THAT = *(endFrame - 1)
@R13
A = M - 1
D = M

@THAT
M = D

// THIS = *(endFrame - 2)
@2
D = A

@R13
D = M - D
A = D
D = M

@THIS
M = D

// ARG = *(endFrame - 3)
@3
D = A

@R13
D = M - D
A = D
D = M

@ARG
M = D

// LCL = *(endFrame - 4)
@4
D = A

@R13
D = M - D
A = D
D = M

@LCL
M = D

@R14
A = M
0;JMP
