try:
    import numpypy
except:
    pass
import numpy as np

class Groups(object):
    def __init__(self,file_name,header,id,header_names,entrez_id,start,end=-1):
        self.file_name = file_name
        self.id = id
        self.start = start
        self.end = end
        self.entrez = []
        self.entrez_map = {}
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
            self.entrez.append(line[entrez_id])
            self.entrez_map[line[self.id]] = line[entrez_id]
        self.features = np.array(features,dtype=float)
        del features

    def run(self,n,source,url):
        for i in range(len(self.header_names)):
            indices = self._get_n_max(n,i)
            labels = yield [self.ids[idx] for idx in indices],self.header_names[i]

    def _get_n_max(self,n,i):
        arr = self.features[:,i]
        indices = arr.argsort()[-n:][::-1]
        return indices

        

