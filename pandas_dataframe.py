# DataFrame is the most frequently used data type for data science and artificial intelligence.
import pandas as pd

list = [12,34,56,32,87]
frame1 = pd.DataFrame(list, columns = ["First_DataFrame"])
print(frame1)
# outputs    First_DataFrame
#         0               12
#         1               34
#         2               56
#         3               32
#         4               87

import numpy as np

numpy_array = np.arange(1,10).reshape((3,3))
# returns ([[1,2,3],
#           [4,5,6],
#           [7,8,9]])

frame2 = pd.DataFrame(numpy_array, columns = ["var1", "var2", "var3"])
print(frame2)
# outputs    var1  var2  var3
#         0     1     2     3
#         1     4     5     6
#         2     7     8     9

print(frame2.columns) # outputs Index(['var1', 'var2', 'var3'], dtype='object')
frame2.columns = ("deg1", "deg2", "deg3") # now column names are updated

print(frame2.axes)
# outputs [RangeIndex(start=0, stop=3, step=1), Index(['deg1', 'deg2', 'deg3'], dtype='object')]

print(frame2.shape)
# outputs (3,3)

print(frame2.ndim)
# outputs 2

print(frame2.size)
# outputs 9

print(frame2.tail(1))
# outputs    deg1  deg2  deg3
#         2     7     8     9

import numpy as np
s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

dictionary = {"first": s1, "second": s2, "third": s3}
print(dictionary)
# outputs {'first': array([6, 2, 2, 0, 4]), 'second': array([5, 4, 1, 6, 0]), 'third': array([9, 6, 2, 4, 2])} // numbers are random

frame3 = pd.DataFrame(dictionary)
print(frame3)
# outputs first  second  third  // numbers are random
#      0      2       0      4
#      1      8       3      4
#      2      8       6      2
#      3      2       6      8
#      4      3       6      5

frame3.drop(0, axis = 0, inplace = True)
print(frame3)
# Without 'inplace = True' statement, code snippet above just deletes the 0th row.
# But with 'inplace = True' statement, it deletes the 0th row from the dataframe permanently.
# axis=0 means that the first parameter is the row number to be deleted, axis=1 means that it is column number to be deleted.

list2 = ["first", "third", "2nd"]
for i in frame3:
    print(i in list2)
# outputs True
#         False
#         True

frame3["fourth"] = frame3["first"] / frame3["second"] # fourth column is added to dataframe
print(frame3)
# outputs    first  second  third    fourth
#         1      8       2      8  4.000000
#         2      5       7      6  0.714286
#         3      0       2      6  0.000000
#         4      8       2      4  4.000000

# -------- observation and variable selection: loc & iloc ---------

print(frame2.loc[0:2])
# outputs    deg1  deg2  deg3
#         0     1     2     3
#         1     4     5     6
#         2     7     8     9

print(frame2.iloc[0:2])
# outputs    deg1  deg2  deg3
#         0     1     2     3
#         1     4     5     6

print(frame2.iloc[0,2])
# outputs 3

print(frame2.iloc[:2,:2])
# outputs    deg1  deg2
#         0     1     2
#         1     4     5

print(frame2.loc[0:2, "deg2"])
# outputs 0    2
#         1    5
#         2    8
#         Name: deg2, dtype: int32

# ----- conditional element operations -----
print(frame2[frame2.deg1 > 6])
# outputs    deg1  deg2  deg3
#         2     7     8     9

print(frame2[(frame2.deg1 > 0) & (frame2.deg3 < 5)])
# outputs    deg1  deg2  deg3
#         0     1     2     3

print(frame2[frame2.deg1 > 1][["deg1", "deg2"]])
# outputs    deg1  deg2
#         1     4     5
#         2     7     8

# ----- join operations -----
frame4 = frame2 + 100
print(pd.concat([frame2, frame4]))
# outputs    deg1  deg2  deg3
#         0     1     2     3
#         1     4     5     6
#         2     7     8     9
#         0   101   102   103
#         1   104   105   106
#         2   107   108   109

print(pd.concat([frame2, frame4], ignore_index=True))
# outputs    deg1  deg2  deg3
#         0     1     2     3
#         1     4     5     6
#         2     7     8     9
#         3   101   102   103
#         4   104   105   106
#         5   107   108   109