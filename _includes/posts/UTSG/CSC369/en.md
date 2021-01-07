## Course Introduction
CSC369 is the coding course in the last two compulsory courses in CS Specialist.  This lesson revolves around operating systems and three themes of the OS that are persistence, concurrency, and virtualization.

The meaning of persistence is to ensure that data can be stored persistently on the host, even if an accident occurs, to ensure as little data loss as possible. The file system (file system) in the OS is a very huge set of applications
Software for managing files on disks, CSC369 will introduce many file systems that existed in history such as fat, ext2, etc. The first major assignment of CSC369 is also to design and implement a file system.

Concurrency is a major problem of modern development. Modern development does not only involve one program running at a time, but many programs are running at the same time. The purpose of concurrency is to ensure that multiple programs run at the same time without triggering any problems. One of the most common problems is how to handle multiple programs requesting access to a resource at the same time. In order to ensure that resources can be accessed correctly, CSC369 will introduce different methods
for example, semaphore, lock, conditional variable, and a famous concurrency problem namely dining philosopher.
The second assignment of CSC369 revolves around multi-threading programs to ensure that resources can be accessed correctly and that dead lock will not be triggered.

The core of virtualization is to give the physical address a layer of virtualization to generate a virtual address and assign a virtual address space to each program.
It makes every program think that it has the illusion of a whole memory. When the program needs to access memory data, the OS is responsible for translating the virtual address to the real physical address, and different translation mechanisms and algorithm for switching pages are involved here.
The third assignment of CSC369 is to implement memory translation and various page switching algorithms

## General course design
- Assignment
    + File System
      
    + Multi- Threading
      
    + Virtual Memory
- Term Test
  
- Final

## Professor(s)
Karen Reid: Karen has taught CSC369 for many years.  Karen is a very good professor and the lectures are clear. If you have questions, she will be willing to help you. , The content of the exam will not be particularly difficult, overall she is a very good professor

## Course difficulty
CSC369 can be said to be a nightmare for many student in the CS Specialist. Workload can be said to be relatively large (or even the largest section) in the first three years of CS. This course requires solid C programming skills and
a lot of time to debug, this class is definitely not a class that you can start writing before due and resulting high marks. The homework of this class must start early.
Make sure you don’t have too much workload. And **strongly not recommended** do not take this course in the same semester as CSC373, it is very likely that there is no time for you to sleep.

- Content difficulty: 3.5/5

- Homework difficulty: 4/5

- Workload: 4.0 / 5

- Overall difficulty: 4.0 / 5