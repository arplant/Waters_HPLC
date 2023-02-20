# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 07:53:55 2022
@author: Alast

Things to do:
    Read files listed by 'files'; decide either to build a 3D dataframe or to make a new frame for each
    Work out how to parse compound sample names, e.g. dnhA_NEG_1

"""

# Import libraries to select data files (glob), read and process them (pandas) and plot them (matplotlib)
import glob
import pandas as pd
import matplotlib.pyplot as plt


# List all files with .arw extension (i.e. data files) so we can iteratively make dataframes from each file
# Maybe create dictionary to include data passed from sample name plus associated dataframe
files = glob.glob('HPLC_data/*.arw')
for i in files:
    tempDf = pd.read_csv(i)
    print(tempDf)

wave_raw = pd.read_csv("HPLC_data/raw1803.arw", sep = '\t', skiprows=2, header=None, nrows=1)
wave = wave_raw.loc[:,1:]
wave_head = wave.values.tolist()
wave_head = wave_head[0]
wave_head.insert(0,"Time")

HPLC = pd.read_csv("HPLC_data/raw1803.arw", sep = '\t', skiprows=4, header=None)
HPLCfilt = HPLC.loc[:,:]
HPLCfilt.columns = wave_head

#HPLCfiltplot = plt.plot(HPLCfilt[300.555])
HPLCfilt.plot(x = "Time", y = 300.555)


# Plot specific wavelength
plt.figure(figsize = (10,5))
plt.plot(HPLC['Time'],HPLC['0'], linewidth = 1.5)
plt.axis([0,40,0,100])
plt.xlabel('Time (min)')
plt.ylabel('Abs')
plt.show()

# Plot sublpots of specific wavelengths
plt.figure(figsize = (10,5))
plt.subplot(211)
plt.plot(HPLC['Time'],HPLC['0'], linewidth = 1.5)
plt.plot(HPLC['Time'],HPLC['100'], linewidth = 2.0)
plt.axis([0,15,0,200])
plt.xlabel('Time (min)')
plt.ylabel('Abs')
plt.show()

"""
# import module
import pandas as pd
 
# assign dataset names
list_of_names = ['crime','username']
 
# create empty list
dataframes_list = []
 
# append datasets into the list
for i in range(len(list_of_names)):
    temp_df = pd.read_csv("./csv/"+list_of_names[i]+".csv")
    dataframes_list.append(temp_df)
 
 """