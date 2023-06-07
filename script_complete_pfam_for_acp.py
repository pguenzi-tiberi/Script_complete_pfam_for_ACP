#!/usr/bin/env python3

import argparse
import os
import sys
import time
import shutil
import pandas as pd
from sympy import im 
#from lib import merging
from lib import traitement

def run() :
    parser = argparse.ArgumentParser(
        prog="complete",
        description="\n\n building table for ACP with PFAM",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=True,
    )

    mandatory_args = parser.add_argument_group("Mandatory arguments")

    # Mandatory arguments

    # Trinotate report
    
    mandatory_args.add_argument(
        "--table_pfam_to_completed",
        action="store",
        dest="table_pfam_general",
        help="",
        default="",
        required=True,
    )

    mandatory_args.add_argument(
        "--species_pfam",
        action="store",
        dest="species_pfam",
        help="",
        default="",
        required=True,
    )
    
    optional_args = parser.add_argument_group("Optional arguments")

    # Output
    optional_args.add_argument(
        "--output",
        action="store",
        dest="output",
        help="",
        default="results",
        required=False,
    )

    optional_args.add_argument(
        "--output_dir",
        "-o",
        action="store",
        dest="output_dir",
        help="",
        default="results",
        required=False,
    )

    args = parser.parse_args()

    try:
        os.mkdir(args.output_dir)
    except:
        print(
            f"\n Output directory {args.output_dir} can not be created, please erase it before launching the programm !"
        )
        sys.exit(1)

    actual_path = os.getcwd()
    os.chdir(args.output_dir)

    global_start = time.perf_counter()
    

    list_occurence=traitement.count(args.table_pfam_general,args.species_pfam)
    table_pfam = pd.read_csv(args.table_pfam_general, sep="\t", header=None)
    occurence="\t".join(list_occurence)
    table_occurence=pd.DataFrame([list_occurence])
    final_table=pd.concat([table_pfam,table_occurence])
    final_table.to_csv(path_or_buf="final_table.tsv", sep="\t", header=False)

    print(
        f"\n Total running time : {float(time.perf_counter() - global_start)} seconds"
    )
    
if __name__ == '__main__':
    run()