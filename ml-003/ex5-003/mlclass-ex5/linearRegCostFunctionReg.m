function J = linearRegCostFunctionReg(X, y, theta, lambda)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

m = length(y); % number of training examples

% Unreg
J = linearRegCostFunctionUnreg(X, y, theta);
% Reg
reg = sum(theta(2:end).^2);
J = J + lambda/(2*m) * reg;

end