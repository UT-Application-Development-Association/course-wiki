## Course Introduction
CSC418 is a class that puts Computer Graphics on the stage. Computer Graphics and
Computer Vision is essentially different. In short word, Computer Vision takes a photo as input and analyzes various information in the photo through various algorithms. Whereas, Computer Graphics makes a photo or special effect based on the algorithms. CSC418 explains the main content of graphics from the beginning, including raster image, ray casting, ray tracing, boundary volume hierarchy, mesh, shader pipeline, kinematics, mass-spring system. At the end of the course, everyone will be free to make a project based on the content of the class.

Raster Image: Raster Image can be said to be the most common way to store images. A Raster Image is just a two-dimensional array. Each index stores the corresponding pixel value, which is the light intensity at the corresponding position. The essence of raster image operation is to operate on array

Ray Casting: Ray Casting is the first step of creating images. The main responsibility of Ray casting is to generate rays and shoot rays.

Ray Tracing: Ray Tracing is a set of imaging framework. Briefly Speaking, Ray Tracing needs to first generate rays through ray casting and shoot the ray to objects during the process the rays maybe reflected, refracted and absorbed according to the rules. Until the light source disappears.

Boundary volume hierarchy: A core problem in rendering is to calculate the position of the intersection of the ray and the object, but usually it requires a huge amount of calculation and encounters objects that do not need to be considered, so in order to improve efficiency, the Boundary Volume Hierarchy is introduced. The essence of Boundary Volume Hierarchy is that Data Structure performs augmentation on the position of the object to reduce the amount of calculation.

Mesh: A popular way of expressing objects in the Graphics is through mesh. Mesh has two major components: location information and topology information. The position information stores the position of a mesh vertex, and the topology information is how meshes are connected together. Through these two parts, a mesh can be constructed to restore a 3d object.

Shader Pipeline: Shader Pipeline mainly describes a pipeline from the GPU receiving information from the CPU to the output location, including shading, transformation, projection, etc.

Kinematics: Kinematics mainly talks about how to simulate object motion through different algorithms

Mass-Spring System: A common method for simulating physical deformation is the Mass-Spring System. Mass Spring System is composed of mass points and springs. Each mass point contains a series of mass points connected by multiple springs, so that physical simulation can be performed through time integration.

## General course design
- 8 Programming Assignments

- Term Test

- Project

- Final

## Professor(s)
Alec Jacobson: Alec can be said to be a professor who changed the course of CSC418. Many of the contents of CSC418 were expanded by him. Alec himself is also a very knowledgeable professor with excellent teaching quality. He is also very welcome to answer questions for students. A really nice professor.

David Levin: David is a professor with a great sense of humor.  In short, David's class will not be boring. Like Alec, David is also a professor with excellent professional background and content delivery.

## Course difficulty
CSC418 is a very interesting but relatively large-workload class. The weekly programming assignment corresponds to the knowledge described in each week of the course. It is a good review of the content of the class, but each assignment will require a lot of time in the debugging.
It will be hard to start writing before due. At the same time, this class is a class that has certain requirements for C++ and Linear Algebra. Especially, you need a good linear algebra background for understanding the later half of the course. It is recommended to review Linear Algebra before going to CSC418. But overall is a very interesting lesson

- Content difficulty: 3.5/5

- Homework difficulty: 3.5 / 5

- Workload: 4/5

- Overall difficulty: 4/5