import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_covtype
from sklearn import linear_model 

import torch
import torch.optim as optim

class LogisticRegression:
    def __init__(self):
        pass

    def fit(self, X, y, lr=0.1, momentum=0, niter=100):
        '''
        Train a multiclass logistic regression model on the given training set.

        Parameters
        ----------
        X: training examples, represented as an input array of shape (n_sample,
           n_features).
        y: labels of training examples, represented as an array of shape
           (n_sample,) containing the classes for the input examples
        lr: learning rate for gradient descent
        niter: number of gradient descent updates
        momentum: the momentum constant (see assignment task sheet for an explanation)

        Returns
        -------
        self: fitted model
        '''
        self.classes_ = np.unique(y)
        self.class2int = dict((c, i) for i, c in enumerate(self.classes_))
        y = np.array([self.class2int[c] for c in y])

        n_features = X.shape[1]
        n_classes = len(self.classes_)

        self.intercept_ = np.zeros(n_classes)
        self.coef_ = np.zeros((n_classes, n_features))

        # Implement your gradient descent training code here; uncomment the code below to do "random training"
        #self.intercept_ = np.random.randn(*self.intercept_.shape)
        #self.coef_ = np.random.randn(*self.coef_.shape)

        return self

    def predict_proba(self, X):
        '''
        Predict the class distributions for given input examples.

        Parameters
        ----------
        X: input examples, represented as an input array of shape (n_sample,
           n_features).

        Returns
        -------
        y: predicted class distributions, represented as an array of shape (n_sample,
           n_classes)
        '''

        # Modify the code below to implement the idea for avoiding numerical flow as described in Q4 (b)
        scores = X @ self.coef_.T + self.intercept_
        scores = np.exp(scores)
        return scores/scores.sum(axis=1).reshape(-1, 1)

    def predict(self, X):
        '''
        Predict the classes for given input examples.

        Parameters
        ----------
        X: input examples, represented as an input array of shape (n_sample,
           n_features).

        Returns
        -------
        y: predicted class labels, represented as an array of shape (n_sample,)
        '''

        # replace pass with your code
        pass

if __name__ == '__main__':
    X, y = fetch_covtype(return_X_y=True)
    X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.3, random_state=42)

    clf = linear_model.LogisticRegression()
    clf.fit(X_tr, y_tr)
    print(accuracy_score(y_tr, clf.predict(X_tr)))
    print(accuracy_score(y_ts, clf.predict(X_ts)))
