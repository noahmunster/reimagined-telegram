#!/usr/bin/env python
# coding: utf-8

# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <b> Reviewer's comment</b>
#     
# Hello, my name is Sveta Nosova and I am going to review this project. 
# 
# Before we start, I want to pay your attention to the color marking:
#     
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# Great solutions and ideas that can and should be used in the future are in green comments.   
# </div>    
#     
#     
# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
# 
# Yellow color indicates what should be optimized. This is not necessary, but it will be great if you make changes to this project.
# </div>      
#     
#     
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
# 
# Issues that need to be corrected to get right results are indicated in red comments. Note that the project cannot be accepted until these issues are resolved.
# </div>    
# 
# <hr>
#     
# **Please, use some color other than those listed to highlight answers to my comments.**
# I would also ask you **not to change, move or delete my comments** so that it would be easier for me to navigate during the next review.
#     
# In addition, my comments are defined as headings. 
# They can mess up the content, however, they are convenient, since you can immediately go to them. I will remove the headings from my comments in the next review. 
#    
#     
#     
# <hr>
#     
# <font color='dodgerblue'>**A few words about the project:**</font> you did a great job, everything is clear and neat. However, there are some issues that need to be fixed. I've also  left some comments with the recommendations for improving the project. If you have any questions, feel free to ask me.
#     
#     
# I will wait for the project for a second review :)
#     
#     
# 📌 Here are some tips and tricks that may help you with Markdown cells:    
# <hr style="border-top: 3px solid purple; "></hr>
# 
# You can leave comments using this code inside a Markdown cell:
#     
#     
#     <div class="alert alert-info">
#     <h2> Student's comment</h2>
# 
#     Your text here. 
#     </div>
# 
#     
#     
#     <font color='red'> This code is used to change text color. </font>     
# 
# <font color='red'> It will look like this. </font> 
#     
# If you don't want your comments to be headings, replace **h2** with **b** or just add `<a class="tocSkip">` after the phrase *Student's comment*.
# 
# 
# You can find out how to **format text** in a Markdown cell or how to **add links** [here](https://sqlbak.com/blog/jupyter-notebook-markdown-cheatsheet) и [and here](https://medium.com/analytics-vidhya/the-ultimate-markdown-guide-for-jupyter-notebook-d5e5abf728fd).
# 
# 
# 
# </div>

# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <b> Reviewer's comment 2</b>
# 
# 
# Thank you for correcting your project! :) I've left new comments titled as **Reviewer's comment 2**. 
#     
#     
# Your project has passed code review. Congratulations 😊
#  
#     
# This is a good [article](https://www.kaggle.com/ramprakasism/pandas-75-exercises-with-solutions/notebook) with 75 pandas exercises and solutions. You can go along the exercises and compare your solution with the solution in the article.
#     
#     
#     
# Take care and good luck! 😊      
#     
#     
#     
# <hr>    
#     
#     
# Best regards, 
#     
#     
# S.N.    
# </div>

# In[ ]:





# # Yandex.Music

# # Contents <a id='back'></a>
# 
# * [Introduction](#intro)
# * [Stage 1. Data overview](#data_review)
#     * [Conclusions](#data_review_conclusions)
# * [Stage 2. Data preprocessing](#data_preprocessing)
#     * [2.1 Header style](#header_style)
#     * [2.2 Missing values](#missing_values)
#     * [2.3 Duplicates](#duplicates)
#     * [2.4 Conclusions](#data_preprocessing_conclusions)
# * [Stage 3. Testing the hypotheses](#hypotheses)
#     * [3.1 Hypothesis 1: user activity in the two cities](#activity)
#     * [3.2 Hypothesis 2: music preferences on Monday and Friday](#week)
#     * [3.3 Hypothesis 3: genre preferences in Springfield and Shelbyville](#genre)
# * [Findings](#end)

