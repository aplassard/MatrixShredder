try:
    import numpypy
except:
    pass
import numpy as np

class Shred(object):
    def __init__(self,file_name,header,id,start,end=-1):
        self.file_name = file_name
        self.id = id
        self.start = start
        self.end = end
        f = open(self.file_name)
        features = []
        ids = []
        for i in range(header):
            line = f.readline().strip().split('\t')
        self.feature_map = {}
        for line in f:
            line = line.rstrip().split('\t')
#            self.feature_map[line[self.id]] = np.array(line[self.start:self.end],dtype=float)
            features.append(np.array(line[self.start:self.end],dtype=float))
            ids.append(line[self.id])
        features = np.array(features,dtype=float)
        for i in xrange(features.shape[1]):
            feature = features[:,i]
            mean = feature.mean()
            std = feature.std()
            features[:,i] = (feature-mean)/std
        for i in xrange(len(ids)):
            self.feature_map[ids[i]] = features[i,:]
    def get_matrix(self,indices):
        return np.array( [self.feature_map[idx] for idx in indices])
