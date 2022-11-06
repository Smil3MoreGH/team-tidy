#!/usr/bin/env python
# coding: utf-8

# In[38]:


#imports
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(dpi=1200)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[39]:


#import the dataset with pandas
dataFrame = pd.read_excel('./salary/salary_data_states.xlsx')


# In[40]:


# reduce variables to only those needed for analyzing
salary = dataFrame.drop(columns=['CASE_NUMBER', 'CASE_STATUS', 'CASE_RECEIVED_DATE', 'DECISION_DATE', 'EMPLOYER_NAME', 'WORK_CITY', 'EDUCATION_LEVEL_REQUIRED', 'COLLEGE_MAJOR_REQUIRED', 'EXPERIENCE_REQUIRED_Y_N', 'EXPERIENCE_REQUIRED_NUM_MONTHS', 'COUNTRY_OF_CITIZENSHIP', 'PREVAILING_WAGE_SOC_CODE', 'PREVAILING_WAGE_SOC_TITLE', 'WORK_STATE_ABBREVIATION', 'WORK_POSTAL_CODE', 'FULL_TIME_POSITION_Y_N', 'PREVAILING_WAGE_PER_YEAR', 'order'])


# In[41]:


#clean the dataset, remove null
salary['JOB_TITLE_SUBGROUP'] = salary['JOB_TITLE_SUBGROUP'].fillna("Nothing")


# In[42]:


salary.JOB_TITLE_SUBGROUP.unique()


# In[49]:


# Compare H1-B1 vs Greencard salaries for each JOB_TITLE_SUBGROUP
# Group by JOB_TITLE_SUBGROUP and get column data for PAID_WAGE_PER_YEAR
#   seperated by VISA_CLASS

salary.groupby(['JOB_TITLE_SUBGROUP', 'VISA_CLASS'])['PAID_WAGE_PER_YEAR'].mean()


# In[ ]:




