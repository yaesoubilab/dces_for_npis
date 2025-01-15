import pandas as pd

from defenisions import ROOT_DIR


def print_unique_column_values(vaccine_scenario):

    print('\n--- Vaccine scenario: {} ---\n'.format(vaccine_scenario))

    # read the data into table
    data = pd.read_csv(
        ROOT_DIR+'/lca_individuals/results_LCA_{}_class_probabilities_and_characters.csv'.format(vaccine_scenario))

    # for all columns, print the unique values
    for column in data.columns[~data.columns.isin(['ID', 'prob_0','prob_1', 'Class_0', 'Class_1'])]:
        print(column, data[column].unique())


if __name__ == '__main__':
    print_unique_column_values('no_vaccine')
    print_unique_column_values('vaccine')
