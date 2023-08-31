function result = matrix_multiply(A, B, flag)
    [rowsA, colsA] = size(A);
    [rowsB, colsB] = size(B);
    
    if colsA ~= rowsB
        error('Matrix dimensions are not same.');
    end
    
    result = zeros(rowsA, colsB);
    
    if flag == 1
        disp('Dot product method')
        for i = 1:rowsA
            for j = 1:colsB
                result(i, j) = dot(A(i, :), B(:, j));
            end
        end
    elseif flag == 2
        disp('Linear combination of columns method')
        for i = 1:colsB
            result(:, i) = A * B(:, i);
        end
    elseif flag == 3
        disp('Linear combination of rows method')
        for i = 1:rowsA
            result(i, :) = A(i, :) * B;
        end
    elseif flag == 4
        disp('Sum of outer products method')
        for i = 1:colsB
            result = result + A(:, i) * B(i, :);
        end
    end
end