# ## Introduction <a id='intro'></a>
# Whenever we're doing research, we need to formulate hypotheses that we can then test. Sometimes we accept these hypotheses; other times, we reject them. To make the right decisions, a business must be able to understand whether or not it's making the right assumptions.
# 
# In this project, you'll compare the music preferences of the cities of Springfield and Shelbyville. You'll study real Yandex.Music data to test the hypotheses below and compare user behavior for these two cities.
# 
# ### Goal: 
# Test three hypotheses:
# 1. User activity differs depending on the day of the week and from city to city. 
# 2. On Monday mornings, Springfield and Shelbyville residents listen to different genres. This is also true for Friday evenings. 
# 3. Springfield and Shelbyville listeners have different preferences. In Springfield, they prefer pop, while Shelbyville has more rap fans.
# 
# ### Stages 
# Data on user behavior is stored in the file `/datasets/music_project_en.csv`. There is no information about the quality of the data, so you will need to explore it before testing the hypotheses. 
# 
# First, you'll evaluate the quality of the data and see whether its issues are significant. Then, during data preprocessing, you will try to account for the most critical problems.
#  
# Your project will consist of three stages:
#  1. Data overview
#  2. Data preprocessing
#  3. Testing the hypotheses
#  
# [Back to Contents](#back)

# ## Stage 1. Data overview <a id='data_review'></a>
# 
# Open the data on Yandex.Music and explore it.

# You'll need `pandas`, so import it.

# In[2]:


# importing pandas
import pandas as pd


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# Good that you are using **pd** to reference pandas. It is convenient as every programmer or analyst has to look for the information on the web or in a documentation. Sometimes you may search for a ready solution and use of a common style is a good idea here as it simplifies understanding someone's code and even copy-paste process. 
#      
# </div>

# Read the file `music_project_en.csv` from the `/datasets/` folder and save it in the `df` variable:

# In[3]:


# reading the file and storing it to df
df = pd.read_csv('/datasets/music_project_en.csv')


# Print the first 10 table rows:

# In[4]:


# obtaining the first 10 rows from the df table
display(df.head(10))


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# It's much better to use display instead of print for dataframes. Take a look:     
# </div>

# In[5]:


# Reviewer's code

display(df)


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment </h2>
#     
# Display is a great thing. The point is, jupyter notebook is an interactive environment that already includes display. When we call a dataframe (see the code below), jupyter prints this dataframe like we do with the display method:</div>

# In[6]:


# Reviewer's code

df


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment </h2>
#     
# If you want to print more than one dataframe, only last command will be executed: 
# 
# </div>

# In[7]:


# Reviewer's code

df.head(4)
df.head(3)
df.head(2)


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment </h2>
#     
# And that's where we need **display**: </div>

# In[8]:


# Reviewer's code

display(df.head(4))
display(df.head(3))

df.head(2)


# Obtaining the general information about the table with one command:

# In[9]:


# obtaining general information about the data in df
display(df.info())


# The table contains seven columns. They all store the same data type: `object`.
# 
# According to the documentation:
# - `'userID'` — user identifier
# - `'Track'` — track title
# - `'artist'` — artist's name
# - `'genre'`
# - `'City'` — user's city
# - `'time'` — the exact time the track was played
# - `'Day'` — day of the week
# 
# We can see three issues with style in the column names:
# 1. Some names are uppercase, some are lowercase.
# 2. There are spaces in some names.
# 3. userID should be spaced out as user_id.
# 
# The number of column values is different. This means the data contains missing values.
# 

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# Indeed. It's recommended that we use **snake_case**. It's elegant and saves our time when we work with somebody's code.  
# 
# </div>
# 

# ### Conclusions <a id='data_review_conclusions'></a> 
# 
# Each row in the table stores data on a track that was played. Some columns describe the track itself: its title, artist and genre. The rest convey information about the user: the city they come from, the time they played the track. 
# 
# It's clear that the data is sufficient to test the hypotheses. However, there are missing values.
# 
# To move forward, we need to preprocess the data.

# [Back to Contents](#back)

# ## Stage 2. Data preprocessing <a id='data_preprocessing'></a>
# Correct the formatting in the column headers and deal with the missing values. Then, check whether there are duplicates in the data.

# ### Header style <a id='header_style'></a>
# Print the column header:

# In[10]:


# the list of column names in the df table
display(df.columns)


# Change column names according to the rules of good style:
# * If the name has several words, use snake_case
# * All characters must be lowercase
# * Delete spaces

# In[11]:


# renaming columns
df = df.rename(columns={
    '  userID': 'user_id', 
    'Track': 'track',
    '  City  ': 'city',
    'Day': 'day' 
})


# Check the result. Print the names of the columns once more:

# In[12]:


# checking result: the list of column names
display(df.columns)


# [Back to Contents](#back)

