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
        for i in range(header):
            line = f.readline().strip().split('\t')
        self.feature_map = {}
        for line in f:
            line = line.rstrip().split('\t')
            self.feature_map[line[self.id]] = np.array(line[self.start:self.end])
