
# Area that will contain the functions 

# lamdata-richard-olson/my_mod.py

import pandas as pd
import numpy as np
from lamdata_richard_olson.state_dict import theStates
# This commented import was used to debug
#from state_dict import theStates
class State():

   

    def __init__(self, state):
        
        self.name = self.__get_state(state)
        self.abrev = self.__get_abrev()


    # Inner method to set the attribute self.abrev
    def __get_abrev(self):
        theName = self.name
        return State.state_abbrev(theName)

    # Will return just the full state name
    # if the abbreviation is passed in.
    def __get_state(self, state):
        state = state.upper()
        ans = theStates.get(state)
        if ans == None:
            for k, v in theStates.items():
                if state == v:
                    return k
        return state
    
    @staticmethod
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
        # Making an upper case of the state abbrev
        if len(state) <= 2:
            state = state.upper()
        else:
            state = state.lower()
            # separating by spaces
            splits = state.split()
            state = ""
            for i in range(len(splits)):
                s = splits[i].capitalize()
                if state == "":
                    state += s
                else:
                    state += " " + s
            
        # getting the abbreviation
        ans = theStates.get(state)
        if ans == None:
            for theKey, theVal in  theStates.items():
                if state == theVal:
                    return theKey
                
            return "That was not a state or territory!"
        return ans

    # Building a function that will make tha dataFrame
    # for the dataFrame that is passed in
    @staticmethod
    def make_abbrev_dataframe(data, col=None, name=None):
        """This method will return a dataframe that has 
        another column to added to the dataframe. If the dataframe 
        has a column of abbreviations then a new column of State full names
        is added, or vice a versa.  If the data that is passed in 
        doesn't contain states or abbreviations then the new column 
        build will contain NAN.

        Data:   A series or a dataframe column is passed in

        col:    If a dataframe is passed in then the col use to map 
        against will be put here.

        name:   The name of the column to be added to the dataframe or 
        the data. If none is passed in then name will be "Abbrev_map"

        Returns:  A new dataFrame is returned.
        """
        data = data.copy()
        if name == None:
            name = "Abbrev_map"

        if(isinstance(data, pd.DataFrame)):
            assert(col != None), "Need to have a column selected!"
            theData = data[col] 
        else:
            theData = data   
        colList = []

        for i in range(len(theData)):
            ans = State.state_abbrev(theData[i])
            if ans == "That was not a state or territory!":
                ans = np.nan
            colList.append(ans)
        data = pd.DataFrame(data)
        data[name] = colList
        return data
        

        
        
            

# making the second utility function
# Will make something that will generate more data


def gen_more_data(df, num=1,   row=None, cols=None, axis=None, names=None ):
    '''
    This method will generate more data on a dataframe
    and then return the dataframe

    row :   default=None.  It you want to replicate a certain row 
    in the dataframe, then you put the row index in here. 
    If you put in a list of rows then it will replicate the list of
    rows in the order they are found in the list. When None is 
    passed in, then the row becomes as if you entered
    a row with all NAN in it.
    


    cols :   default=None.  If you want to replicate a certain column in 
    the dataframe, then you enter the column. If a list is entered
    the columns are added in the order in the list.  If None is used 
    then the all values in the column will be NAN.
    


    axis :   default==None, 0 means will use the index and will add rows.
    1 will cause columns to be added. If the row parameter is used, it will 
    be infered that the axis is 0.  When cols is used it is infered to be that
    you are using the axis of 1.  When neither row or col is used, then axis must
    be used

    
    
    df :   The dataFrame that you want the data appended to 



    num :   Default is 1. This is the number of times you want the rows specified to 
    be replicated.

    names:   This can be passed in when you want to name the columns that 
    being appended to the dataframe.  You can pass in a list or a single name.
    This is only used when you are generating more columns. Default is None.

    returns :    Will return the dataframe with the data added to it
    ''' 
    df = df.copy()

    the_rowShape, the_colShape = df.shape
    # This is the length of the row or colum being added
    row_len = 0
    col_len = 0
    # putting the name out so that I can use 
    # it in a global sense
    arr = None
    
    seriesList = []
    # setting to the defualt if
    # nothing is passed in.
    if num == None:
        num = 1
    
    
        
    if row == None and cols == None:
        assert(axis != None), "You must choose the axis when no cols or rows are chosen"
        if axis == 0:
            # This tells the number of 
            # columns each row will have
            row_len =  num
            col_len = the_colShape
                       
            
        else:
            row_len = the_rowShape
            col_len = num
            

        # This is building the empty np array to then add to the 
        arr = np.empty((row_len, col_len))
        arr[:] = np.NAN
        # making the dataFrame
        newDf = pd.DataFrame(data=arr, 
        columns=df.columns.to_list() if axis == 0 else None )
        # Now want to add to the existing dataframe
        return pd.concat([df , newDf],axis=axis, ignore_index=(axis == 0),  )
        
        
    # Assuring setting of axis when the
    # col or row is set. Axis will determine 
    # where to add the extra data
    if row != None:
        axis = 0
    elif cols != None:
        axis = 1

    # Not creating an empty dataframe
    if axis == 0:
        
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
        

        # making the names be same len as the num
        
        if names != None:

            if not isinstance(names, list):
                names = [names]
            # Putting the numbers in the name list
            #names = [str(i) for i in range(len(cols))]

            if len(cols) != len(names):
                # Building the names list if has 
                # something in it.
                theNames = []
                while len(theNames) < len(cols):
                    for i in range(len(names)):
                        theNames.append(names[i])
                        if len(theNames) == len(cols):
                            break
                names = theNames

        # building the list of series to be added
        for k in range(num):
            for i in range(len(cols)):
                a_col = df.loc[:, cols[i]]

                if names == None:
                    seriesList.append(a_col.to_frame())
                else:
                    df[names[i] + str("_") +str(k)] = a_col.to_list()
                    

        if names == None:
            completeList = [df] + seriesList
            df = pd.concat(completeList, axis=axis)

        return df

        # builing the new dataframe and then returning it
       # completList = [df] + seriesList
        
    #df = pd.concat(objs=completList, axis=1, ignore_index=True, 
           # names=name

         #)
    #return df
           
if __name__ == "__main__":
   # State.make_abbrev_dataframe(pd.DataFrame({"States":["Utah", "Alabama", "Arizona"]}), col="States")

    #gen_more_data(pd.DataFrame({'Y':["CAR", "Pig", "year"], "Howdy": [1,2,3]}), num=5, cols=None, axis=1 )
    #gen_more_data(pd.DataFrame({'Y':["CAR", "Pig", "year"], "Howdy": [1,2,3]}), 
        #num=5, cols=None, axis=0 )

    print(gen_more_data(pd.DataFrame({'Y':["CAR", "Pig", "year"], "Howdy": [1,2,3]}), 
        num=3, cols=['Y', "Howdy"], axis=1, names=["joe", 'jared', 'Frank'] ))