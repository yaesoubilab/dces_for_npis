import pandas as pd
import statsmodels.api as sm

from defenisions import ROOT_DIR

variable_labels = ['Gender', 'Child', 'Hispanic', 'Age']
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
X = data_encoded[['Gender_Male', 'Gender_Other', 'Child_Yes', 'Hispanic_Yes', 'Age_≥ 65']]
y = data_encoded[y_label]

print(X.dtypes)
print(y.dtypes)

# fit the model
model = sm.Logit(y, X)
results = model.fit()

# Display the model summary (coefficients and confidence intervals)
print(results.summary())
# export results to csv
results.summary2().tables[1].to_csv('test.csv')
