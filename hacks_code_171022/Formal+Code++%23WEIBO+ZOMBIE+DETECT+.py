
# coding: utf-8

# # Machine Learning

# ## Data Preprocessing

# ### load data

# In[1]:

import xlrd  
import csv  
from os import sys  
  
def csv_from_excel(excel_file):  
    workbook = xlrd.open_workbook(excel_file)  
    all_worksheets = workbook.sheet_names()  
    for worksheet_name in all_worksheets:  
        worksheet = workbook.sheet_by_name(worksheet_name)  
        your_csv_file = open(''.join(['data1.csv']), 'wb')  
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)  
  
  
        for rownum in xrange(worksheet.nrows):  
            wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])  
        your_csv_file.close()  
csv_from_excel('data1.xlsx')


# ### combine the data

# In[53]:

df_real12 = pd.read_csv('later/real12.csv')
df_real12.columns = ['id', 'max', 'word']
for index, row in df_real12.iterrows():
    df_real12['word'][index] = 1-float(len(set(row.word)))/len(row.word)
    #row.word = float(len(set(row.word)))/len(row.word)
df_real12.drop(df_real12.index[1])

df_real22 = pd.read_csv('later/real22.csv')
df_real22.columns = ['id', 'max', 'word']
for index, row in df_real22.iterrows():
    df_real22['word'][index] = 1-float(len(set(row.word)))/len(row.word)
    #row.word = float(len(set(row.word)))/len(row.word)
df_real22.drop(df_real22.index[1])

df_real32 = pd.read_csv('later/real32.csv')
df_real32.columns = ['id', 'max', 'word']
for index, row in df_real32.iterrows():
    df_real32['word'][index] = 1-float(len(set(row.word)))/len(row.word)
    #row.word = float(len(set(row.word)))/len(row.word)
df_real32.drop(df_real32.index[1])

df_fake12 = pd.read_csv('later/fake12.csv')
df_fake12.columns = ['id', 'max', 'word']
for index, row in df_fake12.iterrows():
    df_fake12['word'][index] = float(len(set(row.word)))/len(row.word)
    #row.word = float(len(set(row.word)))/len(row.word)
df_fake12.drop(df_real12.index[1])



# ### data visialization 

# In[58]:

df_real2 = pd.concat([df_real12, df_real22, df_real32], axis = 0)
real2 = np.array(df_real2.iloc[:,2])

plt.hist(real2, alpha = 0.5)

fake2 = np.array(df_fake12.iloc[:,2])
plt.hist(fake2, alpha = 0.5, color = 'red')
plt.xlabel("regulation")
plt.ylabel("numbers")


# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

df_real11 = pd.read_csv('real11.csv')
df_real11.columns = ['id0','id', 'num', 'attention', 'fans']
df_real21 = pd.read_csv('real21.csv')
df_real21.columns = ['id0','id', 'num', 'attention', 'fans']
df_real31 = pd.read_csv('real31.csv')
df_real31.columns = ['id0','id', 'num', 'attention', 'fans']

df_real12 = pd.read_csv('real12.csv')
df_real22 = pd.read_csv('real22.csv')
df_real32 = pd.read_csv('real32.csv')

df_real = pd.concat([df_real11, df_real21, df_real31], axis = 0)
df_real['zombie'] = 0

df_data1 = pd.read_csv('data1.csv')
df_data1.columns = ['id0','id', 'num', 'attention', 'fans']
df_fake11 = pd.read_csv('fake21.csv')
df_fake11.columns = ['id0','id', 'num', 'attention', 'fans']

df_fake = pd.concat([df_data1, df_fake11], axis = 0)
df_fake['zombie'] = 1

df_real = df_real[['id', 'num', 'attention', 'fans', 'zombie']]
df_fake = df_fake[['id', 'num', 'attention', 'fans', 'zombie']]
df_total = pd.concat([df_real, df_fake], axis = 0)


# In[69]:

df_realq = df_real.iloc[:, 1:5]
df_fakeq = df_fake.iloc[:, 1:5]
df_totalq = df_total.iloc[:, 1:5]
df_realq_normal = df_realq.loc[(df_realq.attention <400)&(df_realq.num < 1000)&(df_realq.fans < 1000)]
df_fakeq_normal = df_fakeq.loc[(df_fakeq.attention <400)&(df_fakeq.num < 1000)&(df_fakeq.fans < 1000)]
df_totalq_normal = df_totalq.loc[(df_totalq.attention <400)&(df_totalq.num < 1000)&(df_totalq.fans < 1000)]

real = np.array(df_realq)
detect = np.array(df_real21)
fake = np.array(df_fakeq)

plt.scatter(real[:,2], real[:,1], alpha = 0.5, marker = 'o', color = "r")
plt.scatter(fake[:,2], fake[:,1], alpha = 0.5, marker = 'o', color = "b")

plt.xlabel("Number")
plt.ylabel("Attention Number")


# In[61]:

real =  np.array(df_realq_normal)
fake = np.array(df_fakeq_normal)
plt.scatter(real[:,2], real[:,1], alpha = 0.5, marker = 'o', color = "r")
plt.scatter(fake[:,2], fake[:,1], alpha = 0.5, marker = 'o', color = "b")

plt.xlabel("Number")
plt.ylabel("Attention Number")


# ### Train Test Split 

# In[62]:

total = np.array(df_totalq_normal)
print total[:5]
from sklearn.cross_validation import train_test_split
XTrain, XTest, yTrain, yTest = train_test_split(total[:, :3], total[:, 3], test_size = 0.25)


# ## Use The Model 

# In[64]:

from sklearn.ensemble import RandomForestClassifier
#model = RandomForestClassifier(n_estimators = 1000)
#model.fit(XTrain, yTrain)
#ypred = model.predict(XTest)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(fit_intercept = True)
model.fit(XTrain, yTrain)
ypred = model.predict(XTest)


# ## Parameters Turning

# In[65]:

from sklearn.grid_search import GridSearchCV

param_grid = {'n_estimators':[500], 
              'max_depth':[1,9,15,None],
              'min_samples_split':[3,9,15],
              'min_samples_leaf':[1,9,15],
              'bootstrap':[True, False],
              'criterion':['gini', 'entropy']}

grid = GridSearchCV(RandomForestClassifier(), param_grid)

grid.fit(total[:, :3], total[:, 3])


# In[68]:

print grid.best_params_
model = grid.best_estimator_
model.fit(XTrain, yTrain)
ypred = model.predict(XTest)


# ## Prediction

# In[106]:

ydetect = model.predict(real[:, :3])
print '关晓彤的僵尸粉比例为 ' + str((sum(ydetect)+0.0)/len(ydetect)*100) +'%'
r = list(ydetect)
app = []
for i in range(len(r)):
    if r[i] ==1:
        app.append(i)
print '僵尸粉的信息：',df_real.iloc[97]
print ''
print '僵尸粉用户名列表'
for i in app:
    print df_real.iloc[i]['id']


# In[67]:

from sklearn import metrics
print (metrics.classification_report(ypred, yTest))


# In[ ]:



