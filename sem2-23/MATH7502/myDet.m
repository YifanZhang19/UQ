function out = myDet(A)
[m,n]=size(A);
if n~=m
    error('Dimension mismatch')
end
if n==2 % 2 by 2 has simple formula
    out = A(1,1)*A(2,2)-A(1,2)*A(2,1);
else % higher dimension has a recursive formula
    out = 0;
    for i=1:n % pattern is + - + - ...
        out = out + (-1)^(i+1)*A(1,i)*myDet(A(2:n,setdiff((1:n),i)));
    end
end