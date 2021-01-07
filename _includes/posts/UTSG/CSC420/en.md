## Course Introduction
Image understanding can be said to be a very popular and cutting- edge field of AI. The human eye is very high-precision and can recognize many things, but for the computer, the essence of a photo is actually a 2d array, each representing one pixel.
From a computer's point of view, a photo is just a bunch of numbers, and it cannot directly make any decisions. CSC420 mainly introduces the analysis of these pixels through different algorithms, including Edge Detection, Corner Detection, SIFT, Camera Model.

Edge Detection: Edge Detection can be said to be the first stage in Image Understanding. CSC420 introduces two ways to detect edge, Canny Edge Detector and Laplacian of Gaussian. Both of these are obtained by filtering the pixels in the photo after using different filters on the photo.

Corner Detection: Corner is a common feature in Image. Corner can be used for image matching. A common way to find Corner in Image is Harris Corner Detection. Its principle is based on Image gradient and Weighted Matrix. Filter the pixels in the photo to get the corner of the photo

SIFT: The SIFT stands for the Scale-invariant feature transform. The meaning of SIFT is that SIFT can still detect the features in the photo even after the size of the photo is changed and rotated. SIFT uses Difference of Gaussian to form a set of Image Pyramid so that SIFT can detect the photos after the size changes and calculate the gradient magnitude and orientation of the keypoint neighbour for rotation detection.

Hologram: The core of Hologram is to switch the viewingfrom 2d to 3d. Its focus is to convert 2d coordinates to 3d coordinates through the camera mode to achieve a 3d perspective

## General course design
- 4 Programming Assignments

- Team Project

## Professor(s)
Morteza Rezanejad: Morteza is a new professor of the UofT. He personally doesn't like to answer some questions repeatedly. He usually asks you to refer to these questions by telling you where he has answered them. But other than that, he is willing to answer most of the questions for you and he will also give you a certain hint

## Course difficulty
CSC420 is a course focuses on the application. It will explain the algorithms and principles in image understanding but it will not explain the principles in depth. Assignment will have two parts written and programming which correspond to short answer and algorithm implementation respectively. The final project is to choose one of the given topics to implement and the project usually requires knowledge of machine learning.

- Content difficulty: 3.5/5

- Homework difficulty: 3.5 / 5

- Workload: 3.5 / 5

- Overall difficulty: 3.5 / 5