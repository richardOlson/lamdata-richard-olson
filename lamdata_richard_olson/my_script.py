

# lamdata-richard/my_script.py

import pandas as pd

from lamdata_richard_olson.my_mod import State 

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