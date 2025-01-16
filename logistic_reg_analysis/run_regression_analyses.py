import pandas as pd

from analysis_support import do_logistic_regression
from defenisions import ROOT_DIR, DICT_VARIABLES
from fig_support import do_correlation_analysis, plot_logistic_regression_coeffs

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

def run_logistic_regression_analysis(vaccine_scenario):

    variable_labels = list(DICT_VARIABLES.keys())
    y_label = ['Class_1']

    # read the data into table
    data = pd.read_csv(
        ROOT_DIR+'/lca_individuals/results_LCA_{}_class_probabilities_and_characters.csv'.format(vaccine_scenario))

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

    # find the list of encoded variable names
    labels_of_coded_variables = []
    for var, var_details in DICT_VARIABLES.items():
        labels_of_coded_variables += [var+'_'+label for label in var_details['values'][1:]]

    # read the coded columns
    X = data_encoded[labels_of_coded_variables]

    X = X.astype('float64')

    y = data_encoded[y_label]

    # do correlation analysis
    do_correlation_analysis(X=X, vaccine_scenario=vaccine_scenario)

    # do logistic regression
    do_logistic_regression(X=X, y=y, vaccine_scenario=vaccine_scenario)

    # plot logistic regression coefficients
    plot_logistic_regression_coeffs(fig_size=(6, 11), vaccine_scenario=vaccine_scenario)


if __name__ == '__main__':
    run_logistic_regression_analysis(vaccine_scenario='no_vaccine')
    run_logistic_regression_analysis(vaccine_scenario='vaccine')