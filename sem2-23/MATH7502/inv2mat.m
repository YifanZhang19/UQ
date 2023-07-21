function out = inv2mat(A)
[m,n]=size(A);
if n~=m
    error('Dimension mismatch')
end
if n~=2
    error('This is for a 2 by 2 matrix only')
end
Delta = det(A);
if Delta == 0
    error('Matrix is singular')
end
a=A(1,1);
b=A(1,2);
c=A(2,1);
d=A(2,2);
out = [d -b; -c a]./Delta;