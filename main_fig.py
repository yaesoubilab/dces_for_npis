import matplotlib.pyplot as plt

from defenisions import *
from support.fig_support import add_to_2_axes
from support.func_support import get_wtas_and_errs, get_table, get_coefs_and_errs

FIG_SIZE = (10, 6)

def do_main_figure():

    # read results for vaccine and no vaccine scenarios
    results_no_vaccine = get_table(
        file_path='estimates/results_drop_first_level_no_vaccine_WTP.csv',
        if_drop_infection_rate=False)
    results_vaccine = get_table(
        file_path='estimates/results_drop_first_level_vaccine_WTP.csv',
        if_drop_infection_rate=False)

    # read coefficient estimates along with confidence intervals
    coefs_no_vaccine, errs_no_vaccine = get_coefs_and_errs(
        table=results_no_vaccine,
        attribute_keys=DICT_COEFF_LABELS.keys())
    coefs_vaccine, errs_vaccine = get_coefs_and_errs(
        table=results_vaccine,
        attribute_keys=DICT_COEFF_LABELS.keys())

    # read wta estimates along with confidence intervals
    wtp_vaccine, wtp_errs_vaccine = get_wtas_and_errs(
        table=results_vaccine,
        attribute_keys=DICT_WTA_LABELS.keys())
    wtp_no_vaccine, wtp_errs_no_vaccine = get_wtas_and_errs(
        table=results_no_vaccine,
        attribute_keys=DICT_WTA_LABELS.keys())

    # plot
    fig, ax = plt.subplots(1, 2, figsize=FIG_SIZE, sharey=True)
    ax[0].set_title('A)', loc='left', weight='bold')
    ax[1].set_title('B)', loc='left', weight='bold')

    # plot coefficient and wta estimates side by side
    add_to_2_axes(
        axes=ax,
        lists_of_estimates_left=[coefs_no_vaccine, coefs_vaccine],
        lists_of_errs_left=[errs_no_vaccine, errs_vaccine],
        lists_of_estimates_right=[wtp_no_vaccine, wtp_vaccine],
        lists_of_errs_right=[wtp_errs_no_vaccine, wtp_errs_vaccine],
        x_axis_label_left='Coefficient Estimates',
        x_axis_label_right='Willingness To Accept (WTA)',
        x_axis_range_left=COEFF_X_RANGE,
        x_axis_range_right=WTA_X_RANGE,
        colors=['#2C5784', '#D9534F'],
        labels=['No Vaccine', 'Vaccine'],
        y_axis_labels=DICT_COEFF_LABELS.values(),
        legend_loc='upper right',
        distance_between_bars=0.2
    )

    fig.tight_layout(w_pad=3)
    fig.savefig('figs/coeff_and_wta.png')


if __name__ == '__main__':
    do_main_figure()
