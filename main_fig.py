import matplotlib.pyplot as plt
import pandas as pd

from defenisions import *
from fig_support import add_to_ax
from func_support import get_coeff_estimates_and_errs, get_wtas_cis

FIG_SIZE = (10, 6)
WTP_X_RANGE = (-200, 200)
MARKER_SIZE = 7
INCLUDE_VACCINE = True


# read results for vaccine and no vaccine scnearios
results_no_vaccine = pd.read_csv('estimates/results_drop_first_level_no_vaccine_WTP.csv', index_col= 0)
results_vaccine = pd.read_csv('estimates/results_drop_first_level_vaccine_WTP.csv', index_col= 0)

# read coefficient estimates along with confidence intervals
coefs_no_vaccine, errs_no_vaccine, coefs_vaccine, errs_coefs_vaccine = get_coeff_estimates_and_errs(
    table_no_vaccine=results_no_vaccine,
    table_vaccine=results_vaccine,
    reorder_indices=reorder_indices_coeff)

# read wta estimates along with confidence intervals
wtp_vaccine, wtp_errs_vaccine, wtp_no_vaccine, wtp_errs_no_vaccine = get_wtas_cis(
    table_no_vaccine=results_no_vaccine,
    table_vaccine=results_vaccine,
    reorder_indices=reorder_indices_wtp)

# plot
fig, ax= plt.subplots(1, 2, figsize=FIG_SIZE, sharey=True)
ax[0].set_title('A)', loc='left', weight='bold')
ax[1].set_title('B)', loc='left', weight='bold')

# plot coefficients
add_to_ax(ax=ax[0],
          lists_of_estimates=[coefs_no_vaccine, coefs_vaccine],
          lists_of_ci=[errs_no_vaccine, errs_coefs_vaccine],
          y_axis_labels=coef_labels,
          x_axis_label='Coefficient Estimates',
          colors=['#2C5784', '#D9534F'],
          labels=['No Vaccine', 'Vaccine'],
          legend_loc='upper right',
          distance_between_bars=0.3)

add_to_ax(ax=ax[1],
          lists_of_estimates=[wtp_no_vaccine, wtp_vaccine],
          lists_of_ci=[wtp_errs_no_vaccine, wtp_errs_vaccine],
          x_axis_label='Willingness To Accept (WTA)',
          colors=['#2C5784', '#D9534F'],
          labels=['No Vaccine', 'Vaccine'],
          legend_loc='upper left',
          distance_between_bars=0.3)


plt.tight_layout(w_pad=3)
plt.savefig('figs/coeffs_and_wta.png')
# plt.show()