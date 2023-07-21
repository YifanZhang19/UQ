function C=myMatMult(A,B)
% My own matrix multiplication function
[n,m]=size(A);
[p,q]=size(B);
if m~=p % Check number of cols of A equals number of rows of B
    error('Dimension mismatch')
end
C=zeros(n,q);
for i=1:n
    for j=1:q
        C(i,j) = dot(A(i,:),B(:,j)); % Dot product of i-th row of A and j-th column of B
    end
end