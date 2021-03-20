## Homework 3

### Question 1  

Let's denote a number of elements for each array, **n - A.length** 
and **m - B.length**. Since this algorithm computes a distance for
each element of **A** between each element of **B** then it leads to 
a complexity of a brute force algorithm, in this case it would: **O(nm) + O(1)**.  

### Question 2

DistanceBST gets called 3 times per iteration and DistanceNumBST ger called 2 times,
O(1) if for simple operations   
**T(n) = 3T(n+1) + 2lg(n+1) + O(1)**  


### Question 3

           Tree A                    Tree B

             27                        29
          /      \                  /      \
        16        35              18        42
      /   \      /  \            /  \      /  \ 
    10    20   31    45        13    25  38    54