# ### Missing values <a id='missing_values'></a>
# First, find the number of missing values in the table. To do so, use two `pandas` methods:

# In[13]:


# calculating missing values
display(df.isna().sum())


# Not all missing values affect the research. For instance, the missing values in `track` and `artist` are not critical. You can simply replace them with clear markers.
# 
# But missing values in `'genre'` can affect the comparison of music preferences in Springfield and Shelbyville. In real life, it would be useful to learn the reasons why the data is missing and try to make up for them. But we do not have that opportunity in this project. So you will have to:
# * Fill in these missing values with markers
# * Evaluate how much the missing values may affect your computations

# Replace the missing values in `'track'`, `'artist'`, and `'genre'` with the string `'unknown'`. To do this, create the `columns_to_replace` list, loop over it with `for`, and replace the missing values in each of the columns:

# In[14]:


# looping over column names and replacing missing values with 'unknown'
for columns_to_replace in ['track', 'artist', 'genre']:
    df[columns_to_replace] = df[columns_to_replace].fillna('unknown')

display(df)


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
#  
# We need to iterate over the list of genre names. But in the code above there's a loop over the dataframe. When you iterate over the list of names, the looping variable takes 3 values: 'track', 'artist' and 'genre'. The idea is to  call a fillna method for each of these values separately, one by one. Moreover, a looping variable is not even used here. 
# 
# </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# I believe I got it on this iteration. Was there also another way to approach this? (As a side note, with the instructions aside, was the first go-around technically correct or would it have led to an error down the line? Thank you! 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# The first one was correct, butthe looping variable was not used, which means that you used a loop for no purpose. Exactly like in the code below:    
# </div>

# In[15]:


# Rewiever's code

for i in [1,2,3]:
    print('f')


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# We just print *f* 3 times, so why do we need *i* here? In your previous code you were replacing wrong values 3 times. The idea is to create  a loop, go through all the wrong values ('track', 'artist', 'genre') and to make a replacement once.
# 
# </div>
# 
# 
# ```python
# 
# columns_to_replace = ['track', 'artist', 'genre']
# 
# for column in columns_to_replace:
#     df[column] = df[column].fillna('unknown')
# ```

# Make sure the table contains no more missing values. Count the missing values again.

# In[16]:


# counting missing values
display(df.isna().sum())


# [Back to Contents](#back)

# ### Duplicates <a id='duplicates'></a>
# Find the number of obvious duplicates in the table using one command:

# In[17]:


# counting clear duplicates
display(df.duplicated().sum()) 


# Call the `pandas` method for getting rid of obvious duplicates:

# In[18]:


# removing obvious duplicates
df[df.duplicated()]
df = df.drop_duplicates()

display(df.head())


# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# 
# Do we need a duplicated_df? 
# </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# That's actually a great point that I wasn't even thinking about when going through it. I was just going through the motions and that was the result I found. I excluded it out since I realized it's not necessary and to clean up the code. Thank you! 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# Got it :) 
# </div>

# Count obvious duplicates once more to make sure you have removed all of them:

# In[19]:


# checking for duplicates
print(df.duplicated().sum())


# Now get rid of implicit duplicates in the `genre` column. For example, the name of a genre can be written in different ways. Such errors will also affect the result.

# Print a list of unique genre names, sorted in alphabetical order. To do so:
# * Retrieve the intended DataFrame column 
# * Apply a sorting method to it
# * For the sorted column, call the method that will return all unique column values

# In[20]:


# viewing unique genre names
unique_genres = sorted(df['genre'].unique())
display(unique_genres)


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# Don't forget about sorting :)
# </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# I wasn't sure if I was supposed to replace anything so I created a variable instead to display the data. 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# It can also be executed in exactly as follows: 
# 
# </div>
# 
# 
# ```python
# 
# df['genre'].sort_values().unique()
# ```

# Look through the list to find implicit duplicates of the genre `hiphop`. These could be names written incorrectly or alternative names of the same genre.
# 
# You will see the following implicit duplicates:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# To get rid of them, declare the function `replace_wrong_genres()` with two parameters: 
# * `wrong_genres=` — the list of duplicates
# * `correct_genre=` — the string with the correct value
# 
# The function should correct the names in the `'genre'` column from the `df` table, i.e. replace each value from the `wrong_genres` list with the value in `correct_genre`.

# In[21]:


