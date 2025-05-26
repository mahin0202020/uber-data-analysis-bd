# %%
import pandas as pd
import numpy as np
import  seaborn as sns
import matplotlib.pyplot as plt

# %%
import os

# %% [markdown]
# full dataset load use os function 

# %%
os.listdir(r"d:\eda project for bd")

# %%
p1=pd.read_csv("BD2024_uber-raw-data-janjune-15_sample.csv")

# %%
p1.head()

# %%
p1.shape

# %%
type(p1)

# %% [markdown]
# how can see  if datasets have same value or null  value 

# %%
p1.duplicated().sum()

# %%
p1.isnull().sum()

# %% [markdown]
# how can check datatypes  and change datatypes

# %%
p1.dtypes

# %%
type(p1['Date/Time'][0])

# %%
p1['Date/Time']=pd.to_datetime(p1['Date/Time'])

# %%
p1['Date/Time'].dtype

# %%
p1['Date/Time'][0]

# %%
type(p1['Date/Time'][0])

# %%
p1.dtypes

# %% [markdown]
# now how can see which month have max uber pickups in the new work city 

# %%
p1.head()

# %%
p1['month']= p1['Date/Time'].dt.month_name()

# %%
 
# Plot
monthly_counts.plot(kind='bar', figsize=(8,6), color='skyblue')
plt.xlabel("Month")
plt.ylabel("Number of Pickups")
plt.title("Number of Uber Pickups by  january Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
print(p1['Date/Time'].min())
print(p1['Date/Time'].max())


# %%
p1['weekday']= p1['Date/Time'].dt.day_name()
p1['day']= p1['Date/Time'].dt.day
p1['hour']= p1['Date/Time'].dt.hour
p1['minute']= p1['Date/Time'].dt.minute

# %%
p1.head(4)

# %%
from pandas import pivot


pivot= pd.crosstab(index= p1['month'],columns=p1['weekday'])

# %%
pivot

# %%
pivot.plot(kind='bar', figsize=(8,6))

# %% [markdown]
# 

# %% [markdown]
#  4. lets find out hourly rush in news work city on all days

# %%


 
 
# Step 3: Create a summary DataFrame (average count of pickups per hour per weekday)
summary = p1.groupby(['weekday', 'hour']).size().reset_index(name='size')

# Optional: Order weekdays
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
summary['weekday'] = pd.Categorical(summary['weekday'], categories=weekday_order, ordered=True)
summary = summary.sort_values(['weekday', 'hour'])

# Step 4: Plot
plt.figure(figsize=(8, 6))
sns.pointplot(x="hour", y="size", hue="weekday", data=summary)
plt.title("Average Pickup Size by Hour and Weekday")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Pickups")
plt.legend(title="Weekday")
plt.tight_layout()
plt.show()


# %%
p1.columns

# %%
os.listdir(r"d:\eda project for bd")

# %%
p1_foil= pd.read_csv(r'd:\eda project for bd\BD2024_Uber-Jan-Feb-FOIL.csv')

# %%
p1_foil

# %%
p1_foil.dtypes

# %%
type(p1_foil['Date/Time'][0])

# %%
p1_foil['Date/Time']=pd.to_datetime(p1_foil['Date/Time'])

# %%
p1_foil.dtypes

# %%
p1_foil['Lat'].value_counts()

# %% [markdown]
# suppose delete any files from datasets than how caan do

# %%
files=os.listdir(r"d:\eda project for bd")[-8:]

# %%
files

# %%
files.remove('BD2024_uber-raw-data-sep14.csv')

# %%
files

# %% [markdown]
#  

# %%
 

path = r"d:\eda project for bd"
files = os.listdir(path)  # list of filenames in the folder

final = pd.DataFrame()  # empty df to start with

for file in files:
    if file.endswith(".csv"):
       # optional: make sure it's a CSV file
        current_df = pd.read_csv(os.path.join(path, file))
        final = pd.concat([final, current_df], ignore_index=True)

 

# %%
final.shape

# %%
final.duplicated().sum()

# %%
final.head()

# %% [markdown]
# what locations of new york city we are getting rush

# %%
rush_uber= final.groupby(['Lat','Lon'], as_index= False).size()

# %%
import folium # for using map

# %%
import folium.map


basemap= folium.Map()

# %%
basemap

# %%
from folium.plugins import  HeatMap  

# %%
HeatMap(rush_uber).add_to(basemap)

# %%
basemap


