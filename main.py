import argparse
import numpypy
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description='Lets Shred Some Matrices')
    parser.add_argument("--groups-input",type=str,help="Input File For Groups",required=True)
    parser.add_argument("--shred-input",type=str,help="Input File For Shredding Against",required=True)
    parser.add_argument("--groups-header-count",type=int,help="Number of header line in the groups file",default = 1,required=False)
    parser.add_argument("--shred-header-count",type=int,help="Number of header line in the shred file",default = 1,required=False)
    parser.add_argument("--groups-column-names",type=int,help="The number of the header line in the groups file, must be <= --groups-header-count",default = 1,required=False)
    parser.add_argument("--groups-id-column",type=int,help="The column of the ID that uniquely maps rows in the groups file to rows in the shred file, 1-based",default=1,required=False)
    parser.add_argument("--shred-id-column",type=int,help="The column of the ID that uniquely maps rows in the shred file to rows in the groups file, 1-based",default=1,required=False)
    parser.add_argument("--groups-entrez-column",type=int,help="The column containing the entrez IDs for the rows in the groups file, 1-based (default: --group-id-column)",required=False,default=None)
    parser.add_argument("--output",type=str,help="Output File",required=True)
    parser.add_argument("--source",type=str,help="Source for ToppGene Output",required=True)
    parser.add_argument("--url",type=str,help="URL for ToppGene Output",required=True)
    args = parser.parse_args()
    if not args.groups_entrez_column: args.groups_entrez_column = args.groups_id_column
    return args

def main():
    args = parse_args()
    print args

def target(*args):
    main,None


if __name__=='__main__':
    main()

