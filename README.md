# lamdata-richard-olson

## Instalation
'''sh


    --- before version 1.021 are deprecated and no longer function --- 

    ---- use the following to make it work --- 

    pip install -i https://test.pypi.org/simple/ lambdata-richard-olson==1.0.21

   

'''

## Usage
'''
    Has a function, state_abbrev() to return the full name of a state if 
    the abbreviation is given. Or will return the abbreviation if the full 
    name of the state is given.
    
    Can also use a static method from the State class to pass in a dataframe which has either 
    a column of the states or the states abbreviations and the function will cause another
    column to be added on that has the other(the abbreviation or the  state's full name)
    

    gen_more_data() :   Used to generate more rows or columns of a dataframe
                        Will  either generate copies of specified rows or columns or can 
                        also add row and columns with NAN added in.

'''
