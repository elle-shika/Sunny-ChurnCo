
import numpy as np
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.base import BaseEstimator, TransformerMixin

class LogTransformer():
    def __init__(self, constant=1e-5):
        self.constant = constant

    def fit(self, x, y = None):
        return self
    
    def transform(self, x):
        return np.log1p(x + self.constant)
    

class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, score_func=mutual_info_classif, k=5):
        self.score_func = score_func
        self.k = k
        self.selector = SelectKBest(score_func=self.score_func, k=self.k)

    def fit(self, X, y=None):
        self.selector.fit(X, y)
        return self

    def transform(self, X):
        return self.selector.transform(X)