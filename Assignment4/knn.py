from classifier import classifier

class KNN(classifier):
    
    def __init__(self, k=3):
        self.X_train = None
        self.y_train = None
        
    def fit(self, X, Y): 
        self.X_train = X
        self.y_train = Y
        return
        
    def predict(self, X, k):
        import numpy as np
        from collections import Counter
       
        predict = []
        for i in range(len(X)):
            distances = []
            for j in range(len(self.X_train)):
                distance = np.linalg.norm(np.array(X.iloc[i])-np.array(self.X_train.iloc[j]))
                distances.append([distance,self.y_train.iloc[j]])
                
            voters = [d[1] for d in sorted(distances)[:k]]
            predict.append(Counter(voters).most_common(1)[0][0])    
        return predict