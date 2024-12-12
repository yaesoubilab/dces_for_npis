def get_coefs_and_errs(table_no_vaccine, table_vaccine, attribute_keys):

    # remove ACS2 and SIGMA_PANEL_ASC2 estimates from the results
    results_no_vaccine_filtered = table_no_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])
    results_vaccine_filtered = table_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])

    estimates_no_vaccine = results_no_vaccine_filtered['Value'].loc[attribute_keys]
    errs_no_vaccine = results_no_vaccine_filtered['Std err'].loc[attribute_keys] * 1.96

    estimates_vaccine = results_vaccine_filtered['Value'].loc[attribute_keys]
    errs_vaccine = results_vaccine_filtered['Std err'].loc[attribute_keys] * 1.96

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine


def get_dict_coefs_and_errs_by_subgroups(table_no_vaccine, table_vaccine, attribute_keys, subgroups):

    # remove ACS2 and SIGMA_PANEL_ASC2 estimates from the results
    table_no_vaccine = table_no_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])
    table_vaccine = table_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])

    # dictionaries
    estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine = {}, {}, {}, {}

    for group in subgroups:

        table_no_vaccine_filtered = table_no_vaccine[table_no_vaccine.index.str.contains(group)]
        table_vaccine_filtered = table_vaccine[table_vaccine.index.str.contains(group)]

        # update attribute keys by adding the group name
        group_attribute_keys = [key + '_' + group for key in attribute_keys]

        estimates_no_vaccine[group] = table_no_vaccine_filtered['Value'].loc[group_attribute_keys]
        errs_no_vaccine[group] = table_no_vaccine_filtered['Std err'].loc[group_attribute_keys] * 1.96

        estimates_vaccine[group] = table_vaccine_filtered['Value'].loc[group_attribute_keys]
        errs_vaccine[group] = table_vaccine_filtered['Std err'].loc[group_attribute_keys] * 1.96

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine


def get_wtas_and_errs(table_no_vaccine, table_vaccine, attribute_keys):

    # multiply WTA by 100 to get per 100 population
    for results in [table_no_vaccine, table_vaccine]:
        results['WTP_mean'] = results['WTP_mean'] * 100
        results['WTP_CI_lower'] = results['WTP_CI_lower']*100
        results['WTP_CI_upper'] = results['WTP_CI_upper']*100

    # remove ACS2 and SIGMA_PANEL_ASC2 estimates from the results
    # and number of infections since WTA is not defined for it
    results_no_vaccine_filtered = table_no_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2', 'Number_of_infections'])
    results_vaccine_filtered = table_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2', 'Number_of_infections'])

    # get wtp estimates and errors
    estimates_no_vaccine = results_no_vaccine_filtered['WTP_mean'].loc[attribute_keys]
    errs_no_vaccine = [
        estimates_no_vaccine - results_no_vaccine_filtered['WTP_CI_lower'].loc[attribute_keys],
        results_no_vaccine_filtered['WTP_CI_upper'].loc[attribute_keys] - estimates_no_vaccine
    ]

    estimates_vaccine = results_vaccine_filtered['WTP_mean'].loc[attribute_keys]
    errs_wtp_vaccine = [
        estimates_vaccine - results_vaccine_filtered['WTP_CI_lower'].loc[attribute_keys],
        results_vaccine_filtered['WTP_CI_upper'].loc[attribute_keys] - estimates_vaccine
    ]

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_wtp_vaccine

