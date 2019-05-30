from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


lahead=3
to_drop=2
data_input = np.random.uniform(-1 * 1, +1 * 1, 15)
data_input = pd.DataFrame(data_input)

expected_output = data_input.rolling(window=10, center=False).mean()
if lahead > 1:
    data_input = np.repeat(data_input.values, repeats=lahead, axis=1)
    data_input = pd.DataFrame(data_input)
    for i, c in enumerate(data_input.columns):
        data_input[c] = data_input[c].shift(i)

expected_output = expected_output[to_drop:]
data_input = data_input[to_drop:]

print(data_input)
print(expected_output)