# lamdata-richard-olson

## Instalation
'''


    --- before version 1.021 are deprecated and no longer function --- 

    ---- use the following to make it work --- 

    pip install -i https://test.pypi.org/simple/ lambdata-richard-olson==1.0.21

   

'''

## Usage
'''
    State class used to get the abrev and full name of a state.  Will hold
    both as attributes.

    A static method in State called state_abbrev() can used to return
    the full name of a state if the abbreviation is passed in. 
    The same method will return the abbreviation when the full name of the 
    state is passed in to the method.
    
    
    make_abbrev_dataframe(data, col=None, name=None):
            This static method will create a new column on the dataframe that contains either the full name or the abbreviation, depending on which one was orginally found in the dataframe passed in to the method.  
    

    gen_more_data(df, num=1,   row=None, cols=None, axis=None, names=None ):
            This funcition is used to generate more rows or columns of a              dataframe.  Will  either generate copies of specified rows or columns or can
            also add row and columns with NAN added in.



    ##Dependancies:
    * pandas
    * numpy


    ##License
    MIT
'''
