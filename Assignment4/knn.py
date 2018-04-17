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
       
        distances = []
        predict = []
        for x in range(len(X)):
            for i in range(len(self.X_train)):
                distance = np.linalg.norm(np.array(X.iloc[x])-np.array(self.X_train.iloc[i]))
                distances.append([distance,i])
            voters = [i[1] for i in sorted(distances)[:k]]
            predict.append(Counter(voters).most_common(1)[0][0])
        return predict