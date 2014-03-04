function map = mapLabelToBinary(y, num_labels)
%  The vector y passed into the function is a vector of labels
%  containing values from 1..K. You need to map this vector into a 
%  binary vector of 1's and 0's to be used with the neural network
%  cost function.

m = size(y,1);
map = zeros(m, num_labels);
for i=1:m
    map(i,:) = y(i) == 1:num_labels;
end
end