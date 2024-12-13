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
        table_no_vaccine, table_vaccine, attribute_keys, estimate_type, subgroups):
    """ Get coefficient estimates and errors for subgroups """

    # dictionaries
    estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine = {}, {}, {}, {}
    table_no_vaccine_filtered = None
    table_vaccine_filtered = None

    for group in subgroups:

        if table_no_vaccine is not None:
            table_no_vaccine_filtered = table_no_vaccine[table_no_vaccine.index.str.contains(group)]
        if table_vaccine is not None:
            table_vaccine_filtered = table_vaccine[table_vaccine.index.str.contains(group)]

        # update attribute keys by adding the group name
        group_attribute_keys = [key + '_' + group for key in attribute_keys]

        # estimates and err
        if estimate_type == 'coeff':
            if table_no_vaccine is not None:
                estimates_no_vaccine[group], errs_no_vaccine[group] = get_coefs_and_errs(
                    table=table_no_vaccine_filtered, attribute_keys=group_attribute_keys)
            if table_vaccine is not None:
                estimates_vaccine[group], errs_vaccine[group] = get_coefs_and_errs(
                    table=table_vaccine_filtered, attribute_keys=group_attribute_keys)
        elif estimate_type == 'wta':
            if table_no_vaccine is not None:
                estimates_no_vaccine[group], errs_no_vaccine[group]= get_wtas_and_errs(
                    table=table_no_vaccine_filtered, attribute_keys=group_attribute_keys)
            if table_vaccine is not None:
                estimates_vaccine[group], errs_vaccine[group] = get_wtas_and_errs(
                    table=table_vaccine_filtered, attribute_keys=group_attribute_keys)
        else:
            raise ValueError('Invalid estimate type.')

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine



def get_estims_errs_by_subgroup(survey_scenario, group_name, estimate_type):


    # read results for vaccine and no vaccine scenarios
    results_no_vaccine = get_table(
        'estimates/results_{}_no_vaccine.csv'.format(group_name), if_drop_infection_rate=False)
    results_vaccine =  get_table(
        'estimates/results_{}_vaccine.csv'.format(group_name), if_drop_infection_rate=False)

    if estimate_type == 'coeff':
        # read coefficient estimates along with confidence intervals
        estims_no_vaccine, errs_no_vaccine, estims_vaccine, errs_coefs_vaccine = get_dict_estimates_and_errs_by_subgroups(
            table_no_vaccine=results_no_vaccine,
            table_vaccine=results_vaccine,
            attribute_keys=dict_coeff_labels.keys(),
            subgroups=group_categories, estimate_type='coeff')

    elif estimate_type == 'wta':
        # read wtp estimates along with confidence intervals
        estims_no_vaccine, errs_no_vaccine, estims_vaccine, errs_coefs_vaccine = get_dict_estimates_and_errs_by_subgroups(
            table_no_vaccine=results_no_vaccine,
            table_vaccine=results_vaccine,
            attribute_keys=dict_wtp_labels.keys(),
            subgroups=group_categories, estimate_type='wta')
    else:
        raise ValueError('Invalid estimate type')