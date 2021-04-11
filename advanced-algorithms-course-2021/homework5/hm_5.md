### Homework 5

#### Q1
The number of executions for the line 8 depends on the dictionary D.  
If D is emtpy then A.len - 1 times, if D contains all computed routes  
then 0. If init state for D is D.len = 0, then for the first Compute-Route(A, D)  
call D would be called for A.len - 1  times, for the second time D would be  
called for 0 times, because D must already contain best routes.  

#### Q2
A new k_A,D value will be increased after adding a new location, because in    
this case the D will contain pairs which don't have computed paths.  
No paths for between A[i-1], A[i] and A[i], A[i+1].  

I guess these values depend on how many times the COMPUTE-ROUTE was called  
before comparing k_A',D with k_A,D.  
The difference range must be in 0 <= k_A',D - k_A,D <= 2.

### Q3


