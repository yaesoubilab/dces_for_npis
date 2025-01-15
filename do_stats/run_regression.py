import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

from defenisions import ROOT_DIR

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
    '1 or more years of college credit, no degree', 'High school or GED', 'Some college credits']), 'Education'] = 'Without College Degree'


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

# correlation matrix
correlation_matrix = X.corr()
correlation_matrix.to_csv('correlation_matrix.csv', index=True)

# get the maximum and minimum correlation
np.fill_diagonal(correlation_matrix.values, np.nan)
print('Maximum correlation:', correlation_matrix.max().max())
print('Minimum correlation:', correlation_matrix.min().min())
print('')

plt.figure(figsize=(15, 14))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm')
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.savefig('correlation_matrix.png')

# fit the model
# add intercept
X_with_const = sm.add_constant(X)
model = sm.Logit(y, X_with_const)
results = model.fit()

# Display the model summary (coefficients and confidence intervals)
print(results.summary())
# export results to csv
results.summary2().tables[1].to_csv('logistic.csv')

# visualize
df = pd.read_csv('logistic.csv')
df = df.iloc[::-1]

# Filter for estimates and confidence intervals
df = df[['Unnamed: 0', 'Coef.', '[0.025', '0.975]']]
df.columns = ['Variables','Estimate', 'CI_Lower', 'CI_Upper']

# Plot estimates with confidence intervals
fig, ax = plt.subplots(1,1, figsize=(8, 6))
ax.errorbar(
    x=df['Estimate'],
    y=range(len(df['Estimate'])),
    xerr=[df['Estimate'] - df['CI_Lower'], df['CI_Upper'] - df['Estimate']],
    fmt='o',
    capsize=4,
    label='Estimate'
)

ax.axvline(x=0, color='gray', linestyle='--', linewidth=1)  # Reference line for zero
# ax.set_title('Logistic Regression Coefficients with Confidence Intervals')
ax.set_xlabel('Estimate')
ax.set_yticks(np.arange(len(df['Estimate'])))
ax.set_yticklabels(df.iloc[:,0].tolist(), fontsize=10)

ax.grid(axis='x', linestyle='--', alpha=0.7)
# ax.legend()
fig.tight_layout()

# Save the plot
fig.savefig('logistic_regression_ci.png', dpi=300, bbox_inches='tight')