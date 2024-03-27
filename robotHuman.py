
import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = pd.Categorical(data['whoAmI'])
unique_categories = categories.categories
one_hot_matrix = pd.DataFrame(columns=unique_categories, data=0, index=data.index)

for i, cat in enumerate(categories):
    one_hot_matrix.loc[i, cat] = 1

result_df = pd.concat([data, one_hot_matrix], axis=1)

print(result_df.head())