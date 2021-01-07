## Course Introduction
Geometry Processing is a relatively new field. The main content of Geometry Processing is the analysis and operation of 3D objects. The main content of CSC419 is to teach these operations and corresponding knowledge including reconstruction, alignment, denoising, shape deformation, surface parameterization, curvature.

Reconstruction: The essence of Reconstruction is to reconstruct countless 3D scanned sample points into a 3D object. One of the common methods is Poisson Reconstruction, which is approximated by gradient based on 3d point cloud and normal vector for reconstruction.

Alignment: The purpose of Alignment is to match the scans of an object and the same object at different positions and different perspectives so that they overlap as much as possible. For this reason, the Iterative Closest Point (ICP) algorithm is introduced based on the sample points and the objective function. The optimal rotation matrix and thereby minimize the objective function until the algorithm converge, that is, the surfaces coincide with each other

Denoising: The meaning of Denoising is to denoise the surface of the object, including texture, shape, etc. Here, we will cover Cotangent Laplacian and Massmatrix, which are very commonly used in Geometry Processing.

Deformation: The main research of Deformation is to simulate the deformation of objects, such as stretching and rotating objects. Here will introduce two kinds of deformation methods, biharmonic and as-rigid-as-possible.

Parameterization: The essence of Parametrization is actually to express 3d surface through 2d. Common texture mapping (adding texture to objects) is also the use of parameterization

Curvature: Curvature represents the curvature of the surface of an object. Many algorithms can determine the boundary condition based on Curvature.

## General course design
- 7 Programming Assignments

- Paper Implementation

## Professor(s)
Alec Jacobson: Alec can be said to be one of the leaders of Geometry Processing. He has made great achievements in Geometry Processing. At the same time, the quality of his own teaching is also very good. The lectures are also very clear. A really good professor.

## Course difficulty
CSC419 has high requirements for mathematics, especially calculus and optimization. This class mainly focuses on explaining the mathematical principles of each part, and the homework will require the implementation of the content of the class. The workload of the CSC419 job is not huge, but it requires a very good understanding of the content or there is even no way to start the assignment. And the final project is to choose one from the provided paper for implementation and presentation.

- Content difficulty: 4/5

- Homework difficulty: 3.5 / 5

- Workload: 3.5 / 5

- Overall difficulty: 4/5