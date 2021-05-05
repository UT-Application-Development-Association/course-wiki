## Course Introduction
CSC488 is one of the few courses in CS that requires CSC324 as a prerequisite. But in essence, it does not have much overlap with the CSC324. CSC324 is talking about Programming Language at a macro level, while 488 is focusing on explaining the principles of Compiler. The main content of CSC488 will talk about Compiler's complete pipeline from take source input to generating executable. At the same time, there will be 6 assignments corresponding to the content.

The front end of Compiler Pipeline includes Lexical Analysis, Syntax Analysis and Semantic Analysis, and the back end includes Intermediate Representation Generation, Machine Independent Optimization, Target Machine Code Generation and Machine Dependent Optimization.

Lexical Analysis is responsible for removing the useless text (such as whitespace comment, etc.) in the Source Program while extracting the necessary Token and passing it to Syntax Analysis

Syntax Analysis is responsible for converting the Token extracted by Lexical Analysis into the grammatical structure of Parse Tree to represent the entire language. The parsing that Compiler often says actually happens in Syntax Analysis. Generally, Parsing is divided into two categories: Top-Down Parsing and Bottom-Up Parsing. The two types of Parsing have different extensions, such as LL Parsing in Top-Down Parsing and Recursive Descendent Parsing in Bottom-Up Parsing. Parse Tree represents a complete grammatical structure, but often we do not need every detail in Parse Tree, so we need to simplify Parse Tree and leave only the necessary parts in Parse Tree to obtain Abstract Syntax Tree (AST) and AST It is also the most important Data Structure in the Compiler front end

Semantic Analysis is responsible for traverse AST to fill the Symbol Table so that necessary information can be recorded. Common errors can also be found in the process of traverse AST, such as variable redefinition, incorrect operand type, etc.

Intermediate Representation Generation is responsible for converting AST to Platform Independent representation, which is the so-called Intermediate Representation (IR). Now the most commonly used IR is LLVM (Low Level Virtual Machine) IR. The principle of IR Gen is the same as that of Semantic Analysis. It also needs traverse AST, which translates the statement and expression of the entire program into the corresponding LLVM Instruction according to the Symbol Table filled in the Semantic Analysis.

Machine Independent Optimization is responsible for analyzing IR to make changes to achieve optimization. Generally speaking, Compiler Optimization mostly refers to Machine Independent Optimization, which is optimization performed without considering Target Machine. Common Machine Independent Optimization includes Memory to register promotion, Common Subexpression Elimination, Constant Propagation, Dead Code Elimination, etc. In LLVM, optimization is carried out through Pass. LLVM has two Passes: Analysis Pass and Transform Pass. Analysis Pass is usually used to obtain information, such as which definitions on a program point are reachable, which variables are live or which expressions are available, etc. The Analysis Pass is only responsible for analyzing the information extracted from the IR and not making any changes to the IR. . Transform Pass is responsible for modifying the IR, such as deleting an Instruction, replacing the argument in the Instruction, or adding a new Instruction.

Machine Code Generation is responsible for translating IR into instruction corresponding to Target Machine. There are two general tasks of Machine Code Generation: Instruction Selection and Register Allocation. In some architectures, there are multiple different instructions that can be used to do the same thing. Instruction Selection is responsible for selecting the correct instruction for IR. LLVM IR assumes there are infinite amount of virtual register, but when the actual translation is done, the number of physical registers on each target machine is limited, so register allocation needs to allocate physical register to map to virtual registers and when the number of physical registers is not enough you need to select the physical register to spill the stored content to the memory so that it can be allocated

Machine Dependent Optimization is the platform-specific optimization based on the Target Machine after the Machine Code is generated.

## General course design
- 6 Assignments (75 %)
  - Environment Setup (4%)
  - Grammar and parse (10%)
  - AST (11%)
  - Semantic Analysis (12%)
  - IR Generation (22%)
  - IR Optimization (16%)
- Final Exam (25%)

## Permanent Professor

## Course difficulty
In general, the content of the 488 class is not very difficult. The content cover in the lecture is actually deeper than that used in Assignment and exams. So if there are parts that you don’t understand in Lecture, don’t worry too much. If you can finish the assignments then you will not have a big problem for the exam. Generally speaking, it is a class with moderate difficulty to learn something.

-Content difficulty: 3.5/5

-Homework difficulty: 3.5/ 5

-Workload: 3.5/ 5

-Overall difficulty: 3.5/ 5
