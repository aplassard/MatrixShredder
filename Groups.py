import numpypy
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
            if i + 1 == header_name:
                self.header_names = line[self.start:self.end]
        self.ids = []
        features = []
        for line in f:


