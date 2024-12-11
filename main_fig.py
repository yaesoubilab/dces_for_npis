import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from fig_support import add_to_ax

FIG_SIZE = (10, 5)
WTP_X_RANGE = (-200, 200)
MARKER_SIZE = 7
INCLUDE_VACCINE = True


results_no_vaccine = pd.read_csv('estimates/results_drop_first_level_no_vaccine_WTP.csv', index_col= 0)
results_vaccine = pd.read_csv('estimates/results_drop_first_level_vaccine_WTP.csv', index_col= 0)

results_vaccine['WTP_CI_lower'] = results_vaccine['WTP_CI_lower']*100
results_vaccine['WTP_CI_upper'] = results_vaccine['WTP_CI_upper']*100
results_no_vaccine['WTP_CI_lower'] = results_no_vaccine['WTP_CI_lower']*100

results_no_vaccine['WTP_CI_upper'] = results_no_vaccine['WTP_CI_upper']*100
results_vaccine['WTP_mean'] = results_vaccine['WTP_mean']*100
results_no_vaccine['WTP_mean'] = results_no_vaccine['WTP_mean']*100

coef_labels = ["Crowded indoor venues closed",
              "Non-essential businesses close",
              "Masks required only in schools",
              "Masks required in public",
              "Masks required in all indoor spaces",
              "High schools close with remote learning",
              "High schools close, no remote learning",
              "All schools close with remote learning",
              "All schools close, no remote learning",
              "50% reduction in transit capacity",
              "Restricted primary care",
               "Restricted primary and optional care",
               "Number of infections"]
wta_labels = ["Crowded indoor venues closed",
             "Non-essential businesses close",
             "Masks required only in schools",
             "Masks required in public",
             "Masks required in all indoor spaces",
             "High schools close with remote learning",
             "High schools close, no remote learning",
             "All schools close with remote learning",
             "All schools close, no remote learning",
             "50% reduction in transit capacity",
             "", "", ""]

reorder_indices = [
    'Business_closures_2',
    'Business_closures_3',
    'Mask_mandates_2',
    'Mask_mandates_3',
    'Mask_mandates_4',
    'School_closures_2',
    'School_closures_3',
    'School_closures_4',
    'School_closures_5',
    'Transit_2',
    'Healthcare_restrictions_2',
    'Healthcare_restrictions_3',
    'Number_of_infections'
]


results_no_vaccine_filtered = results_no_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])
results_vaccine_filtered = results_vaccine.drop(['ACS2', 'SIGMA_PANEL_ASC2'])
# Indices and Labels

remove_indices_general = ['Number_of_infections'] # 'Healthcare_restrictions_2', 'Healthcare_restrictions_3'

# Replace values at 'remove_indices' with np.nan

results_no_vaccine_filtered.loc[remove_indices_general, ['WTP_mean', 'WTP_CI_lower', 'WTP_CI_upper']] = np.nan
results_vaccine_filtered.loc[remove_indices_general, ['WTP_mean', 'WTP_CI_lower', 'WTP_CI_upper']] = np.nan

coefficients_no_vaccine = results_no_vaccine_filtered['Value'].loc[reorder_indices]
ci_coefficients_no_vaccine = results_no_vaccine_filtered['Std err'].loc[reorder_indices] * 1.96

coefficients_vaccine = results_vaccine_filtered['Value'].loc[reorder_indices]
ci_coefficients_vaccine = results_vaccine_filtered['Std err'].loc[reorder_indices] * 1.96

# Process WTP data with np.nan values
filtered_wtp_no_vaccine = results_no_vaccine_filtered['WTP_mean'].loc[reorder_indices]
ci_wtp_no_vaccine = [
    filtered_wtp_no_vaccine - results_no_vaccine_filtered['WTP_CI_lower'].loc[reorder_indices],
    results_no_vaccine_filtered['WTP_CI_upper'].loc[reorder_indices] - filtered_wtp_no_vaccine
]

filtered_wtp_vaccine = results_vaccine_filtered['WTP_mean'].loc[reorder_indices]
ci_wtp_vaccine = [
    filtered_wtp_vaccine - results_vaccine_filtered['WTP_CI_lower'].loc[reorder_indices],
    results_vaccine_filtered['WTP_CI_upper'].loc[reorder_indices] - filtered_wtp_vaccine
]

# Plotting setup as before
fig, ax= plt.subplots(1, 2, figsize=FIG_SIZE, sharey=True)
ax[0].set_title('A)', loc='left')
ax[1].set_title('B)', loc='left')

# plot coefficients
add_to_ax(ax=ax[0],
          lists_of_estimates=[coefficients_no_vaccine, coefficients_vaccine],
          lists_of_ci=[ci_coefficients_no_vaccine, ci_coefficients_vaccine],
          y_axis_labels=coef_labels,
          x_axis_label='Coefficient Estimates',
          colors=['#2C5784', '#D9534F'],
          labels=['No Vaccine', 'Vaccine'])

add_to_ax(ax=ax[1],
          lists_of_estimates=[filtered_wtp_no_vaccine, filtered_wtp_vaccine],
          lists_of_ci=[ci_wtp_no_vaccine, ci_wtp_vaccine],
          x_axis_label='Willingness To Accept (WTA)',
          colors=['#2C5784', '#D9534F'],
          labels=['No Vaccine', 'Vaccine'])


plt.tight_layout(w_pad=3)

plt.savefig('coefficients_WTP_all_both_no_and_with_vaccine_flipped_Reza_presentation.png')
plt.show()