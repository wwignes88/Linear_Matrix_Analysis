These files are posted prematurely in an effort to show off some coding/ math ability for the sake of a volunteer application with the city of Portland.

By 'linear matrix analysis' I mean analyzing or solving the equation Ax = b where A is some matrix and x,b are vectors. Such a general equation is so often encountered in linear algebra and data analysis, and I spent a reasonable amount of time programming the various techniques, that the various means of analyzing it are worthy of their own repository. 

- Solver.py file will tell you if the system is linearly dependent, independent, or has no solution.
- span_space_test.py file will test a set of vectors and tell you if they span the space. 
- Poly_min.py will give the minimum polynomial of a matrix.

What I'm currently working on finishing is Jordan matrix analysis. The Jordan form of a matrix is an extremely fundamental and powerful conceptin in linear algebra (and consequently data analysis). It is what I intuitively suspect to be a healthy means of in some way performing an optimization analysis without naively applying idealizations - a thing inherent to much of optimization theory. Jordan matrix analysis also happens to be extremely fundamental to quantum mechanical theory (a thing you'd think to be entirely unrelated to data analysis and quantitative trading, but that is only what I want you to think).

I plan on using these algorithms for quantitative trading purposes. For now the files are posted as is. In the future, when I'm actually using them regularly for my own trading, I'll make more of an effort to describe what they do.
