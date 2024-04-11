"""
    Main Program | Functional Dependencies
    Edwin Sanchez
    
    This program allows you to automatically
    find functional dependencies in a given
    set of data. This is a bottom-up approach
    to database design.
"""

import os
import csv
import json
import multiprocessing

import numpy as np

import Dataset

import argparse

# make parser object
parser = argparse.ArgumentParser(
prog='Functional Dependencies',
description="""This program allows you to automatically
find functional dependencies in a given
set of data. This is a bottom-up approach
to database design."""
) # end ArgumentParser construction

# arguments to be passed in by the user via the command line/terminal
parser.add_argument('-f', '--data_file_path', type=str, 
    help="The path to the file containing the data to find functional dependencies for. Accepts file types: csv")
parser.add_argument('-o', '--output_dir', default="./output/", type=str, 
    help="The path to where the functional dependency analysis information will be written to. Defaults to: './output/'")
parser.add_argument('-mcks', '--max_composite_key_size', default=1, type=int, 
    help="The maximum number of composite keys to try. If you expect that your data may require more than a single attribute to use for a table's primary key, then increase this value. NOTE: This will exponentially increase runtime (which may or may not be feasible with your data.)")
parser.add_argument('-mpc', '--max_process_count', default=os.cpu_count(), type=int,
    help="The number of processes that should be used to determine the results. Because python multithreading is throttled by the GIL, we use multiprocessing.")
parser.add_argument('-gpu', '--use_gpu', default=True, type=argparse.BooleanOptionalAction, 
    help="Whether or not to use gpu to speed up processing.")

# parse the arguments given
args = parser.parse_args()

# Parameters
DATA_FILE_PATH:str = str(args.data_file_path)
CPU_COUNT:int = int(args.mpc)

# error checking for CPU_COUNT
# if OS returns 'None' for cpu_count,
# default to a single process.
if CPU_COUNT == None:
    CPU_COUNT:int = 1


def main():
    # TODO: Multi-Process the dependency-checking? This would allow for
    # faster processing of the data for larger datasets. Allow for the program
    # to pick up where it left off if interrupted.

    # load the data into a dataset object
    
    # evaluate its functional dependencies - store
    # in a json file
    
    # save dependencies into a json file
    
    # NOTE: Keep track of columns that don't end up having anything that
    # they are dependent on. It may be that these are dependent on a
    # composite key.
        
    pass


def is_functionally_dependent (
    attr_1_values:list[str],
    attr_2_values:list[str]
)-> bool:
    """
    This function determines whether or not
    the potentially dependent category is 
    actually dependent on the given category.
    
    Does this by checking finding values in 
    the attr_1_values list for exact matching values.
    If there are, it checks the attr_2_values at the same
    row to see if they also match each other. If they do,
    then attr_2 is likely to be functionally dependent on 
    attr_1. This check is done for all rows with matching 
    attr_1 values.
    
    It is important to note that this is a 'likelihood', not
    a guarantee. The more data obtained from the people you
    are designing the Database for, the more likely this program
    will yield promising results. Not all possible dependencies
    are likely or realistic - you must analyze the dependencies
    to find the most likely candidates for relations in the database.
    
    Inputs:
    --------
    `attr_1_values : list[str]`
        A list of values corresponding to the attribute that
        we are checking to see of the other attribute is dependent
        on: {attr_1} -> {attr_2} (read as 'attribute 1 determines attribute 2').
        
    `attr_2_values : list[str]`
        A list of values corresponding to the attribute that
        we are checking to see if it is dependent on the other
        attribute: {attr_1} -> {attr_2} (read as 'attribute 2 is determined by attribute 1').
    """
    
    # enforce that list sizes are the same
    # if not, there may be an issue. If
    # sizes are not the same, some padding 
    # may be needed.
    assert len(attr_1_values) == len(attr_2_values)
    
    # first, determine the indices of every row with matching values.
    
    
        
# end is_functionally_dependent

def find_matching_indices (
    attr_values:np.ndarray
) -> np.ndarray:
    """
    Finds the indices with matching values
    for a specific attribute (a column in an
    SQL database).
    
    Inputs:
    --------
    attr_values : 
    """
    
# end find_matching_indices


def load_data_csv (
    file_path:str
) -> Dataset:
    """
    Loads the data from a csv file into
    a data structure that can be used to
    determine functional dependencies.
    
    The output format is uniform for all
    input types. If there isn't a supported
    file type, write a new load function
    for that datatype.
    
    Inputs:
    ---------
    * `file_path : str`
        The path to the file containing the data to find functional dependencies for. Accepts file types: csv
    
    Outputs:
    --------
    * `dataset_object : Dataset`
        A data structure containing the data of the loaded csv file, in a structure that makes the functional
        dependency evaluation simple.
    """
    
    
    
# end load_data_csv


if __name__ == "__main__":
    main()
