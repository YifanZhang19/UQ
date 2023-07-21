function C=myMatMult2(A,B)
% Another way to implement matrix multiplication (Outer product)
[n,m]=size(A);
[p,q]=size(B);
if m~=p % Check number of cols of A equals number of rows of B
    error('Dimension mismatch')
end
C=zeros(n,q);
for k=1:m
    C=C+A(:,k)*B(k,:); % outer product
end