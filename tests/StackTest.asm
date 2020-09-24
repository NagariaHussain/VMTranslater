
// push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 17
@17
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

// push constant 17
@17
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 16
@16
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
@TRUE_eq_1
// Jump if x == y
D;JEQ

// Jump unconditionally
@FALSE_eq_1
0;JMP

(TRUE_eq_1)
@SP
A = M
M = -1

@END_eq_1
0;JMP

(FALSE_eq_1)
@SP
A = M
M = 0

(END_eq_1)
// SP++;
@SP
M = M + 1

// push constant 16
@16
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 17
@17
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
@TRUE_eq_2
// Jump if x == y
D;JEQ

// Jump unconditionally
@FALSE_eq_2
0;JMP

(TRUE_eq_2)
@SP
A = M
M = -1

@END_eq_2
0;JMP

(FALSE_eq_2)
@SP
A = M
M = 0

(END_eq_2)
// SP++;
@SP
M = M + 1

// push constant 892
@892
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1

// lt
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
@TRUE_lt_0
// Jump if x < y
D;JLT

// Jump unconditionally
@FALSE_lt_0
0;JMP

(TRUE_lt_0)
@SP
A = M
M = -1

@END_lt_0
0;JMP

(FALSE_lt_0)
@SP
A = M
M = 0

(END_lt_0)
// SP++;
@SP
M = M + 1

// push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 892
@892
D = A
@SP
A = M
M = D
@SP
M = M + 1

// lt
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
@TRUE_lt_1
// Jump if x < y
D;JLT

// Jump unconditionally
@FALSE_lt_1
0;JMP

(TRUE_lt_1)
@SP
A = M
M = -1

@END_lt_1
0;JMP

(FALSE_lt_1)
@SP
A = M
M = 0

(END_lt_1)
// SP++;
@SP
M = M + 1

// push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 891
@891
D = A
@SP
A = M
M = D
@SP
M = M + 1

// lt
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
@TRUE_lt_2
// Jump if x < y
D;JLT

// Jump unconditionally
@FALSE_lt_2
0;JMP

(TRUE_lt_2)
@SP
A = M
M = -1

@END_lt_2
0;JMP

(FALSE_lt_2)
@SP
A = M
M = 0

(END_lt_2)
// SP++;
@SP
M = M + 1

// push constant 32767
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1

// gt
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
@TRUE_gt_0
// Jump if x > y
D;JGT

// Jump unconditionally
@FALSE_gt_0
0;JMP

(TRUE_gt_0)
@SP
A = M
M = -1

@END_gt_0
0;JMP

(FALSE_gt_0)
@SP
A = M
M = 0

(END_gt_0)
// SP++;
@SP
M = M + 1

// push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 32767
@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1

// gt
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
@TRUE_gt_1
// Jump if x > y
D;JGT

// Jump unconditionally
@FALSE_gt_1
0;JMP

(TRUE_gt_1)
@SP
A = M
M = -1

@END_gt_1
0;JMP

(FALSE_gt_1)
@SP
A = M
M = 0

(END_gt_1)
// SP++;
@SP
M = M + 1

// push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 32766
@32766
D = A
@SP
A = M
M = D
@SP
M = M + 1

// gt
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
@TRUE_gt_2
// Jump if x > y
D;JGT

// Jump unconditionally
@FALSE_gt_2
0;JMP

(TRUE_gt_2)
@SP
A = M
M = -1

@END_gt_2
0;JMP

(FALSE_gt_2)
@SP
A = M
M = 0

(END_gt_2)
// SP++;
@SP
M = M + 1

// push constant 57
@57
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 31
@31
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push constant 53
@53
D = A
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

// push constant 112
@112
D = A
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

// neg
@SP
M = M - 1
A = M
M = -M

@SP
M = M + 1

// and
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
M = D & M
@SP
M = M + 1

// push constant 82
@82
D = A
@SP
A = M
M = D
@SP
M = M + 1

// or
@SP
M = M - 1
A = M
// D becomes y
D = M

@SP
M = M - 1
A = M
M = D|M
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
