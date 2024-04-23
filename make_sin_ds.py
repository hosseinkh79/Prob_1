import math
import numpy as np
import pandas as pd

nums = np.arange(-10, 10, step=.1)
sins = np.sin(nums)

df = pd.DataFrame({
    'nums': nums,
    'sins': sins
})

df.to_csv('./df.csv')