function grad = lrGradFunctionUnreg(X, y, theta)
%lrGradFunctionReg Compute gradient for linear and logistic regression
%   without regularization

m = length(y); % number of training examples

predictions = X*theta;
grad = 1/m * (predictions-y)' * X;

end