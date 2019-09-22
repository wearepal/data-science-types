import pandas as pd

a: pd.DataFrame = pd.DataFrame([[1, 2, 3], [1, 2, 3]], columns=['a', 'b', 'c'])
b: pd.Series = a['a']
