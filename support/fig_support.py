import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from defenisions import *
from support.func_support import get_dict_coefs_and_errs_by_subgroups


def add_to_ax(ax,
              lists_of_estimates,
              lists_of_errs,
              x_axis_label,
              colors, labels,
              y_axis_labels=None,
              title=None,
              legend_loc='upper right',
              distance_between_bars=None, ):

    # number of lists
    n = len(lists_of_estimates)

    if distance_between_bars is None:
        diffs = [0]*n
    else:
        diffs = np.linspace(start=-distance_between_bars/2,
                            stop=distance_between_bars/2, num=n)

    for i, this_list in enumerate(lists_of_estimates):
        ax.errorbar(this_list,
                    np.arange(len(this_list)) + diffs[i],
                    xerr=lists_of_errs[i],
                    fmt='o', color=colors[i], ecolor=colors[i], capsize=0, alpha=0.7,
                    label=labels[i])

    ax.set_xlabel(x_axis_label, fontsize=12)
    if y_axis_labels is not None:
        ax.set_yticks(np.arange(len(y_axis_labels)))
        ax.set_yticklabels(y_axis_labels, fontsize=10)

    ax.axvline(x=0, color='black', linestyle='-', linewidth=1.3)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(loc=legend_loc, fontsize=10)
    ax.set_title(title, fontsize=14)


def add_to_2_axes(axes,
                  lists_of_estimates_left,
                  lists_of_errs_left,
                  lists_of_estimates_right,
                  lists_of_errs_right,
                  x_axis_label_left,
                  x_axis_label_right,
                  colors, labels,
                  y_axis_labels=None,
                  title_left=None,
                  title_right=None,
                  legend_loc='upper right',
                  distance_between_bars=None):

    # add left
    add_to_ax(ax=axes[0],
              lists_of_estimates=lists_of_estimates_left,
              lists_of_errs=lists_of_errs_left,
              title=title_left,
              x_axis_label=x_axis_label_left,
              colors=colors,
              labels=labels,
              y_axis_labels=y_axis_labels,
              distance_between_bars=distance_between_bars)

    # add right
    add_to_ax(ax=axes[1],
              lists_of_estimates=lists_of_estimates_right,
              lists_of_errs=lists_of_errs_right,
              title=title_right,
              x_axis_label=x_axis_label_right,
              colors=colors,
              labels=labels,
              legend_loc=legend_loc,
              distance_between_bars=distance_between_bars)


def do_coeffs_by_group(group_name, group_categories, group_colors, distance_between_bars=0.3, figsize=(10,6)):

    # read results for vaccine and no vaccine scenarios
    results_no_vaccine = pd.read_csv(
        'estimates/results_{}_no_vaccine.csv'.format(group_name), index_col=0)
    results_vaccine = pd.read_csv(
        'estimates/results_{}_vaccine.csv'.format(group_name), index_col=0)

    # read coefficient estimates along with confidence intervals
    coefs_no_vaccine, errs_no_vaccine, coefs_vaccine, errs_coefs_vaccine = get_dict_coefs_and_errs_by_subgroups(
        table_no_vaccine=results_no_vaccine,
        table_vaccine=results_vaccine,
        attribute_keys=dict_coeff_labels.keys(),
        subgroups=group_categories)

    # plot
    fig, ax = plt.subplots(1, 2, figsize=figsize, sharey=True)
    ax[0].set_title('A)', loc='left', weight='bold')
    ax[1].set_title('B)', loc='left', weight='bold')

    # plot coefficient and wta estimates side by side
    add_to_2_axes(
        axes=ax,
        lists_of_estimates_left=list(coefs_no_vaccine.values()),
        lists_of_errs_left=list(errs_no_vaccine.values()),
        lists_of_estimates_right=list(coefs_vaccine.values()),
        lists_of_errs_right=list(errs_coefs_vaccine.values()),
        title_left = 'Vaccine Not Available',
        title_right = 'Vaccine Available',
        x_axis_label_left='Coefficient Estimates',
        x_axis_label_right='Coefficient Estimates',
        colors=group_colors,
        labels=group_categories,
        y_axis_labels=dict_coeff_labels.values(),
        legend_loc='upper right',
        distance_between_bars=distance_between_bars
    )

    plt.tight_layout(w_pad=3)
    plt.savefig('figs/coeffs_by_{}.png'.format(group_name))
