# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 07:53:55 2022
@author: Alast

Things to do:
    Work out how to parse compound sample names, e.g. dnhA_NEG_1
"""

# Import libraries to select data files (glob), read and process them (pandas) and plot them (matplotlib)
import glob
import pandas as pd
import matplotlib.pyplot as plt


# List all files with .arw extension (i.e. data files) so we can iteratively make dataframes from each file
files = glob.glob('*.arw')
for i in files:
    tempDf = pd.read_csv(i)
    print(tempDf)

#Construct column header list from first file
wave_raw = pd.read_csv(files[0], sep = '\t', skiprows=2, header=None, nrows=1)
wave = wave_raw.loc[:,1:]
wave_head = wave.values.tolist()
wave_head = wave_head[0]
wave_head.insert(0,"Time")

#Select timepoint to plot
#Time intervals:
#0
#0.01666667
#0.03333334
#0.05
#0.06666667
#0.08333334
#0.1
timepoint = 8
maxY = 0.1


#Read file, trim header, add header, set row labels, filter by timepoint

#Plot everything in one figure
for i in files:
    HPLC = pd.read_csv(i, sep = '\t', skiprows=4, header=None)
    HPLCfilt = HPLC.loc[:,:]
    HPLCfilt.columns = wave_head
    HPLCfilt = HPLCfilt.set_index(['Time'])
    HPLCrow = HPLCfilt.loc[(timepoint)]
    plt.title('Abs at T=' + str(timepoint))
    plt.ylabel('Abs')
    plt.xlabel('Wavelength')
    plt.grid(True)
    plt.ylim((0, maxY))
    plt.plot(HPLCrow)
plt.show()
    
#Plot separate figures
for i in files:
    HPLC = pd.read_csv(i, sep = '\t', skiprows=4, header=None)
    HPLCfilt = HPLC.loc[:,:]
    HPLCfilt.columns = wave_head
    HPLCfilt = HPLCfilt.set_index(['Time'])
    HPLCrow = HPLCfilt.loc[timepoint]
    plt.title('Abs for ' + i + 'at T=' + str(timepoint))
    plt.ylabel('Abs')
    plt.xlabel('Wavelength')
    plt.grid(True)
    plt.ylim((0, maxY))
    plt.plot(HPLCrow)
    plt.show()




    
"""
#Efficient loop
wave_raw = pd.read_csv(i, sep = '\t', skiprows=2, header=None, nrows=1)
wave = wave_raw.loc[:,1:]
wave_head = wave.values.tolist()
wave_head = wave_head[0]
wave_head.insert(0,"Time")


for i in files:
    HPLC = pd.read_csv(i, sep = '\t', skiprows=4, header=None)
    HPLCfilt = HPLC.loc[:,:]
    HPLCfilt.columns = wave_head
    HPLCfilt = HPLCfilt.set_index(['Time'])

    HPLCrow = HPLCfilt.iloc[8]
    HPLCrow.plot()
"""
    
    
"""
#Single run
wave_raw = pd.read_csv("raw32552.arw", sep = '\t', skiprows=2, header=None, nrows=1)
wave = wave_raw.loc[:,1:]
wave_head = wave.values.tolist()
wave_head = wave_head[0]
wave_head.insert(0,"Time")

HPLC = pd.read_csv("raw32552.arw", sep = '\t', skiprows=4, header=None)
HPLCfilt = HPLC.loc[:,:]
HPLCfilt.columns = wave_head
HPLCfilt = HPLCfilt.set_index(['Time'])

HPLCrow = HPLCfilt.iloc[0]
HPLCrow.plot()
"""    
    
    
    
"""
#Inefficient loop
for i in files:
    wave_raw = pd.read_csv(i, sep = '\t', skiprows=2, header=None, nrows=1)
    wave = wave_raw.loc[:,1:]
    wave_head = wave.values.tolist()
    wave_head = wave_head[0]
    wave_head.insert(0,"Time")

    HPLC = pd.read_csv(i, sep = '\t', skiprows=4, header=None)
    HPLCfilt = HPLC.loc[:,:]
    HPLCfilt.columns = wave_head
    HPLCfilt = HPLCfilt.set_index(['Time'])

    HPLCrow = HPLCfilt.iloc[0]
    HPLCrow.plot()
"""
