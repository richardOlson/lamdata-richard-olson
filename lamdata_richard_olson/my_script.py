

# lamdata-richard/my_script.py

import pandas as pd

from lamdata_richard_olson.my_mod import State,  gen_more_data 
#from my_mod import gen_more_data, State
#state = input("Enter a State and we will return the abbreviation  ")

#print(state_abbrev(state))

#df = pd.DataFrame({'X':[1,2,3], "Y": [51,52,63]})

#print(gen_more_data(df, num=2, row=None, cols='X', axis=1 ))

print(State.state_abbrev('ut'))

theState = State('NY')
print(f"\"{theState.name}\"")
print(theState.abrev)
print(State.state_abbrev("Utah"))
print(State.make_abbrev_dataframe(pd.DataFrame({"States":["Utah", "Alabama", "Arizona"]}),
 col="States", name="Abbreviation of States"))


print(gen_more_data(pd.DataFrame({"X": [1,2,3], "Y":[5,6,7], "Z":[8,9,10]}),num=5, 
row=[2,1] ))
print("\n\n\n")
print(gen_more_data(pd.DataFrame({'Y':["CAR", "Pig", "year"], "Howdy": [1,2,3]}), 
num=5, cols=["Y", 'Howdy'], axis=0 ))
print("\n")
print(gen_more_data(pd.DataFrame({'Y':["CAR", "Pig", "year"], "Howdy": [1,2,3]}), 
num=3, cols=['Y', "Howdy"], axis=1, names=['Y', 'Howdy'] ))