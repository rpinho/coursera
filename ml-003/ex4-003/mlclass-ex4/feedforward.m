function a = feedforward(Theta, X)
% Feedforward Propagation

m = size(X, 1);
a = X;
n_layers = size(Theta,2);
for i=1:n_layers
    a = [ones(m, 1) a];
    z = a*Theta(i).x';
    a = sigmoid(z);
end
end