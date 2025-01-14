import pandas as pd

from defenisions import ROOT_DIR

# read the data into table
data = pd.read_csv(ROOT_DIR+'/lca_individuals/results_LCA_no_vaccine_class_probabilities_and_characters.csv')

# for all columns, print the unique values
for column in data.columns[~data.columns.isin(['ID', 'prob_0','prob_1', 'Class_0', 'Class_1'])]:
    print(column, data[column].unique())
