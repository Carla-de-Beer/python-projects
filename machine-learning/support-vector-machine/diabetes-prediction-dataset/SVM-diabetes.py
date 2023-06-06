#!/usr/bin/env python
# coding: utf-8

# # Diabetes prediction dataset

# Diabetes Prediction Dataset from Kaggle: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

# ## Feature Engineering
# ### Visualising the data and performing feature engineering
# 
# * The result set is skewed, since most people in the study, as in life, do not have diabetes. This means that a machine learning model, however good or bad, is likely to most often guess the correct answer. Model accuracy therefore won't be the guiding factor for this dataset.
# 
# * The `smoking_history` column has some missing data. Since the "never" and "no info" categories have similar diabetes rates, these two categories may be lumped together (leaving the `smoking_history` column off completely did not influence the result much, so this could be considered). 
# 
# * There are no strong correlations between the features. The only correlation that appears to have some significance, albeit a low one, is that between `age` and `bmi`.

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


# In[2]:


# Reading in the data
df = pd.read_csv('diabetes_prediction_dataset.csv')
df


# In[3]:


sns.countplot(x='diabetes',data=df)


# In[4]:


sns.countplot(x='hypertension',data=df)


# In[5]:


sns.countplot(x='heart_disease',data=df)


# In[6]:


sns.displot(df['age'], kde=False)


# In[7]:


sns.kdeplot(data=df, x="age", hue="diabetes", multiple="stack")


# In[48]:


sns.displot(df['gender'], kde=False)


# In[9]:


sns.countplot(x='smoking_history',hue='diabetes',data=df)


# In[10]:


sns.displot(df['bmi'], kde=False, bins=100)


# In[11]:


sns.displot(df['smoking_history'], kde=False)


# In[12]:


# Confirming that there are no obvious missing data points
df.isnull().sum()


# In[13]:


# Separating the y-values
y = df.iloc[:, 8].values
y


# In[14]:


# Separating the X-values
X = df.iloc[:, 0:8]


# In[15]:


# Mapping the categorical data
gender_mapping = {
    'Female': 0,
    'Male': 1,
    'Other': 2
}

X0 = X.iloc[:, 0:1].replace({'gender': gender_mapping})
X0

X['gender'] = X0


# In[16]:


smoking_mapping = {
    'Never': 0,
    'No Info': 0,
    'current': 2,
    'former': 3,
    'not current': 4
}

X0 = X.iloc[:, 0:1].replace({'smoking_history': smoking_mapping})
X0

X['smoking_history'] = X0


# In[17]:


sns.countplot(data=df, x="smoking_history", hue="diabetes")


# In[18]:


X


# In[19]:


# Plot the correlation matrix
sns.heatmap(X.corr(), cmap='RdBu', vmin=-1, vmax=1, annot=True);


# ## Support Vector Machine

# In[21]:


# Preparing the data for training and classification
X.to_numpy()


# In[22]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


# In[29]:


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[35]:


classifier = SVC(kernel='poly', random_state=0)
classifier.fit(X_train, y_train)
Pipeline(steps=[('standardscaler', StandardScaler()), ('svc', SVC(gamma='auto'))])


# In[36]:


y_pred = classifier.predict(X_test)


# In[37]:


cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)


# In[38]:


disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classifier.classes_)
disp.plot()
print("Confusion Matrix:\n", disp)


# In[49]:


report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)


# In[ ]:




