function grad = lrGradFunctionReg(X, y, theta, lambda)
%lrGradFunctionReg Compute gradient for linear and logistic regression
%   with regularization

m = length(y); % number of training examples

grad = lrGradFunctionUnreg(X, y, theta);
grad(:,2:end) = grad(:,2:end) + lambda/m * theta(2:end)';

end