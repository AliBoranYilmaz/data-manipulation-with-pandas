import seaborn as sns # library of data sets
import pandas as pd
import numpy as np

frame1 = sns.load_dataset("planets")
print(frame1.shape)
# outputs (1035,6) // 1035 rows, 6 columns

print(frame1["mass"].mean())
# outputs 2.6381605847953216

print(frame1["mass"].count())
# outputs 513

print(frame1["mass"].min())
# outputs 0.0036

print(frame1["mass"].max())
# outputs 25.0

print(frame1["mass"].std()) # standard deviation
# outputs 3.8186166509616046

print(frame1["mass"].var()) # variance
# outputs 14.58183312700122

print(frame1.describe())
# outputs        number  orbital_period        mass     distance         year
#    count  1035.000000      992.000000  513.000000   808.000000  1035.000000
#    mean      1.785507     2002.917596    2.638161   264.069282  2009.070531
#    std       1.240976    26014.728304    3.818617   733.116493     3.972567
#    min       1.000000        0.090706    0.003600     1.350000  1989.000000
#    25%       1.000000        5.442540    0.229000    32.560000  2007.000000
#    50%       1.000000       39.979500    1.260000    55.250000  2010.000000
#    75%       2.000000      526.005000    3.040000   178.500000  2012.000000
#    max       7.000000   730000.000000   25.000000  8500.000000  2014.000000

print(frame1.describe().T) # transposed
# outputs                  count         mean           std          min         25%        50%       75%       max
#         number          1035.0     1.785507      1.240976     1.000000     1.00000     1.0000     2.000       7.0
#         orbital_period   992.0  2002.917596  26014.728304     0.090706     5.44254    39.9795   526.005  730000.0
#         mass             513.0     2.638161      3.818617     0.003600     0.22900     1.2600     3.040      25.0
#         distance         808.0   264.069282    733.116493     1.350000    32.56000    55.2500   178.500    8500.0
#         year            1035.0  2009.070531      3.972567  1989.000000  2007.00000  2010.0000  2012.000    2014.0

frame2 = pd.DataFrame({"groups": ["A", "B", "C", "A", "B", "C"], "data": [10,11,52,23,43,55]}, columns=["groups", "data"])
print(frame2)
# outputs   groups  data
#         0      A    10
#         1      B    11
#         2      C    52
#         3      A    23
#         4      B    43
#         5      C    55

print(frame2.groupby("groups").mean())
# outputs         data
#         groups
#         A       16.5
#         B       27.0
#         C       53.5

print(frame2.groupby("groups").sum())
# outputs         data
#         groups
#         A         33
#         B         54
#         C        107

print(frame1.groupby("method")["orbital_period"].mean())
# outputs method
#         Astrometry                          631.180000
#         Eclipse Timing Variations          4751.644444
#         Imaging                          118247.737500
#         Microlensing                       3153.571429
#         Orbital Brightness Modulation         0.709307
#         Pulsar Timing                      7343.021201
#         Pulsation Timing Variations        1170.000000
#         Radial Velocity                     823.354680
#         Transit                              21.102073
#         Transit Timing Variations            79.783500
#         Name: orbital_period, dtype: float64

frame3 = pd.DataFrame({"groups": ["A", "B", "C", "A", "B", "C"],
                       "var1": [10,23,33,22,11,99],
                       "var2": [100,253,333,262,111,969]},
                       columns=["groups", "var1", "var2"])

print(frame3.groupby("groups").aggregate(["min", np.median, "max"]))
# outputs    var1            var2
#            min median max  min median  max
#    groups
#    A        10   16.0  22  100  181.0  262
#    B        11   17.0  23  111  182.0  253
#    C        33   66.0  99  333  651.0  969

print(frame3.groupby("groups").aggregate({"var1": ["min", "max"], "var2": np.mean}))
# outputs        var1      var2
#                min max   mean
#        groups
#        A        10  22  181.0
#        B        11  23  182.0
#        C        33  99  651.0

def filter_func(x):
    return x["var1"].std() > 9

print(frame3.groupby("groups").std())
# outputs              var1        var2
#         groups
#         A        8.485281  114.551299
#         B        8.485281  100.409163
#         C       46.669048  449.719913

print(frame3.groupby("groups").filter(filter_func))
# outputs   groups  var1  var2
#         2      C    33   333
#         5      C    99   969

frame3_a = frame3.iloc[:, 1:3]
print(frame3_a.transform(lambda x: x - (x.mean())))
# outputs    var1   var2
#0          -23.0 -238.0
#1          -10.0  -85.0
#2            0.0   -5.0
#3          -11.0  -76.0
#4          -22.0 -227.0
#5           66.0  631.0

print(frame3_a.apply(np.sqrt))
# outputs        var1       var2
#         0  3.162278  10.000000
#         1  4.795832  15.905974
#         2  5.744563  18.248288
#         3  4.690416  16.186414
#         4  3.316625  10.535654
#         5  9.949874  31.128765

titanic = sns.load_dataset("titanic")
print(titanic.groupby("sex")["survived"].mean())
# outputs sex
#         female    0.742038
#         male      0.188908
#         Name: survived, dtype: float64

print(titanic.groupby(["sex", "class"])[["survived"]].aggregate("mean").unstack())
# outputs         survived
#         class      First    Second     Third
#         sex
#         female  0.968085  0.921053  0.500000
#         male    0.368852  0.157407  0.135447

print(titanic.pivot_table("survived", index="sex", columns="class"))
# outputs class      First    Second     Third
#         sex
#         female  0.968085  0.921053  0.500000
#         male    0.368852  0.157407  0.135447