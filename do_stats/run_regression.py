import pandas as pd
import statsmodels.api as sm

from defenisions import ROOT_DIR

variable_labels = ['Gender', 'Hispanic', 'Age', 'Income', 'Residence', 'Child', 'Assisted_Living',
                   'Chronic', 'Vulnerable_contact', 'Health_Insurance', 'News', 'Political',
                   'Self_employed', 'Remote', 'Education', 'Pregnant', 'Vehicle'
                   ]


'''
News ['Social media (Instagram, Facebook, X (Twitter), TikTok)'
 'TV (including cable)' 'Print media (newspapers, journals)'
 'News apps or websites' 'Radio or podcasts'
 'Do not read/listen/watch the news' 'Other']
Remote ['No' 'NA (studying, retired, not in paid employment)' 'Yes']
Education ['1 or more years of college credit, no degree' 'Postgraduate degree'
 'High school or GED' 'Some college credits' 'Undergraduate degree'
 'Associate’s degree']
Pregnant [nan 'No' 'Yes']
Vehicle ['No' 'Yes']

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


# one-hot encode the categorical variables
data_encoded = pd.get_dummies(data_reduced, columns=variable_labels)

# read two columns
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
                  'Self_employed_Yes',]]

y = data_encoded[y_label]

# fit the model
model = sm.Logit(y, X)
results = model.fit()

# Display the model summary (coefficients and confidence intervals)
print(results.summary())
# export results to csv
results.summary2().tables[1].to_csv('test.csv')
