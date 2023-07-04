# Pandas is not an alternative to NumPy, it is a library that uses NumPy's features and extends them.
import pandas as pd

serie1 = pd.Series([10,20,40,50]) # it also keeps the indexes of elements
print(serie1)
# outputs 0    10
#         1    20
#         2    40
#         3    50
#         dtype: int64

print(serie1.axes)
# outputs [RangeIndex(start=0, stop=4, step=1)]

print(serie1.dtype)
# outputs int64

print(serie1.size)
# outputs 4

print(serie1.ndim)
# outputs 1 (number of dimensions)

print(serie1.values)
# outputs [10 20 40 50]

# print(serie1.head(x)) outputs the first 'x' elements of serie1.
# print(serie1.tail(x)) outputs the last 'x' elements of serie1.

serie2 = pd.Series([121,321,1,435,23], index = [12,8,76,45,87])
print(serie2)  # indexes can also be strings
# outputs 12    121
#         8     321
#         76      1
#         45    435
#         87     23
#         dtype: int64

# serie2[76] = 1
# serie2[76:87] returns [1,435,23]

dictionary = {"reg":10, "log":11, "cart": 12}
serie3 = pd.Series(dictionary)
print(serie3)
# outputs reg     10
#         log     11
#         cart    12
#         dtype: int64

print(pd.concat([serie3, serie3]))
# outputs reg     10
#         log     11
#         cart    12
#         reg     10
#         log     11
#         cart    12
#         dtype: int64

import numpy as np
a = np.array([1,32,86,23,96])
serie4 = pd.Series(a)
print(serie4)
# outputs 0     1
#         1    32
#         2    86
#         3    23
#         4    96
#         dtype: int32

print(serie3.index) # outputs Index(['reg', 'log', 'cart'], dtype='object')
print(list(serie3.items())) # outputs [('reg', 10), ('log', 11), ('cart', 12)]

print("reg" in serie3) # outputs True
print(11 in serie3) # outputs False

print(serie3[["reg", "cart"]])
# outputs reg     10
#         cart    12
#         dtype: int64

# serie3["reg"] = 130 --> This line updates the value of key 'reg' to 130.