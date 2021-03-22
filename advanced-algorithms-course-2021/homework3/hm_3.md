## Homework 3

### Question 1  

Let's denote a number of elements for each array, **n - A.length** 
and **m - B.length**. Since this algorithm computes a distance for
each element of **A** between each element of **B** then it leads to 
a complexity of a brute force algorithm, in this case it would: **O(nm) + O(1)**.  
In case n is closer enough or equals to m then: **Θ(n^2)**


### Question 2

DistanceBST gets called 3 times per iteration and DistanceNumBST ger called 2 times,
O(1) if for simple operations   
**T(n) = 3T((n+1)/2) + 2log(n+1) + O(1)**  


### Question 3

           Tree A                    Tree B

             27                        29
          /      \                  /      \
        16        35              19        42
      /   \      /  \            /  \      /  \ 
    10    22   31    45        13    25  38    54


`distance_bst(A, B) = 2, closest elements:  27 - 29 = 2`   

I chose the Master theorem for solving the following recursion **T(n) = 3T(n/2) + log(n)** :  
Based on the Master theorem we got: k = 0, p = 1, a = 3, b = 2  
log<sub>2</sub><sup>3</sup> = 1.585, log<sub>2</sub><sup>3</sup> > 0,
then it's a 1st case: **Θ(n^1.585)**

### Question 4

Overall complexity for generation two trees A and B from arrays
and computing distance between them would like: 
**O(n) = 2nlog(n) + 3log(n) + 2log(n) + O(1) =**
**2nlog(n) + 5log(n) + O(1)**  

Distance array complexity: **O(n^2)**  
Despite a complex formula from Q3 it's obvious that this formula
is more efficient than distanceArray: **Θ(n^2) > Θ(nlog(n))** and **Θ(n^2) > Θ(n^1.585)**

### Question 5

list_a: 10 16 22 27 31 35 45  
list_b: 13 19 25 29 38 42 54  

```
distanceSortedArray(A, B)
  min_d = ∞
  i = 1
  j = 1
  while i < A.len AND j < B.len
    d = abs(A[i] - B[i])
    if d == 0
      return 0
    if min_d > d
      min_d = d
    if A[i] > B[j]
      j = j + 1
    else
      i = i + 1
  return mid_d

```

Complexity: **O(n+m)**, where n = A.len, and m = B.len  
Since we know that all values are sorted, we can simply iterate through 
two lists and search for a minimal difference between values.
In case of 0 there is no sense to proceed the loop if we know that
the possible minimal value is 0