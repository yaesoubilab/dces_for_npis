

def get_coeff_estimates_and_errs(table_no_vaccine, table_vaccine, reorder_indices):

    # remove ACS2 and SIGMA_PANEL_ASC2 estimates from the results
    results_no_vaccine_filtered = table_no_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])
    results_vaccine_filtered = table_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])

    estimates_no_vaccine = results_no_vaccine_filtered['Value'].loc[reorder_indices]
    errs_no_vaccine = results_no_vaccine_filtered['Std err'].loc[reorder_indices] * 1.96

    estimates_vaccine = results_vaccine_filtered['Value'].loc[reorder_indices]
    errs_vaccine = results_vaccine_filtered['Std err'].loc[reorder_indices] * 1.96

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_vaccine


def get_wtas_cis(table_no_vaccine, table_vaccine, reorder_indices):

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
    estimates_no_vaccine = results_no_vaccine_filtered['WTP_mean'].loc[reorder_indices]
    errs_no_vaccine = [
        estimates_no_vaccine - results_no_vaccine_filtered['WTP_CI_lower'].loc[reorder_indices],
        results_no_vaccine_filtered['WTP_CI_upper'].loc[reorder_indices] - estimates_no_vaccine
    ]

    estimates_vaccine = results_vaccine_filtered['WTP_mean'].loc[reorder_indices]
    errs_wtp_vaccine = [
        estimates_vaccine - results_vaccine_filtered['WTP_CI_lower'].loc[reorder_indices],
        results_vaccine_filtered['WTP_CI_upper'].loc[reorder_indices] - estimates_vaccine
    ]

    return estimates_no_vaccine, errs_no_vaccine, estimates_vaccine, errs_wtp_vaccine

