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
        "--table_pfam_to_compled",
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
        "-o",
        action="store",
        dest="output",
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
    

    print(
        f"\n Total running time : {float(time.perf_counter() - global_start)} seconds"
    )

    
if __name__ == '__main__':
    run()