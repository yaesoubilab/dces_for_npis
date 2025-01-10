import numpy as np
import pandas as pd


def get_table(file_path, if_drop_infection_rate):
    """ Read the table from the file path and drop the unnecessary rows """

    table = pd.read_csv(file_path, index_col=0)
    if if_drop_infection_rate:
        table = table.drop(['ACS2', 'SIGMA_PANEL_ASC2', 'Number_of_infections'])
    else:
        table = table.drop(['ACS2', 'SIGMA_PANEL_ASC2'])

    return  table


def get_coefs_and_errs(table, attribute_keys):
    """ Get coefficient estimates and errors """

    estimates = table['Value'].loc[attribute_keys]
    errs = table['Std err'].loc[attribute_keys] * 1.96

    return estimates, errs


def get_wtas_and_errs(table, attribute_keys, num_infection_suffix):
    """ Get WTA estimates and errors """

    infection_coeff = table['Value'].loc['Number_of_infections'+num_infection_suffix]

    # get wtp estimates and errors
    wtas = table['WTP_mean'].loc[attribute_keys]*100
    errs = [
        wtas - table['WTP_CI_lower'].loc[attribute_keys]*100,
        table['WTP_CI_upper'].loc[attribute_keys]*100 - wtas]

    for i in range(len(wtas)):
        if infection_coeff < 0:
            if wtas.iloc[i] < 0:
                errs[0].iloc[i] = 0
                upper = wtas.iloc[i] + errs[1].iloc[i]
                errs[1].iloc[i] = max(0, upper)
                wtas.iloc[i] = 0
            else:
                if wtas.iloc[i] > 200:
                    wtas.iloc[i] = np.inf
                    errs[0].iloc[i] = 0
                    errs[1].iloc[i] = 0
                else:
                    lower = wtas.iloc[i] - errs[0].iloc[i]
                    errs[0].iloc[i] = wtas.iloc[i] - max(0, lower)
        elif infection_coeff >= 0:
            # if wtas.iloc[i] > 0:
            #     lower = wtas.iloc[i] - errs[0].iloc[i]
            #     errs[0].iloc[i] = wtas.iloc[i] - max(0, lower)
            # else:
            wtas.iloc[i] = np.inf
            errs[0].iloc[i] = 0
            errs[1].iloc[i] = 0

    return wtas, errs


def update_table_to_include_all_subgroups(table, subgroup_categories):
    """ Update the table to include all subgroups """

    table.index = [idx if any(item in idx for item in subgroup_categories)
                   else idx+'_'+subgroup_categories[0] for idx in table.index]

    return table


def get_dict_estimates_and_errs_by_subgroups(
        survey_scenario, subgroup_name, subgroup_categories, attribute_keys, estimate_type):
    """ Get coefficient estimates and errors for subgroups
    : param survey_scenario: (string) 'vaccine' or 'no vaccine'
    : param subgroup_name: (string) name of the subgroup (gender, race, etc.)
    : param subgroup_categories: (list) list of subgroup categories (['Male', 'Female'])
    : param attribute_keys: (list) list of attribute keys
    : param estimate_type: (string) 'coeff' or 'wta'
    """

    if survey_scenario == 'no vaccine':
        table = get_table(
            'estimates/results_{}_no_vaccine.csv'.format(subgroup_name), if_drop_infection_rate=False)
    elif survey_scenario == 'vaccine':
        table = get_table(
            'estimates/results_{}_vaccine.csv'.format(subgroup_name), if_drop_infection_rate=False)
    else:
        raise ValueError('Invalid survey scenario')

    # dictionaries
    estimates, errs = {}, {}

    # update the table to include all subgroups
    if subgroup_categories is not None:
        table = update_table_to_include_all_subgroups(table, subgroup_categories)

        for group in subgroup_categories:

            table_filtered = table[table.index.str.contains(group)]

            # update attribute keys by adding the group name
            group_attribute_keys = [key + '_' + group for key in attribute_keys]

            # estimates and err
            if estimate_type == 'coeff':
                estimates[group], errs[group] = get_coefs_and_errs(
                    table=table_filtered, attribute_keys=group_attribute_keys)
            elif estimate_type == 'wta':
                estimates[group], errs[group]= get_wtas_and_errs(
                    table=table_filtered, attribute_keys=group_attribute_keys,
                    num_infection_suffix='_{}'.format(group))
            else:
                raise ValueError('Invalid estimate type.')

    else:
        # estimates and err and put them in a dictionary
        if estimate_type == 'coeff':
            estimates['average_pop'], errs['average_pop'] = get_coefs_and_errs(
                table=table, attribute_keys=attribute_keys)
        elif estimate_type == 'wta':
            estimates['average_pop'], errs['average_pop'] = get_wtas_and_errs(
                table=table, attribute_keys=attribute_keys, num_infection_suffix='')
        else:
            raise ValueError('Invalid estimate type.')

    return estimates, errs
