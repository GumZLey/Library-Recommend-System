#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


import os

file_path = './data/books.csv'
if os.path.exists(file_path):
	df = pd.read_csv(file_path, quotechar='"', on_bad_lines='skip')
else:
	print(f"File not found: {file_path}")
df.head()


# In[3]:


df.shape


# In[4]:


df.isnull().sum()


# In[5]:


df.describe()


# In[6]:


features = ['title','authors','publisher']
df['combined_features'] = df.title + ' ' + df.authors + ' ' + df.publisher


# In[7]:


from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack

# Vectorize each feature separately
tfidf_title = TfidfVectorizer().fit_transform(df['title'])
tfidf_publisher = TfidfVectorizer().fit_transform(df['publisher'])
tfidf_author = TfidfVectorizer().fit_transform(df['authors'])

# Reduce weight of author's vector
tfidf_author = tfidf_author * 0.3  # e.g., reduce to 30% influence
tfidf_publisher =  tfidf_publisher * 0.3

# Combine all vectors
combined_matrix = hstack([tfidf_title, tfidf_publisher, tfidf_author])
cosine_sim = cosine_similarity(combined_matrix)


# In[15]:


import re


# In[16]:


def get_recommendations(title, cosine_sim=cosine_sim):
    user_choice = title
    user_index = df[df.title.str.contains(user_choice,case=False)].index[0]
    sim_movies = list(enumerate(cosine_sim[user_index]))
    sorted_sim_movies = sorted(sim_movies,key=lambda x:x[1],reverse=True)[1:]
    full_title = df.loc[user_index, 'title']

    recommend_books = []

    print('Recommend books for ' + full_title)
    for i,element in enumerate(sorted_sim_movies):
        book_id = element[0]
        title = df.title.iloc[book_id]
        score = element[1]
        author = df.authors.iloc[book_id]

        title = re.sub(r'\s*\([^)]*\)', '', title)
        recommend_books.append([title, score, author])
        print('{:30} {:3f} {:30}'.format(title,score,author))
        if i > 10:
            break
    return recommend_books


# In[17]:


print(get_recommendations('Harry Potter'))


# In[75]:


