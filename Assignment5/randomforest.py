from decision_tree import decision_tree
from classifier import classifier

class random_forest(classifier):
    
    def __init__(self,trees=10, max_depth=-1):
        self.n_trees = trees
        self.max_depth = max_depth
        self.trees_list = None
       
    def fit(self,X,Y):
        import pandas as pd
        import numpy as np
        
        dataset_train = pd.concat([X, Y], axis=1)
        sample_size = 1.0
        feature_size = int(np.sqrt(len(X.iloc[0])-1))
        trees = list()
        
        for i in range(self.n_trees):
            dtree_clf = decision_tree()
            features = self.subfeatures(X.columns,feature_size)
            sample_X, sample_Y = self.subsample(dataset_train[features],sample_size)
            dtree_clf.fit(sample_X.values.tolist(),sample_Y.values.tolist())
            trees.append(dtree_clf)
        self.trees_list = trees
        return self.trees_list

        
    def predict (self,X_test):
        import operator
        from collections import defaultdict
        
        predictions = [t.predict(X_test.values.tolist()) for t in self.trees_list]
        hypothesis = []
        for x in range(0,len(X_test)):
            count =  defaultdict(int)
            for p in predictions:
                if p[x] != None:
                    count[p[x]] +=1
            max_vote = max(count.items(), key=operator.itemgetter(1))[0]
            hypothesis.append(max_vote)
        return hypothesis
        
    
    def subsample(self,dataset,ratio):
        import numpy as np
        sample = list()
        n_sample = round(len(dataset) * ratio)
        chosen_idx=np.random.choice(len(dataset), replace=False, size=n_sample)
        dataset_trimmed =dataset.iloc[chosen_idx]
        sample_X = dataset_trimmed.iloc[:,:-1]
        sample_Y = dataset_trimmed.iloc[:,-1]
        return sample_X, sample_Y
    
    def subfeatures(self,features, n_sample):
        import numpy as np
        return np.random.choice(features,n_sample,replace=False)