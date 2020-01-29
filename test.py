#!/usr/bin/env python
# coding: utf-8

# In[10]:


from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import GridSearchCV 
import pandas as pd
import numpy as np1
#from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from joblibspark import register_spark
from sklearn.utils import parallel_backend
from sklearn.ensemble import RandomForestClassifier
from pyspark.sql import SparkSession


# In[ ]:





# In[2]:


#from pyspark.ml import Pipeline
from pyspark.ml.classification import GBTClassifier
#from pyspark.ml.classification import RandomForestClassifier
#from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
#from pyspark.ml.evaluation import MulticlassClassificationEvaluator


# In[3]:


register_spark()


# In[4]:


wine_data = pd.read_csv('wine.csv')
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC(gamma='auto')


# In[5]:


wine_data.head()


# In[6]:


# separate target from training features
y = wine_data.quality
X = wine_data.drop('quality', axis=1)


# In[7]:


# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y, 
    test_size=0.2, 
    random_state=123, 
    stratify=y
)


# In[8]:


hyperparameters = {'randomforestclassifier__max_features': [None, 'auto', 'sqrt', 'log2'],
                   'randomforestclassifier__max_depth': [None, 3, 5, 10],}


# In[ ]:





# In[12]:


# fit and tune model
clf = RandomForestClassifier()


# In[13]:


with parallel_backend('spark', n_jobs=3):
    clf.fit(X_train, y_train)


# In[ ]:




