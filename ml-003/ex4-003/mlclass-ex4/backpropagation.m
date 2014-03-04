function [Theta1_grad, Theta2_grad] = backpropagation(Theta1, Theta2, X, y)
%
m = size(X, 1);
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

for t = 1:m
    % forward propagation
    a1 = [1 X(t,:)];
    z2 = a1*Theta1';
    a2 = sigmoid(z2);
    a2 = [1 a2];
    z3 = a2*Theta2';
    a3 = sigmoid(z3);
    
    % back propagation
    d3 = a3 - y(t,:);
    d2 = d3*Theta2(:,2:end) .* sigmoidGradient(z2);

    Theta1_grad = Theta1_grad + d2'*a1;
    Theta2_grad = Theta2_grad + d3'*a2;
end

Theta1_grad = Theta1_grad / m;
Theta2_grad = Theta2_grad / m;

end