# function for replacing implicit duplicates
def replace_wrong_genres(wrong_genres, correct_genre):
    for wrong_genre in wrong_genres:
        df['genre'] = df['genre'].replace(wrong_genre, correct_genre)


# Call `replace_wrong_genres()` and pass it arguments so that it clears implicit duplcates (`hip`, `hop`, and `hip-hop`) and replaces them with `hiphop`:

# In[22]:


# removing implicit duplicates
duplicates = ['hip', 'hop', 'hip-hop']
right_genre = 'hiphop'
replace_wrong_genres(duplicates, right_genre)


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# Great. You wrote and  called a function that worked properly.
# 
# In general, it can be performed without a function. To do this, we need a list and the same **replace** method. It will look like this:
#     
#     
#     wrong_genres = ['hip', 'hop', 'hip-hop']
#     correct_genre = 'hiphop'  
# 
#     df['genre'] = df['genre'].replace(wrong_genres, correct_genre)
#     
#     
# Or, which is the same:
#     
#     
#     df['genre'] = df['genre'].replace(['hip', 'hop', 'hip-hop'], 'hiphop')
# </div>

# Make sure the duplicate names were removed. Print the list of unique values from the `'genre'` column:

# In[23]:


# checking for implicit duplicates
display(sorted(df['genre'].unique()))


# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment </b>
#     
# Some sorting would make it look better, since we use sorting to simplify searching for the duplicates like *hip-hop* and *hiphop*. 
# 
# </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# That's a good point (I need to get into the habit of sorting through data more to make it easier to view and catch errors) I updated. 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2 </h2>
#     
# Yes, it may be useful :) 
# </div>

# [Back to Contents](#back)

# ### Conclusions <a id='data_preprocessing_conclusions'></a>
# We detected three issues with the data:
# 
# - Incorrect header styles
# - Missing values
# - Obvious and implicit duplicates
# 
# The headers have been cleaned up to make processing the table simpler.
# 
# All missing values have been replaced with `'unknown'`. But we still have to see whether the missing values in `'genre'` will affect our calculations.
# 
# The absence of duplicates will make the results more precise and easier to understand.
# 
# Now we can move on to testing hypotheses. 

# [Back to Contents](#back)

# ## Stage 3. Testing hypotheses <a id='hypotheses'></a>

# ### Hypothesis 1: comparing user behavior in two cities <a id='activity'></a>

# According to the first hypothesis, users from Springfield and Shelbyville listen to music differently. Test this using the data on three days of the week: Monday, Wednesday, and Friday.
# 
# * Divide the users into groups by city.
# * Compare how many tracks each group played on Monday, Wednesday, and Friday.
# 

# For the sake of practice, perform each computation separately. 
# 
# Evaluate user activity in each city. Group the data by city and find the number of songs played in each group.
# 
# 

# In[24]:


# Counting up the tracks played in each city
# print(df['city'].value_counts()['Springfield'])
# print(df['city'].value_counts()['Shelbyville'])

display(df.groupby('city')['track'].count())


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# We are asked to try  **groupby** method here. Would you do this? 
# </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# Thank you, I believe I updated it correctly (interesting how you can find mulitple ways to get the same result... Although if I kept it like I did, does it influence the results in a negative way as we go through the data? (Would I get an unexpected error?) 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# Now, you would not. However, if we had more cities, you would need much more time to print them using the previous approach. With a groupby method, it's super easy. 
# 
# 
# 
# By the way, you can print Series this way:
# </div>

# In[45]:


# Reviewer's code

df.groupby('city')[['user_id']].count()


# Springfield has more tracks played than Shelbyville. But that does not imply that citizens of Springfield listen to music more often. This city is simply bigger, and there are more users.
# 
# Now group the data by day of the week and find the number of tracks played on Monday, Wednesday, and Friday.
# 

# In[25]:


# Calculating tracks played on each of the three days
# print(df['day'].value_counts()['Monday'])
# print(df['day'].value_counts()['Wednesday'])
# print(df['day'].value_counts()['Friday'])

display(df.groupby('day')['track'].count())


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# And here :) 
# </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# Fixed! 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# Correct.
#     
# </div>
# 
# 

# Wednesday is the quietest day overall. But if we consider the two cities separately, we might come to a different conclusion.

