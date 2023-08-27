
% Dimension (length) of a vector
v1 = [1] %scalar
v2 = [1,2] %point in the plane
v3 = [1,2,3] %point in space
v4 = [1,2,3,4] %point in higher dimension
pause
fprintf("length of v3 = %d\n",length(v3))
pause
length(v4)
pause
help length
pause % Linear combinations of vectors
v1 = [1,2,3]
v2 = [4,5,6]
a1 = 2
a2 = -1
pause
a1*v1 + a2*v2
pause % Dot product
v1*v2'
pause
dot(v1,v2)
pause
sum(v1.*v2)
pause % Norms
norm(v1)
pause
norm(v1,2)
pause
sqrt(v1*v1')
pause
norm(-v1)
pause
[norm(v1,1),norm(-v1,1)]
pause % Normalizing a vector
normvect = @(v) v./norm(v)
pause
vn=normvect(v1)
pause
fprintf("The norm of the normed vector: %g\n",norm(vn))
pause
u = [10, 0]
v = [-5, -5]
pause
theta=acos(dot(u,v)/(norm(u)*norm(v)))
pause
rad2deg(theta)
pause
help angle
pause
u = [10, 0]
v = [5, 5]
pause
costheta=dot(u,v)/(norm(u)*norm(v))
pause
[costheta, sqrt(2)/2]
pause % Triangle inequality
n = 10; % Length of vectors
N = 10^4; % Number of vectors
arr1 = []; % Initialize an empty array
for i = 1:N
    u=rand(n,1);
    v=rand(n,1);
    cs = norm(u)*norm(v)-abs(dot(u,v)); % Cauchy-Schwarz
    arr1=[arr1,cs]; % Append to the array
end
min(arr1)
pause
hist(arr1,100)
pause % Matrices
imagesc(rand(300,300))
pause
H=zeros(10,10);
for i = 1:10
    for j = 1:10
        if (i==j+4)||(i==j-2)
            H(i,j)=1;
        end
    end
end
H
pause
imagesc(H)
pause
A=[1 2 ; 3 4] % 2 by 2 matrix
B=[-2 3 ; 1 3]
C=[0 1 2; -1 1 0] % 2 by 3 matrix
pause
A+B
pause
% A+C would produce an error
pause
3*A
pause % Matrix multiplication
% Four ways
% - Dot products
% - Cols
% - Rows
% - Outer product
A
B
A*B
pause
% To get the 9 value in the entry 1,2 of the product AB, I take the inner 
% product of the first row of A and the second column of B
A(1,1)*B(1,2) + A(1,2)*B(2,2)
pause
B*A % matrix multiplication is not commutative in general
pause 
% myMatMult function
myMatMult(A,B)
pause
% myMatMult(C,A) would give an error
myMatMult(A,C)
pause
rand('state',0)
A=rand(100,100);
tic
for i=1:1000
    A=A*rand(100,100); % Multiplication using LAPACK routines
end
toc
pause
rand('state',0)
A=rand(100,100);
tic
for i=1:1000
    A=myMatMult(A,rand(100,100));
end
toc
pause
x=[7 12 33]
A=x(randi(length(x),5,3)) % select entries uniformly at random from x
y=[-1 0 24 23 522 4]
B=y(randi(length(y),3,10)) % select entries uniformly at random from y
pause
A*B
pause
myMatMult2(A,B)
pause
A*B - myMatMult2(A,B)
pause
norm(A*B - myMatMult2(A,B))
pause % Matrix multiplication is associative
A= rand(2,4)
B= rand(4,5)
C= rand(5,3)
A*B*C
pause
(A*B)*C
pause
A*(B*C)
pause % Identity matrix
A = [1 2; 3 4]
I = eye(2) % create identify matrix
A*I
pause
(A*I - A)==0
pause
I*A
pause % creating an identity matrix
ones(3,1)
pause
myI = diag(ones(2,1))
pause
help diag
pause
diag(myI) % retrieves the diagonal elements
pause % trace of a (square) matrix is the sum of its diagonal elements
A = [1 2 3; 4 5 6; 7 8 9]
sum(diag(A))
pause
trace(A)
pause % create a banded matrix
diag([5,7,0],1)+diag([2 3 4],-1)
pause % Inverses
A=[1 2; 3 4]
pause
help inv
pause
Ai = inv(A) % We rarely do this in practice
pause
A*Ai
pause
Ai*A
pause
A=[1 2; 3 4]
B=[5 6; 7 8]
inv(A*B)
pause
inv(B)*inv(A)
pause
inv(A)*inv(B) % something different
pause % Transpose
A=[];
for i=1:3 % rows
    for j=1:3 % cols
        A(i,j)=j+3*(i-1);
    end
end
A
pause
A=reshape((1:9),3,3)'
pause
A' % transpose, flips rows and cols
pause
ctranspose(A) % complex conjugate transpose (adjoint)
pause
A=[1+2*sqrt(-1) 2 - 3*sqrt(-1); -sqrt(-1) 0]
pause
A'
pause
ctranspose(A)
pause
A=reshape((1:9),3,3)'
pause
A''
pause
isequal(A,A') % check if the matrix is symmetric
pause
S=(A'+A)./2 % symmetrizing the matrix
pause
isequal(S,S')
pause
B=A+3
pause
(A*B)'
pause
B'*A'
pause % Determinants
A=[1 2; 3 4]
pause
det(A)
pause
A(1,1)*A(2,2) - A(1,2)*A(2,1)
pause
% det([1 2 3; 4 5 6]) would give error as it is not a square matrix
det(diag(ones(5,1)))
pause
A=diag([1 2 3])
pause
det(A) % det of diagonal is product of diagonal elements
pause
A(2,3)=-53;
A(1,3)=7;
A
pause
det(A) % determinant of a triangular matrix is the product of its diagonal elements (upper or lower)
pause
A(3,1)=35;
A
pause
det(A) % Not triangular anymore --- no longer the product of the diagonals
pause
setdiff((1:4),2) % set difference
pause % myDet function
myDet(A)
pause
det(rand(100,100)) % Arbitrary random matrices won't have determinant zero
pause
myDet(rand(100,100)) % Takes a very long time
pause
A=rand(4,4)
B=rand(4,4)
det(A*B)
det(A)*det(B)
pause
det(inv(A))
pause
1/det(A)
pause
A=[1 0; 1 0] % det will be zero
det(A)
pause
inv(A) % A is non-invertible / singular matrix
pause
B = [1 2 3; 4 5 6; 5 7 9] % third row is sum of first two
det(B)
inv(B) % numerical trouble
pause
myDet(B)
pause
cond(B) % condition number - coming toward the end of the course
pause
help cond
pause % Inverse of a 2 x 2 matrix
A = rand(2,2)
Ai = inv2mat(A)
pause
Ai*A
pause % Application: k-means
x = iris_dataset % could have used "load fisheriris"
K = 2 % number of clusters
rand('state',0) % set the random seed (for reproducability)
[idx,C] = kmeans(x(1:2,:)',K) % perform clustering on the first two dimensions
figure, % First plot the clusters
plot(x(1,idx==1),x(2,idx==1),'b.')
hold on
plot(x(1,idx==2),x(2,idx==2),'g.')
plot(x(1,idx==3),x(2,idx==3),'r.')
plot(C(:,1),C(:,2),'k.','markersize',20) % Plot the cluster centroids
hold off
pause % manual implementation of k-means (2D data)
n=size(x,2); % number of data points
dataPoints = x(1:2,randperm(n)); % shuffle the data points
xMin = min(x(1,:));
xMax = max(x(1,:));
yMin = min(x(2,:));
yMax = max(x(2,:));
for i =1:K % Random initial centroids
    means(i,:) = [xMin + (xMax-xMin).*rand(1),yMin + (yMax-yMin).*rand(1)];
end
labels=randi(K,n,1); % Random initial labels
prevMeans = -means;

while norm(prevMeans-means) > 0.001 % While centroids haven't converged
   prevMeans=means;
   for i=1:n % Update the labels based on closest points to centroids
       minNorm=inf;
       for j=1:K
          if norm(means(j,:)-dataPoints(:,i)')<minNorm
              labels(i)=j;
              minNorm=norm(means(j,:)-dataPoints(:,i)');
          end
       end
   end
   for i=1:K % Update centroids
       means(i,:)=mean(dataPoints(:,labels==i),2);
   end
end

figure, % First plot the clusters
plot(dataPoints(1,labels==1),dataPoints(2,labels==1),'b.')
hold on
plot(dataPoints(1,labels==2),dataPoints(2,labels==2),'g.')
plot(dataPoints(1,labels==3),dataPoints(2,labels==3),'r.')
plot(means(:,1),means(:,2),'k.','markersize',20) % Plot the cluster centroids
hold off



