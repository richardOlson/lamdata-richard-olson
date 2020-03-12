
# Area that will contain the functions 

# lamdata-richard-olson/my_mod.py

import pandas as pd
import numpy as np
from state_dict import theStates

def state_abbrev(state):
    '''
    This method will take in a state and return its
    abbreviation.  If the abbreviation is passed in it will 
    return the Full name of the state.

    state:      This is the state that will be either abbreviated or
                will be not abbreviated.
    returns:    Will return the opposite of that which is passed into the
                function
    '''
    # Making an upper case of the state
    state = state.upper()
    # creating the  return 
    
    ans = theStates.get(state)
    if ans == None:
        for theKey, theVal in  theStates.items():
            if state == theVal:
                return theKey
            
        return "That was not a state or territory!"
    return ans
        

# making the second utility function
# Will make something that will generate more data

def gen_more_data(df, num=1,   row=None, cols=None, axis=0,  ):
    '''
    This method will generate more data on a dataframe
    and then return the dataframe

    row:        default=None.  It you want to replicate a certain row in the dataframe, 
    then you put the row index in here. If you put in a list of rows then it
    will replicate the list of rows in the order they are
    found in the list. When None is passed in, then the row
    becomes as if you entered a row with all NAN in it.
    


    cols:       default=None.  If you want to replicate a certain column in 
    the dataframe, then you enter the column. If a list is entered
    the columns are added in the order in the list.  If None is used 
    then the all values in the column will be NAN.
    


    axis:       default==0, 0 means will use the index and will add rows.
    1 will cause columns to be added.

    
    
    df:         The dataFrame that you want the data appended to 



    num:        Default is 1. This is the number of times you want the rows specified to 
                be replicated.
    ''' 
    df = df.copy()

    the_rowShape, the_colShape = df.shape
    # This is the length of the row or colum being added
    t_len = 0
    # putting the name out so that I can use 
    # it in a global sense
    arr = None
    row_col = 0
    seriesList = []
    # setting to the defualt if
    # nothing is passed in.
    if num == None:
        num = 1
    
    if row == None and cols == None:

        if axis == 0:
            # This tells the number of 
            # columns each row will have
            t_len = the_colShape
            # getting the row
            row_col = row
            
            
        else:
            t_len = the_rowShape
            row_col = cols
            

        # This is building the empty np array to then add to the 
        if row_col == None:
            arr = np.empty(t_len, num)
            arr[:] = np.NAN
            # making the dataFrame
            newDf = pd.DataFrame(data=arr)
            seriesList.append(newDf)
            # assigning num to 1 to use later how 
            # many times to add this to the
            # dataframe
        

    # Not creating an empty dataframe
    elif axis == 0:
        
        if not isinstance(row, list ):
            # create a list
            row = [row]
       # builing the list of series that will be added to 
       # the dataframe 
        for j in range(num):
            for i in range(len(row)):
                a_row = df.iloc[row[i]]
                # this is to add the rows on one by one
                df.loc[len(df.index) ] = a_row
                #seriesList.append(a_row.to_frame())
        return df

    else:
        
        if not isinstance(cols, list):
            # making it a list
            cols = [cols]
        # building the list of series to be added
        for j in range(num):
            for i in range(len(cols)):
                a_col = df.loc[:, cols[i]]
                
                seriesList.append(a_col.to_frame())

        # builing the new dataframe and then returning it
        completList = [df] + seriesList
        
    df = pd.concat(objs=completList, axis=1, ignore_index=True, 
                   names=names )
    return df
           