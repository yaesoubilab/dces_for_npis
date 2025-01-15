import pandas as pd

from analysis_support import do_logistic_regression
from defenisions import ROOT_DIR
from fig_support import do_correlation_analysis, plot_logistic_regression_coeffs

variable_labels = ['Gender', 'Hispanic', 'Age', 'Income', 'Residence', 'Child', 'Assisted_Living',
                   'Chronic', 'Vulnerable_contact', 'Health_Insurance', 'News', 'Political',
                   'Self_employed', 'Remote', 'Education', 'Pregnant', 'Vehicle'
                   ]


'''
Race [
 'White' 
 'Black or African American'
 'American Indian or Native American or Alaskan Native'
 'Black or African American,White' 
 'Self-define' 'Asian/Asian American'
 'Asian/Asian American,White' 
 'Prefer not to answer' 
 'Chinese,White'
 'Native Hawaiian or Pacific Islander,American Indian or Native American or Alaskan Native,White'
 'Asian/Asian American,Filipino'
 'American Indian or Native American or Alaskan Native,White'
 'Middle Eastern or North African,White'
 'Native Hawaiian or Pacific Islander'
 'Asian/Asian American,Chinese,Filipino' 
 'Asian/Asian American,Chinese'
 'Japanese' 
 'Asian Indian' 
 'Chinese'
 'Native Hawaiian or Pacific Islander,Asian/Asian American,White'
 'Filipino'
 'Black or African American,American Indian or Native American or Alaskan Native'
 'Asian/Asian American,Japanese' 
 'Asian/Asian American,Korean'
 'Middle Eastern or North African'
 'Black or African American,American Indian or Native American or Alaskan Native,White'
 'Korean,White'
 'American Indian or Native American or Alaskan Native,Filipino'
 'Asian/Asian American,Asian Indian' 'Japanese,Korean']
'''

y_label = ['Class_1']

# read the data into table
data = pd.read_csv(ROOT_DIR+'/lca_individuals/results_LCA_no_vaccine_class_probabilities_and_characters.csv')

# remove rows with missing data
data_cleaned = data.dropna(subset=variable_labels + y_label)
data_reduced = data_cleaned[variable_labels + y_label]

# replace 'self_define', 'non_binary', 'prefer_not_to_answer' with 'Other'
data_reduced.loc[data_reduced['Gender'].isin(['Self-define', 'Non-binary', 'Prefer not to answer']), 'Gender'] = 'Other'
data_reduced.loc[data_reduced['Age'].isin(['50-64', '35-49' '25-34' '18-24']), 'Age'] = '<65'
data_reduced.loc[data_reduced['Pregnant'].isin(['No', 'nan']), 'Pregnant'] = 'No'
data_reduced.loc[data_reduced['Hispanic'].isin(['No', 'nan']), 'Hispanic'] = 'No'
data_reduced.loc[data_reduced['Education'].isin(
    ['Postgraduate degree', 'Undergraduate degree', 'Associate’s degree']), 'Education'] = 'With College Degree'
data_reduced.loc[data_reduced['Education'].isin([
    '1 or more years of college credit, no degree',
    'High school or GED',
    'Some college credits']), 'Education'] = 'Without College Degree'


# one-hot encode the categorical variables
data_encoded = pd.get_dummies(data_reduced, columns=variable_labels)

# read the coded columns
X = data_encoded[['Gender_Male', 'Gender_Other',
                  'Hispanic_Yes',
                  'Age_≥ 65',
                  'Income_$35,000 - 75,000', 'Income_$75,000 - 150,000', 'Income_> $150,000',
                  'Residence_Suburban', 'Residence_Rural',
                  'Child_Yes',
                  'Assisted_Living_Yes',
                  'Chronic_Yes','Chronic_Prefer not to answer',
                  'Vulnerable_contact_Yes',
                  'Health_Insurance_Yes',
                  'Political_Republican', 'Political_Independent', 'Political_Other',
                  'Self_employed_Yes',
                  'Remote_Yes', 'Remote_NA (studying, retired, not in paid employment)',
                  'Pregnant_Yes',
                  'Vehicle_Yes',
                  'News_Social media (Instagram, Facebook, X (Twitter), TikTok)',
                  'News_TV (including cable)',
                  'News_News apps or websites',
                  'News_Radio or podcasts',
                  'News_Do not read/listen/watch the news',
                  'News_Other',
                  'Education_With College Degree'
                  ]]
X = X.astype('float64')

y = data_encoded[y_label]

# do correlation analysis
do_correlation_analysis(X=X)

# do logistic regression
do_logistic_regression(X=X, y=y)

# plot logistic regression coefficients
plot_logistic_regression_coeffs()
