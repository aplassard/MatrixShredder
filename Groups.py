try:
    import numpypy
except:
    pass
import numpy as np

class Groups(object):
    def __init__(self,file_name,header,id,header_names,start,end=-1):
        self.file_name = file_name
        self.id = id
        self.start = start
        self.end = end
        f = open(self.file_name)
        for i in range(header):
            line = f.readline().strip().split('\t')
            if i + 1 == header_names:
                self.header_names = line[self.start:self.end]
        self.ids = []
        features = []
        for line in f:
            line = line.rstrip().split('\t')
            self.ids.append(line[self.id])
            features.append(line[self.start:self.end])
        self.features = np.array(features,dtype=float)
        del features

    def run(self,n):
        for i in range(len(self.header_names)):
            indices = self._get_n_max(n,i)
            yield [self.ids[idx] for idx in indices]

    def _get_n_max(self,n,i):
        arr = self.features[:,i]
        indices = arr.argsort()[-n:][::-1]
        return indices

        

