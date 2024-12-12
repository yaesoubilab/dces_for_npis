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


def get_coefs_and_errs_by_vaccine(table_no_vaccine, table_vaccine, attribute_keys):
    """ Get coefficient estimates and errors for no vaccine and with vaccine scenarios """

    # get coefficient estimates and errors for no vaccine scenario
    estimates_no_vaccine, errs_no_vaccine = get_coefs_and_errs(
        table=table_no_vaccine, attribute_keys= attribute_keys)

    # get coefficient estimates and errors for with vaccine scenario
    estimates_vaccine, errs_vaccine = get_coefs_and_errs(
        table=table_vaccine, attribute_keys=attribute_keys)

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine


def get_dict_estimates_and_errs_by_subgroups(
        table_no_vaccine, table_vaccine, attribute_keys, estimate_type, subgroups):
    """ Get coefficient estimates and errors for subgroups """

    # dictionaries
    estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine = {}, {}, {}, {}

    for group in subgroups:

        table_no_vaccine_filtered = table_no_vaccine[table_no_vaccine.index.str.contains(group)]
        table_vaccine_filtered = table_vaccine[table_vaccine.index.str.contains(group)]

        # update attribute keys by adding the group name
        group_attribute_keys = [key + '_' + group for key in attribute_keys]

        # estimates and err
        if estimate_type == 'coeff':
            estimates_no_vaccine[group], errs_no_vaccine[group] = get_coefs_and_errs(
                table=table_no_vaccine_filtered, attribute_keys=group_attribute_keys)
            estimates_vaccine[group], errs_vaccine[group] = get_coefs_and_errs(
                table=table_vaccine_filtered, attribute_keys=group_attribute_keys)
        elif estimate_type == 'wta':
            estimates_no_vaccine[group], errs_no_vaccine[group]= get_wtas_and_errs(
                table=table_no_vaccine_filtered, attribute_keys=group_attribute_keys)
            estimates_vaccine[group], errs_vaccine[group] = get_wtas_and_errs(
                table=table_vaccine_filtered, attribute_keys=group_attribute_keys)
        else:
            raise ValueError('Invalid estimate type.')

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine


def get_wtas_and_errs_by_vaccine(table_no_vaccine, table_vaccine, attribute_keys):
    """ Get WTA estimates and errors for no vaccine and with vaccine scenarios """

    estimates_no_vaccine, errs_no_vaccine = get_wtas_and_errs(
        table=table_no_vaccine, attribute_keys=attribute_keys)
    estimates_vaccine, errs_wtp_vaccine = get_wtas_and_errs(
        table=table_vaccine, attribute_keys=attribute_keys)

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_wtp_vaccine

