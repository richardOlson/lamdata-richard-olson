

# lamdata-richard/my_script.py

import pandas as pd

from lamdata_richard_olson.my_mod import state_abbrev, gen_more_data

#state = input("Enter a State and we will return the abbreviation  ")

#print(state_abbrev(state))

df = pd.DataFrame({'X':[1,2,3], "Y": [51,52,63]})

print(gen_more_data(df, num=2, row=None, cols='X', axis=1 ))