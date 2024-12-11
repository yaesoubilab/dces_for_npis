import numpy as np

def get_wtas_cis(table_no_vaccine, table_vaccine, reorder_indices):

    # multiply WTA by 100 to get per 100 population
    for results in [table_no_vaccine, table_vaccine]:
        results['WTP_mean'] = results['WTP_mean'] * 100
        results['WTP_CI_lower'] = results['WTP_CI_lower']*100
        results['WTP_CI_upper'] = results['WTP_CI_upper']*100

    # remove ACS2 and SIGMA_PANEL_ASC2 estimates from the results
    results_no_vaccine_filtered = table_no_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])
    results_vaccine_filtered = table_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])

    # WTA estimate is  not defined for number of infections
    remove_indices_general = ['Number_of_infections'] # 'Healthcare_restrictions_2', 'Healthcare_restrictions_3'
    results_no_vaccine_filtered.loc[
        remove_indices_general, ['WTP_mean', 'WTP_CI_lower', 'WTP_CI_upper']] = np.nan
    results_vaccine_filtered.loc[
        remove_indices_general, ['WTP_mean', 'WTP_CI_lower', 'WTP_CI_upper']] = np.nan

    # Process WTP data with np.nan values
    filtered_wtp_no_vaccine = results_no_vaccine_filtered['WTP_mean'].loc[reorder_indices]
    ci_wtp_no_vaccine = [
        filtered_wtp_no_vaccine - results_no_vaccine_filtered['WTP_CI_lower'].loc[reorder_indices],
        results_no_vaccine_filtered['WTP_CI_upper'].loc[reorder_indices] - filtered_wtp_no_vaccine
    ]

    filtered_wtp_vaccine = results_vaccine_filtered['WTP_mean'].loc[reorder_indices]
    ci_wtp_vaccine = [
        filtered_wtp_vaccine - results_vaccine_filtered['WTP_CI_lower'].loc[reorder_indices]]

    return filtered_wtp_no_vaccine, ci_wtp_no_vaccine, filtered_wtp_vaccine, ci_wtp_vaccine


def get_coeff_estimates_and_cis(table_no_vaccine, table_vaccine, reorder_indices):

    # remove ACS2 and SIGMA_PANEL_ASC2 estimates from the results
    results_no_vaccine_filtered = table_no_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])
    results_vaccine_filtered = table_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])

    coefs_no_vaccine = results_no_vaccine_filtered['Value'].loc[reorder_indices]
    ci_coefs_no_vaccine = results_no_vaccine_filtered['Std err'].loc[reorder_indices] * 1.96

    coefs_vaccine = results_vaccine_filtered['Value'].loc[reorder_indices]
    ci_coefs_vaccine = results_vaccine_filtered['Std err'].loc[reorder_indices] * 1.96

    return coefs_no_vaccine, ci_coefs_no_vaccine, coefs_vaccine, ci_coefs_vaccine