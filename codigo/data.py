import pandas as pd
import numpy as np
i = 0
err = 0
try: 
    # print(df2010)
    df2010 = pd.read_excel (r'../datos-excel/Femicidios 2010 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2011)
    df2011 = pd.read_excel (r'../datos-excel/Femicidios 2011 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2012)
    df2012 = pd.read_excel (r'../datos-excel/Femicidios 2012 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2013)
    df2013 = pd.read_excel (r'../datos-excel/Femicidios 2013 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2014)
    df2014 = pd.read_excel (r'../datos-excel/Femicidios 2014 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2015)
    df2015 = pd.read_excel (r'../datos-excel/Femicidios 2015 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2016)
    df2016 = pd.read_excel (r'../datos-excel/Femicidios 2016 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2017)
    df2017 = pd.read_excel (r'../datos-excel/Femicidios 2017 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2018)
    df2018 = pd.read_excel (r'../datos-excel/Femicidios 2018 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2019)
    df2019 = pd.read_excel (r'../datos-excel/Femicidios 2019 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2020)
    df2020 = pd.read_excel (r'../datos-excel/Femicidios 2020 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2021)
    df2021 = pd.read_excel (r'../datos-excel/Femicidios 2021 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1

try: 
    # print(df2022)
    df2022 = pd.read_excel (r'../datos-excel/Femicidios 2022 - Red Chilena contra la Violencia hacia las Mujeres.xlsx')
except FileNotFoundError:
    pass
    err = err+1
else:
    i = i+1
print("###################################")
print("###################################")
print("cantidad de lecturas correctas: ",i)
print("cantidad de lecturas erroneas: ",err)
print("###################################")
print("###################################")
raw2010 = df2010.iloc[:,:8]
raw2011 = df2011.iloc[:,:8]
raw2012 = df2012.iloc[:,:8]
raw2013 = df2013.iloc[:,:8]
raw2014 = df2014.iloc[:,:8]
raw2015 = df2015.iloc[:,:8]
raw2016 = df2016.iloc[:,:8]
raw2017 = df2017.iloc[:,:8]
raw2018 = df2018.iloc[:,:8]
raw2019 = df2019.iloc[:,:8]
raw2020 = df2020.iloc[:,:8]
raw2021 = df2021.iloc[:,:8]
raw2022 = df2022.iloc[:,:8]
print("###################################")
print("###################################")
print (raw2010)
print("###################################")
print (raw2011)
print("###################################")
print (raw2012)
print("###################################")
print (raw2013)
print("###################################")
print (raw2014)
print("###################################")
print (raw2015)
print("###################################")
print (raw2016)
print("###################################")
print (raw2017)
print("###################################")
print (raw2018)
print("###################################")
print (raw2019)
print("###################################")
print (raw2020)
print("###################################")
print (raw2021)
print("###################################")
print (raw2022)
print("###################################")
