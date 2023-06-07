#!/usr/bin/env python3

import argparse
import os
import sys
import time
import shutil
from numpy import product
import pandas as pd 


def count(table_pfam_general : chr ,species_pfam : chr) -> chr:
    table_pfam = pd.read_csv(table_pfam_general, sep="\t", header=None)
    table_species_pfam = pd.read_csv(species_pfam, sep="\t", header=None)
    list_occurence_pfam=[]
    for pfam_total in range(0,table_pfam.shape[1]):
        pfam_name=table_pfam.iloc[0,pfam_total]
        column_pfam=table_species_pfam.loc[table_species_pfam[0]==pfam_name].index.values
        if len(column_pfam) == 0 :
            list_occurence_pfam.append("0")
        else :
            list_occurence_pfam.append(str(table_species_pfam.iloc[column_pfam[0],1]))
    print(len(list_occurence_pfam))
    return list_occurence_pfam


