

from lamdata_richard_olson.my_mod import State 
import pandas as pd
# building the functions that will be doing the testing.

def test_create_state():
    s = State("Ut")
    # asserting if the State now will
    # contain the name of the state and the abbrev
    assert(s.name == "Utah")
    assert(s.abrev == "UT")


def test_make_abbrev_dataframe():
    #make_abbrev_dataframe(data, col=None, name=None)
    df = pd.DataFrame({"Y":["Ut", "NV", "Arizona"],
         "Z":[1,2,3]})
    df = State.make_abbrev_dataframe(df,col="Y", name="Yes")
    assert("Yes" in list(df.columns))
    # doing another assert
    assert(df.loc[2, "Yes"] == "AZ")
    


