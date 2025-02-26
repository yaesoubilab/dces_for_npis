import matplotlib.pyplot as plt

from defenisions import *
from support.fig_support import add_to_ax, add_to_2_axes
from support.func_support import get_wtas_and_errs, get_table, get_coefs_and_errs

FIG_SIZE_1 = (6.5, 5)
FIG_SIZE_2 = (10, 6)

def do_main_vaccine():
    # read results for vaccine and no vaccine scenarios
    results_no_vaccine = get_table(
        file_path='estimates/results_entire_pop_no_vaccine.csv',
        if_drop_infection_rate=False)

    # read coefficient estimates along with confidence intervals
    coefs_no_vaccine, errs_no_vaccine = get_coefs_and_errs(
        table=results_no_vaccine,
        attribute_keys=DICT_COEFF_LABELS.keys())

    # read wta estimates along with confidence intervals
    wtp_no_vaccine, wtp_errs_no_vaccine = get_wtas_and_errs(
        table=results_no_vaccine,
        attribute_keys=DICT_WTA_LABELS.keys(), num_infection_suffix='')

    # add None to the end of each list to make the length of all lists the same
    wtp_no_vaccine.loc[len(wtp_no_vaccine)] = None
    for l in wtp_errs_no_vaccine:
        l.loc[len(l)] = None

    # plot
    fig, ax = plt.subplots(1, 2, figsize=FIG_SIZE_2, sharey=True)
    ax[0].set_title('A)', loc='left', weight='bold')
    ax[1].set_title('B)', loc='left', weight='bold')

    # plot coefficient and wta estimates side by side
    add_to_2_axes(
        axes=ax,
        lists_of_estimates_left=[coefs_no_vaccine],
        lists_of_errs_left=[errs_no_vaccine],
        lists_of_estimates_right=[wtp_no_vaccine],
        lists_of_errs_right=[wtp_errs_no_vaccine],
        x_axis_label_left=COEFF_LABEL,
        x_axis_label_right=WTA_LABEL,
        x_axis_range_left=COEFF_X_RANGE,
        x_axis_range_right=WTA_X_RANGE,
        colors=COLORS,
        legend_labels=[None],
        y_axis_labels=DICT_COEFF_LABELS.values(),
        legend_loc='upper right',
        distance_between_bars=0
    )

    fig.tight_layout(w_pad=3)
    fig.savefig('figs/vaccine_coeff_and_wta.png', dpi=300)


def do_main_coeff_vacine():

    # read results for vaccine and no vaccine scenarios
    results_no_vaccine = get_table(
        file_path='estimates/results_entire_pop_no_vaccine.csv',
        if_drop_infection_rate=False)

    # read coefficient estimates along with confidence intervals
    coefs_no_vaccine, errs_no_vaccine = get_coefs_and_errs(
        table=results_no_vaccine,
        attribute_keys=DICT_COEFF_LABELS.keys())

    # plot
    fig, ax = plt.subplots(1, 1, figsize=FIG_SIZE_1, sharey=True)

    # plot coefficient and wta estimates side by side
    add_to_ax(
        ax=ax,
        lists_of_estimates=[coefs_no_vaccine],
        lists_of_errs=[errs_no_vaccine],
        x_axis_label=COEFF_LABEL,
        colors=[COLORS[0]],
        legend_labels=[None],
        y_axis_labels=DICT_COEFF_LABELS.values(),
        title=None,
        x_axis_range=COEFF_X_RANGE,
        distance_between_bars=None,
        legend_pad=None,
        title_pad=None
    )

    fig.tight_layout(w_pad=3)
    fig.savefig('figs/vaccine_coeff.png', dpi=300)


if __name__ == '__main__':

    do_main_vaccine()
    do_main_coeff_vacine()
