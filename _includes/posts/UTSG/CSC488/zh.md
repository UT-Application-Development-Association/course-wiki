## 课程介绍
CSC488这门课是CS里为数不多需要CSC324做prerequisite的课。但本质上它和324并没有太大的overlap。CSC324是宏观的在讲Programming Language，而488则是侧重于讲解Compiler的原理。CSC488的主线会讲Compiler从take source input到生成executable的全套pipeline同时会有6个作业对应所讲的内容。

Compiler Pipeline的前端包括Lexical Analysis, Syntax Analysis和Semantic Analysis, 后端则包含了Intermediate Representation Generation, Machine Independent Optimization, Target Machine Code Generation和Machine Dependent Optimization。

Lexical Analysis是负责将Source Program中没用的text(例如whitespace comment等)挪除同时将必要的Token提取出来传递给Syntax Analysis

Syntax Analysis负责将Lexical Analysis提取出来的Token转化为Parse Tree用来代表整个语言的语法结构。Compiler常说的parsing其实就是发生在Syntax Analysis。大体上的Parsing分为两种分别为Top-Down Parsing和Bottom-Up Parsing。而这两种Parsing中又有不同的延展例如Top-Down中的LL Parsing和Bottom-Up中的Recursive Descendent Parsing。Parse Tree代表了完整的语法结构，但是往往我们并不需要Parse Tree里的每一个细节，所以需要将Parse Tree进行简化只留下Parse Tree中必要的部分从而得到了Abstract Syntax Tree(AST) 而AST也是Compiler前端中最重要的Data Structure

Semantic Analysis负责traverse AST用来填充Symbol Table从而可以record必要的信息。而常见的error也可以在traverse AST的过程中被发现例如variable redefinition，incorrect operand type, etc.

Intermediate Representation Generation负责将AST转换为Platform Independent的representation也就是所谓的Intermediate Representation(IR)现在最常用的IR就是LLVM(Low Level Virtual Machine) IR。IR Gen的原理和Semantic Analysis相同它也需要traverse AST，根据在Semantic Analysis中填充好的Symbol Table来将整个program的statement和expression 翻译成对应的LLVM Instruction。

Machine Independent Optimization负责分析IR对其进行更改从而达到优化。通常所说的Compiler Optimization大多统指Machine Independent Optimization，也就是在不考虑Target Machine的前提下进行的Optimization。常见的Machine Independent Optimization有Memory to register promotion, Common Subexpression Elimination，Constant Propagation, Dead Code Elimination等。而在LLVM中优化是通过Pass进行的, LLVM有两种Pass分别是Analysis Pass和Transform Pass。Analysis Pass通常是用来获取信息例如在一个program point上有哪些definition是reachable，哪些variable是live 亦或者哪些expression是available的等等， Analysis Pass只负责分析从IR中提取信息不对IR进行任何的更改。Transform Pass则是负责对IR进行修改，例如删掉一个Instruction，替换Instruction中的argument亦或是添加新的Instruction。

Machine Code Generation负责将IR翻译成为对应Target Machine的Instruction。Machine Code Generation大体的工作有两个分别为Instruction Selection和Register Allocation。 在一些architecture中会有多个不同的instruction可以被用来做同样的事情Instruction Selection就需要负责对IR挑选正确的Instruction。LLVM IR中assume会有infinite amount of virtual register但是当真正翻译的时候每台target machine上的physical register的数量是有限的，所以register allocation需要allocate physical register用来map到virtual register以及当physical register数量不够的时候需要挑选physical register将它储存的内容spill到memory从而可以被allocate

Machine Dependent Optimization则是在生成好Machine Code后跟据Target Machine进行Platform特有的优化

## 大体课设
- 6 Assignments (75 %)
	- Environment Setup (4%)
	- Grammar and parse (10%)
	- AST(11%)
	- Semantic Analysis(12%)
	- IR Generation(22%)
	- IR Optimization(16%)
- Final Exam(25%)

注：上述课设来源于2021Winter，仅供参考

## 常驻教授

## 课程难度
总体来说488这么课内容上其实并不是十分的难，课上cover的内容其实比Assignment和考试中要用得到的会深，所以如果Lecture上有没听懂的部分不用太担心，如果能把Assignment做好其实对于考试就问题不大。总体还是一节难度适中能学到东西的一节课

- 内容难度:  3.5/ 5

- 作业难度:  3.5/ 5

- Workload:  3.5/ 5

- Overall难度:  3.5/ 5