# You have seen how grouping by city or day works. Now write a function that will group by both.
# 
# Create the `number_tracks()` function to calculate the number of songs played for a given day and city. It will require two parameters:
# * day of the week
# * name of the city
# 
# In the function, use a variable to store the rows from the original table, where:
#   * `'day'` column value is equal to the `day` parameter
#   * `'city'` column value is equal to the `city` parameter
# 
# Apply consecutive filtering with logical indexing.
# 
# Then calculate the `'user_id'` column values in the resulting table. Store the result to a new variable. Return this variable from the function.

# In[26]:


# <creating the function number_tracks()>
# We'll declare a function with two parameters: day=, city=.
# Let the track_list variable store the df rows where
# the value in the 'day' column is equal to the day= parameter and, at the same time, 
# the value in the 'city' column is equal to the city= parameter (apply consecutive filtering 
# with logical indexing).
# Let the track_list_count variable store the number of 'user_id' column values in track_list
# (found with the count() method).
# Let the function return a number: the value of track_list_count.
# The function counts tracked played for a certain city and day.
# It first retrieves the rows with the intended day from the table,
# then filters out the rows with the intended city from the result,
# then finds the number of 'user_id' values in the filtered table,
# then returns that number.
# To see what it returns, wrap the function call in print().
def number_tracks(day, city):
    track_list = df.loc[(df['day'] == day) & (df['city'] == city)]
    track_list_count = track_list['user_id'].count()
    return track_list_count


# <div class="alert alert-warning" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment</b>
#     
# 
# You don't need to return a print function -  you should return a variable instead, without calling a print function. 
# </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# Good to know for the future, thank you I updated. 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# I am glad to help.     
# </div>

# Call `number_tracks()` six times, changing the parameter values, so that you retrieve the data on both cities for each of the three days.

# In[27]:


# the number of songs played in Springfield on Monday
number_tracks('Monday', 'Springfield')


# In[28]:


# the number of songs played in Shelbyville on Monday
number_tracks('Monday', 'Shelbyville')


# In[29]:


# the number of songs played in Springfield on Wednesday
number_tracks('Wednesday', 'Springfield')


# In[30]:


# the number of songs played in Shelbyville on Wednesday
number_tracks('Wednesday', 'Shelbyville')


# In[31]:


# the number of songs played in Springfield on Friday
number_tracks('Friday', 'Springfield')


# In[32]:


# the number of songs played in Shelbyville on Friday
number_tracks('Friday', 'Shelbyville')


# Use `pd.DataFrame` to create a table, where
# * Column names are: `['city', 'monday', 'wednesday', 'friday']`
# * The data is the results you got from `number_tracks()`

# In[33]:


# table with results
data = {'city': ['Springfield', 'Shelbyville'],
        'monday': [15740, 5614],
        'wednesday': [11056, 7003],
        'friday': [15945, 5895],
        }

city_days_df = pd.DataFrame(data)

print(city_days_df)


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# All values are correct.</div>

# **Conclusions**
# 
# The data reveals differences in user behavior:
# 
# - In Springfield, the number of songs played peaks on Mondays and Fridays, while on Wednesday there is a decrease in activity.
# - In Shelbyville, on the contrary, users listen to music more on Wednesday. User activity on Monday and Friday is smaller.
# 
# So the first hypothesis seems to be correct.

# [Back to Contents](#back)

# ### Hypothesis 2: music at the beginning and end of the week <a id='week'></a>

# According to the second hypothesis, on Monday morning and Friday night, citizens of Springfield listen to genres that differ from ones users from Shelbyville enjoy.

# Get tables (make sure that the name of your combined table matches the DataFrame given in the two code blocks below):
# * For Springfield — `spr_general`
# * For Shelbyville — `shel_general`

# In[34]:


# create the spr_general table from the df rows, 
# where the value in the 'city' column is 'Springfield'
spr_general = df.loc[df['city'] == 'Springfield']


# In[35]:


# create the shel_general from the df rows,
# where the value in the 'city' column is 'Shelbyville'
shel_general = df[df['city'] == 'Shelbyville']


# Write the `genre_weekday()` function with four parameters:
# * A table for data (`df`)
# * The day of the week (`day`)
# * The first timestamp, in 'hh:mm' format (`time1`)
# * The last timestamp, in 'hh:mm' format (`time2`)
# 
# The function should return info on the 15 most popular genres on a given day within the period between the two timestamps.

