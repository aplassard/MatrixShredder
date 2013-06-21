import argparse
try:
    import numpypy
except:
    pass
import numpy as np
from Groups import Groups
from Shred import Shred

def parse_args():
    parser = argparse.ArgumentParser(description='Lets Shred Some Matrices')
    parser.add_argument("--groups-input",type=str,help="Input File For Groups",required=True)
    parser.add_argument("--shred-input",type=str,help="Input File For Shredding Against",required=True)
    parser.add_argument("--groups-header-count",type=int,help="Number of header line in the groups file",default = 1,required=False)
    parser.add_argument("--shred-header-count",type=int,help="Number of header line in the shred file",default = 1,required=False)
    parser.add_argument("--groups-header-names",type=int,help="The number of the header line in the groups file, must be <= --groups-header-count",default = 1,required=False)
    parser.add_argument("--groups-id-column",type=int,help="The column of the ID that uniquely maps rows in the groups file to rows in the shred file, 1-based",default=1,required=False)
    parser.add_argument("--shred-id-column",type=int,help="The column of the ID that uniquely maps rows in the shred file to rows in the groups file, 1-based",default=1,required=False)
    parser.add_argument("--groups-entrez-column",type=int,help="The column containing the entrez IDs for the rows in the groups file, 1-based (default: --group-id-column)",required=False,default=None)
    parser.add_argument("--groups-feature-column",type=int,help="The column containing the first feature for the rows in the groups file, 1-based",required=True)
    parser.add_argument("--groups-feature-end",type=int,help="The column containing the last feature for the rows in the groups file, 1-based",required=False,default=-1)
    parser.add_argument("--output",type=str,help="Output File",required=True)
    parser.add_argument("--source",type=str,help="Source for ToppGene Output",required=True)
    parser.add_argument("--url",type=str,help="URL for ToppGene Output",required=True)
    parser.add_argument("--counts",type=str,help="Counts for K-Meansing, comma separated list",required=True)
    args = parser.parse_args()
    args.groups_id_column -= 1
    args.shred_id_column -= 1
    if not args.groups_entrez_column: args.groups_entrez_column = args.groups_id_column
    args.groups_feature_column -= 1
    args.counts = [int(a) for a in args.counts.split(",")]
    return args

def main():
    args = parse_args()
    groups = Groups(args.groups_input,args.groups_header_count,args.groups_id_column,args.groups_header_names,args.groups_feature_column,args.groups_feature_end)
    shred = Shred(args.groups_input,args.groups_header_count,args.groups_id_column,args.groups_feature_column,args.groups_feature_end)
    for count in args.counts:
        for group in groups.run(count):
            mat = shreds.get_marix(group)

def target(*args):
    main,None


if __name__=='__main__':
    main()

