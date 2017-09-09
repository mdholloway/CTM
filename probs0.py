# 0.8.1
def increments(L): return [x+1 for x in L]

# 0.8.2
def cubes(L): return [x*x*x for x in L]

# 0.8.3
def tuple_sum(A, B): return [(A[i][0]+B[i][0],A[i][1]+B[i][1]) for i in range(len(A))]

# 0.8.4
def inv_dict(d): return {b:a for (a,b) in d.items()}

# 0.8.5
def row(p, n): return [p+i for i in range(n)]

# 0.8.6
Yes, because it is both one-to-one and onto.

# 0.8.7
No, because it is not onto. It could be made invertible if the final element n were removed from V, or an element m were added to U such that f(m) = n.

# 0.8.8
No, there is no possible domain of g that will contain the image of f where the domain of f consists of all real numbers. If the domain of f were restricted to non-negative real numbers, then the expression would be defined.

# 0.8.9
Yes:
1->23
2->22
3->21

# 0.8.10
Pr(even-out) = Pr(odd-in) = Pr(1) + Pr(3) + Pr(5) = 0.7 
Pr(odd-out) = Pr(even-in) = Pr(2) + Pr(4) + Pr(6) = 0.3

# 0.8.11
Pr(0-out) = Pr(3) + Pr(6) = 0.3
Pr(1-out) = Pr(1) + Pr(4) + Pr(7) = 0.4 
Pr(2-out) = Pr(2) + Pr(5) = 0.3
