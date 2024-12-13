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


def get_wtas_and_errs(table, attribute_keys):
    """ Get WTA estimates and errors """

    # get wtp estimates and errors
    wtas = table['WTP_mean'].loc[attribute_keys]*100
    errs = [
        wtas - table['WTP_CI_lower'].loc[attribute_keys]*100,
        table['WTP_CI_upper'].loc[attribute_keys]*100 - wtas]

    return wtas, errs


def get_dict_estimates_and_errs_by_subgroups(
        survey_scenario, subgroup_name, subgroup_categories, attribute_keys, estimate_type):
    """ Get coefficient estimates and errors for subgroups
    : param survey_scenario: (string) 'vaccine' or 'no vaccine'
    : param subgroup_name: (string) name of the subgroup
    : param subgroup_categories: (list) list of subgroup categories
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
                table=table_filtered, attribute_keys=group_attribute_keys)
        else:
            raise ValueError('Invalid estimate type.')

    return estimates, errs