# In[36]:


# 1) Let the genre_df variable store the rows that meet several conditions:
#    - the value in the 'day' column is equal to the value of the day= argument
#    - the value in the 'time' column is greater than the value of the time1= argument
#    - the value in the 'time' column is smaller than the value of the time2= argument
#    Use consecutive filtering with logical indexing.

# 2) Group genre_df by the 'genre' column, take one of its columns, 
#    and use the count() method to find the number of entries for each of 
#    the represented genres; store the resulting Series to the
#    genre_df_count variable

# 3) Sort genre_df_count in descending order of frequency and store the result
#    to the genre_df_sorted variable

# 4) Return a Series object with the first 15 genre_df_sorted value - the 15 most
#    popular genres (on a given day, within a certain timeframe)

# Write your function here
    
    # consecutive filtering
    # Create the variable genre_df which will store only those df rows where the day is equal to day=

    # filter again so that genre_df will store only those rows where the time is smaller than time2=

    # filter once more so that genre_df will store only rows where the time is greater than time1=

    # group the filtered DataFrame by the column with the names of genres, take the genre column, and find the number of rows for each genre with the count() method

    # sort the result in descending order (so that the most popular genres come first in the Series object)

    # we will return the Series object storing the 15 most popular genres on a given day in a given timeframe
def genre_weekday(df, day, time1, time2):
    genre_df = df.loc[(df['day'] == day) & (df['time'] < time2) & (df['time'] > time1)]
    genre_df_count = genre_df.groupby('genre')['track'].count()
    genre_df_sorted = genre_df_count.sort_values(ascending=False) 
    return genre_df_sorted.head(15)


# Compare the results of the `genre_weekday()` function for Springfield and Shelbyville on Monday morning (from 7AM to 11AM) and on Friday evening (from 17:00 to 23:00):

# In[37]:


# calling the function for Monday morning in Springfield (use spr_general instead of the df table)
genre_weekday(spr_general, 'Monday', '07:00:00', '11:00:00')


# In[38]:


# calling the function for Monday morning in Shelbyville (use shel_general instead of the df table)
genre_weekday(shel_general, 'Monday', '07:00:00', '11:00:00')


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment </b>
#     
# We should use morning hours for Mondays and evening hours for Fridays. </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# Thank you, I read it wrong for some reason. Fixed now! 
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# Now it's correct, thank you!     
# </div>

# In[39]:


# calling the function for Friday evening in Springfield
genre_weekday(spr_general, 'Friday', '17:00:00', '23:00:00')


# In[40]:


# calling the function for Friday evening in Shelbyville
genre_weekday(shel_general, 'Friday', '17:00:00', '23:00:00')


# **Conclusion**
# 
# Having compared the top 15 genres on Monday morning, we can draw the following conclusions:
# 
# 1. Users from Springfield and Shelbyville listen to similar music. The top five genres are the same, only rock and electronic have switched places.
# 
# 2. In Springfield, the number of missing values turned out to be so big that the value `'unknown'` came in 10th. This means that missing values make up a considerable portion of the data, which may be a basis for questioning the reliability of our conclusions.
# 
# For Friday evening, the situation is similar. Individual genres vary somewhat, but on the whole, the top 15 is similar for the two cities.
# 
# Thus, the second hypothesis has been partially proven true:
# * Users listen to similar music at the beginning and end of the week.
# * There is no major difference between Springfield and Shelbyville. In both cities, pop is the most popular genre.
# 
# However, the number of missing values makes this result questionable. In Springfield, there are so many that they affect our top 15. Were we not missing these values, things might look different.

# [Back to Contents](#back)

# ### Hypothesis 3: genre preferences in Springfield and Shelbyville <a id='genre'></a>
# 
# Hypothesis: Shelbyville loves rap music. Springfield's citizens are more into pop.

# Group the `spr_general` table by genre and find the number of songs played for each genre with the `count()` method. Then sort the result in descending order and store it to `spr_genres`.

# In[41]:


# on one line: group the spr_general table by the 'genre' column, 
# count the 'genre' values with count() in the grouping, 
# sort the resulting Series in descending order, and store it to spr_genres
# this code below would return a dataframe instead of a Series
# spr_genres = spr_general.groupby('genre').count().sort_values(by='track', ascending=False)
spr_genres = spr_general.groupby('genre')['genre'].count().sort_values(ascending=False)


# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <b> Reviewer's comment </b>
#     
# We are asked to return a Series - not dataframe. Would you try? </div>
# 
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# Ahh, I see the difference now that I've typed it out. Thank you. I still left the other one commented out just for my reference in the future.
# </div>
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# Yes. These are different objects that have different methods.     
# </div>

# Print the first 10 rows from `spr_genres`:

# In[42]:


# printing the first 10 rows of spr_genres
display(spr_genres.head(10))


# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# One more trick is to convert series to a dataframe:
# 
# </div>
# 

# In[46]:


# Reviewer's code

spr_genres.to_frame().head(10)


# Now do the same with the data on Shelbyville.
# 
# Group the `shel_general` table by genre and find the number of songs played for each genre. Then sort the result in descending order and store it to the `shel_genres` table:
# 

# In[43]:


# on one line: group the shel_general table by the 'genre' column, 
# count the 'genre' values in the grouping with count(), 
# sort the resulting Series in descending order and store it to shel_genres
# this code below would return a dataframe instead of a Series
# shel_genres = shel_general.groupby('genre').count().sort_values(by='track', ascending=False)

shel_genres = shel_general.groupby('genre')['genre'].count().sort_values(ascending=False)


# Print the first 10 rows of `shel_genres`:

# In[44]:


# printing the first 10 rows from shel_genres
display(shel_genres.head(10))


# **Conclusion**

# The hypothesis has been partially proven true:
# * Pop music is the most popular genre in Springfield, as expected.
# * However, pop music turned out to be equally popular in Springfield and Shelbyville, and rap wasn't in the top 5 for either city.
# 

# [Back to Contents](#back)

# # Findings <a id='end'></a>

# We have tested the following three hypotheses:
# 
# 1. User activity differs depending on the day of the week and from city to city. 
# 2. On Monday mornings, Springfield and Shelbyville residents listen to different genres. This is also true for Friday evenings. 
# 3. Springfield and Shelbyville listeners have different preferences. In both Springfield and Shelbyville, they prefer pop.
# 
# After analyzing the data, we concluded:
# 
# 1. User activity in Springfield and Shelbyville depends on the day of the week, though the cities vary in different ways. 
# 
# The first hypothesis is fully accepted.
# 
# 2. Musical preferences do not vary significantly over the course of the week in both Springfield and Shelbyville. We can see small differences in order on Mondays, but:
# * In Springfield and Shelbyville, people listen to pop music most.
# 
# So we can't accept this hypothesis. We must also keep in mind that the result could have been different if not for the missing values.
# 
# 3. It turns out that the musical preferences of users from Springfield and Shelbyville are quite similar.
# 
# The third hypothesis is rejected. If there is any difference in preferences, it cannot be seen from this data.
# 
# ### Note 
# In real projects, research involves statistical hypothesis testing, which is more precise and more quantitative. Also note that you cannot always draw conclusions about an entire city based on the data from just one source.
# 
# You will study hypothesis testing in the sprint on statistical data analysis.

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment</h2>
#     
# The general conclusion is very important. Often, our tasks end with the  presentation or report for the client. Therefore, all results should be described in a general conclusion. Ideally, one should reinforce it with the previously obtained values.
# </div>

# [Back to Contents](#back)

# <div style="border-radius: 15px; border: 3px solid indigo; padding: 15px;">
# <h2> Overall conclusion <a class="tocSkip"></h2>
#  
# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
#     
# Thank you for submitting your project. You've done a really good job! Groupby methods are used correctly, functions are written accurately. I see that you are already good at using pandas 😊
#     
# </div>    
#     
# <div class="alert alert-danger" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
#     
# There are some issues that need to be fixed, but it will not take much time. As soon as you fix them, I will accept the project 😉 
# 
#     
#     
# </div>   
# <hr>    
# Best regards,
#     
# Sveta    
#     
# </div>
#     
# <div class="alert alert-info">
# <h2> Student's comment</h2>
# 
# I'll be honest, this one kicked my butt but I learned so much from trial and error. Thank you for the ama
# </div>

# <div class="alert alert-success" style="border-radius: 15px; box-shadow: 4px 4px 4px; border: 1px solid ">
# <h2> Reviewer's comment 2</h2>
#     
# Thank you for such a good job! 
# </div>
# 

# In[ ]:




