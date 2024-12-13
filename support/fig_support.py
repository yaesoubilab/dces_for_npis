import matplotlib.pyplot as plt
import numpy as np

from defenisions import *
from support.func_support import get_dict_estimates_and_errs_by_subgroups


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


def do_fig_by_group(
        estimate_type, group_name, group_categories, group_colors,
        distance_between_bars=0.3, fig_size=(10, 6)):
    """
    :param estimate_type: (string) 'coeffs' or 'wtas'
    :param group_name:
    :param group_categories:
    :param group_colors:
    :param distance_between_bars:
    :param fig_size:
    :return:
    """

    # get estimates and errors
    estims_no_vaccine, errs_no_vaccine = get_dict_estimates_and_errs_by_subgroups(
        survey_scenario='no vaccine',
        group_name=group_name,
        attribute_keys=dict_coeff_labels.keys(),
        subgroups=group_categories, estimate_type=estimate_type)

    estims_vaccine, errs_coefs_vaccine = get_dict_estimates_and_errs_by_subgroups(
        survey_scenario='vaccine',
        group_name=group_name,
        attribute_keys=dict_coeff_labels.keys(),
        subgroups=group_categories, estimate_type=estimate_type)

    # plot
    fig, ax = plt.subplots(1, 2, figsize=fig_size, sharey=True)
    ax[0].set_title('A)', loc='left', weight='bold')
    ax[1].set_title('B)', loc='left', weight='bold')

    x_axis_label = 'Coefficient Estimates' if estimate_type == 'coeff' else 'Willingness To Accept (WTA)'
    # plot coefficient and wta estimates side by side
    add_to_2_axes(
        axes=ax,
        lists_of_estimates_left=list(estims_no_vaccine.values()),
        lists_of_errs_left=list(errs_no_vaccine.values()),
        lists_of_estimates_right=list(estims_vaccine.values()),
        lists_of_errs_right=list(errs_coefs_vaccine.values()),
        title_left = 'Vaccine Not Available',
        title_right = 'Vaccine Available',
        x_axis_label_left=x_axis_label,
        x_axis_label_right=x_axis_label,
        colors=group_colors,
        labels=group_categories,
        y_axis_labels=dict_coeff_labels.values(),
        legend_loc='upper right',
        distance_between_bars=distance_between_bars
    )

    plt.tight_layout(w_pad=3)
    plt.savefig('figs/{}_by_{}.png'.format(estimate_type, group_name))

#
# def do_row_of_subgroups(estimate_type, survey_scenario, subgroup_info, fig_size):
#
#     n_of_panels = len(subgroup_info)
#     fig, ax = plt.subplots(1, n_of_panels, figsize=fig_size, sharey=True)
#
#     # populate panels
#     for i in range(n_of_panels):
#         ax[i].set_title('{})'.format(string.ascii_uppercase[i]), loc='left', weight='bold')
#
#
#     for subgroup in subgroup_info:
#
#         add_to_ax(
#             ax=ax[i],
#             lists_of_estimates=subgroup_info[i],
#             lists_of_errs=subgroup_info[i],
#             x_axis_label='Coefficient Estimates',
#             colors=)
