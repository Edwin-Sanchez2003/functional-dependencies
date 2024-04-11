"""
    Dataset Class | Functional Dependencies
    Edwin Sanchez
    
    This program allows you to automatically
    find functional dependencies in a given
    set of data. This is a bottom-up approach
    to database design.
"""

import pandas as pd

def main():
    pass


class Dataset(object):
    """
    This class defines the structure of
    the data to be used 
    """
    
    # initialize the dataset with values
    def __init__ (
        self, 
        column_names:list[str], 
        data:list[list[str]]
    ) -> None:
        self.__column_names = column_names
        self.__data = data
        
        
    def get_column_names (
        self
    ) -> list[str]:
        return self.__column_names
        
    
    def get_data (
        self
    )-> list[list[str]]:
        return self.__data
    
    
    column_names:list[str] = property(
        fget=get_data,
        doc="The rows & columns containing our data.")

    
    data:list[list[str]] = property(
        fget=get_data,
        doc="The rows & columns containing our data.")    
# end Dataset Class


if __name__ == "__main__":
    main()
