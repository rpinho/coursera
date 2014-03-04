function J = lrCostFunctionUnreg(predictions, y)
%LRCOSTFUNCTION Compute cost for logistic regression without 
%regularization

m = length(y); % number of training examples

cost = -y.*log(predictions) - (1-y).*log(1-predictions);
J = 1/m * sum(cost(:));
end