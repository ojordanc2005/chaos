import numpy as np

# here is where i'll have a large storage of automata rules that i can access easily

# i'll use dictionaries
def rule_90():
    rule_90 = {
        "(0,0,0)": 0,
        "(1,0,0)": 1,
        "(0,1,0)": 0,
        "(0,0,1)": 1,
        "(1,1,0)": 1,
        "(0,1,1)": 1,
        "(1,0,1)": 0,
        "(1,1,1)": 0
    }
    return rule_90

