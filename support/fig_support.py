import string

import matplotlib.pyplot as plt
import numpy as np

from defenisions import *
from support.func_support import get_dict_estimates_and_errs_by_subgroups


def add_to_ax(ax,
              lists_of_estimates,
              lists_of_errs,
              x_axis_label,
              colors, legend_labels,
              y_axis_labels=None,
              title=None,
              x_axis_range=None,
              legend_loc='upper right',
              distance_between_bars=None,
              legend_pad=None,
              title_pad=None):

    # number of lists
    n = len(lists_of_estimates)

    if distance_between_bars is None:
        diffs = [0]*n
    else:
        diffs = np.flip(np.linspace(start=-distance_between_bars/2,
                            stop=distance_between_bars/2, num=n))

    for i, this_list in enumerate(lists_of_estimates):
        # plot a series of estimates
        ax.scatter(this_list, np.arange(len(this_list)) + diffs[i],
                marker='o', color=colors[i], label=legend_labels[i])

        ax.errorbar(this_list,
                    np.arange(len(this_list)) + diffs[i],
                    xerr=lists_of_errs[i], fmt='none',
                    ecolor=colors[i], capsize=0, alpha=0.50)

    ax.set_xlabel(x_axis_label, fontsize=10)
    if y_axis_labels is not None:
        ax.set_yticks(np.arange(len(y_axis_labels)))
        ax.set_yticklabels(y_axis_labels, fontsize=10)

    ax.axvline(x=0, color='black', linestyle='-', linewidth=1.3)
    ax.grid(True, linestyle='--', alpha=0.7)

    # add legend to the top of the figure
    if len(legend_labels) > 1:
        ax.legend(loc=legend_loc,
                  bbox_to_anchor=None if legend_pad is None else (0.5, legend_pad),
                  ncol=1, fontsize=9)

    # ax.legend(loc=legend_loc, fontsize=9)
    ax.set_title(title, pad=title_pad, fontsize=10, weight='bold')
    ax.set_xlim(x_axis_range)
    ax.set_ylim(-0.5, len(lists_of_estimates[0]) - 0.5)

    # delete the first and last x-axis labels
    ax.set_xticks(ax.get_xticks()[1:-1])


def add_to_2_axes(axes,
                  lists_of_estimates_left,
                  lists_of_errs_left,
                  lists_of_estimates_right,
                  lists_of_errs_right,
                  x_axis_label_left,
                  x_axis_label_right,
                  x_axis_range_left,
                  x_axis_range_right,
                  colors, legend_labels,
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
              x_axis_range=x_axis_range_left,
              colors=colors,
              legend_labels=legend_labels,
              y_axis_labels=y_axis_labels,
              distance_between_bars=distance_between_bars)

    # add right
    add_to_ax(ax=axes[1],
              lists_of_estimates=lists_of_estimates_right,
              lists_of_errs=lists_of_errs_right,
              title=title_right,
              x_axis_label=x_axis_label_right,
              x_axis_range=x_axis_range_right,
              colors=colors,
              legend_labels=legend_labels,
              legend_loc=legend_loc,
              distance_between_bars=distance_between_bars)


def do_fig_by_group(
        estimate_type, group_name, group_categories, group_colors, legend_labels=None,
        x_range=None, distance_between_bars=0.3, fig_size=(10, 6)):
    """
    :param estimate_type: (string) 'coeffs' or 'wtas'
    :param group_name:
    :param group_categories:
    :param group_colors:
    :param legend_labels:
    :param x_range: (list) range of x-axis
    :param distance_between_bars:
    :param fig_size:
    :return:
    """

    # get estimates and errors
    estims_no_vaccine, errs_no_vaccine = get_dict_estimates_and_errs_by_subgroups(
        survey_scenario='no vaccine',
        subgroup_name=group_name,
        attribute_keys=DICT_COEFF_LABELS.keys() if estimate_type == 'coeff' else DICT_WTA_LABELS.keys(),
        subgroup_categories=group_categories, estimate_type=estimate_type)

    estims_vaccine, errs_coefs_vaccine = get_dict_estimates_and_errs_by_subgroups(
        survey_scenario='vaccine',
        subgroup_name=group_name,
        attribute_keys=DICT_COEFF_LABELS.keys() if estimate_type == 'coeff' else DICT_WTA_LABELS.keys(),
        subgroup_categories=group_categories, estimate_type=estimate_type)

    # plot
    fig, ax = plt.subplots(1, 2, figsize=fig_size, sharey=True)
    ax[0].set_title('A)', loc='left', weight='bold')
    ax[1].set_title('B)', loc='left', weight='bold')

    x_axis_label = COEFF_LABEL if estimate_type == 'coeff' else WTA_LABEL
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
        x_axis_range_left= x_range,
        x_axis_range_right= x_range,
        colors=group_colors,
        legend_labels=group_categories if legend_labels is None else legend_labels,
        y_axis_labels=DICT_COEFF_LABELS.values(),
        legend_loc='upper right',
        distance_between_bars=distance_between_bars
    )

    fig.tight_layout(w_pad=3)
    fig.savefig('figs/one_group/{}_by_{}.png'.format(estimate_type, group_name), dpi=300)
    plt.close(fig)


def add_subgroups_to_row(axes, survey_scenario, subgroup_info, estimate_type, x_axis_range,
                         show_x_axis_label=True, legend_pad=None, title_pad=None):

    for i, key in enumerate(subgroup_info):

        # get estimates and errors
        dict_estimates, dict_errs = get_dict_estimates_and_errs_by_subgroups(
            survey_scenario=survey_scenario,
            subgroup_name=key,
            attribute_keys=DICT_COEFF_LABELS.keys() if estimate_type == 'coeff' else DICT_WTA_LABELS.keys(),
            subgroup_categories=subgroup_info[key]['group_categories'],
            estimate_type=estimate_type
        )

        if show_x_axis_label:
            x_axis_label = COEFF_LABEL if estimate_type == 'coeff' else WTA_LABEL
        else:
            x_axis_label = ''

        add_to_ax(
            ax=axes[i],
            lists_of_estimates=list(dict_estimates.values()),
            lists_of_errs=list(dict_errs.values()),
            x_axis_label=x_axis_label,
            colors=subgroup_info[key]['group_colors'],
            legend_labels=subgroup_info[key]['legend_labels'],
            y_axis_labels=DICT_COEFF_LABELS.values() if estimate_type == 'coeff' else DICT_WTA_LABELS.values(),
            title=subgroup_info[key]['title'],
            x_axis_range=x_axis_range,
            legend_loc='upper center',
            legend_pad=legend_pad,
            title_pad=title_pad,
            distance_between_bars=subgroup_info[key]['dist_between_bars']
        )


def do_row_of_subgroups(estimate_type, survey_scenario, subgroup_info, x_axis_range,
                        fig_size, w_pad, legend_pad=None, title_pad=None):

    n_of_panels = len(subgroup_info)
    fig, ax = plt.subplots(1, n_of_panels, figsize=fig_size, sharey=True)

    # populate panels
    for i in range(n_of_panels):
        ax[i].set_title('{})'.format(string.ascii_uppercase[i]), loc='left', weight='bold')

    add_subgroups_to_row(axes=ax, survey_scenario=survey_scenario, subgroup_info=subgroup_info,
                         estimate_type=estimate_type, x_axis_range=x_axis_range,
                         legend_pad=legend_pad, title_pad=title_pad, show_x_axis_label=False)

    fig.supxlabel(COEFF_LABEL.replace("\n", " ") if estimate_type == 'coeff' else WTA_LABEL.replace("\n", " "),
                  fontsize=11, weight='bold', x=0.65, y=0.02)

    fig.tight_layout(w_pad=w_pad)
    # combine keys
    group_names = '_'.join(list(subgroup_info.keys()))
    fig.savefig('figs/row_of_groups/{}_by_{}.png'.format(estimate_type, group_names), dpi=300)
    plt.close(fig)


def do_coeff_and_wta_of_a_subgroup(subgroup_name, subgroup_info,
                                   coeff_x_axis_range, wta_x_axis_range,
                                   fig_size, w_pad=None, legend_pad=None, title_pad=None):
    """

    """
    fig, axes = plt.subplots(2, 2, figsize=fig_size)

    # populate panels
    for i in range(4):
        axes.ravel()[i].set_title('{})'.format(string.ascii_uppercase[i]), loc='left', weight='bold')

    for row_index, estimate_type in enumerate(['coeff', 'wta']):

        # get estimates and errors
        estims_no_vaccine, errs_no_vaccine = get_dict_estimates_and_errs_by_subgroups(
            survey_scenario='no vaccine',
            subgroup_name=subgroup_name,
            attribute_keys=DICT_COEFF_LABELS.keys() if estimate_type == 'coeff' else DICT_WTA_LABELS.keys(),
            subgroup_categories=subgroup_info['group_categories'], estimate_type=estimate_type)

        estims_vaccine, errs_coefs_vaccine = get_dict_estimates_and_errs_by_subgroups(
            survey_scenario='vaccine',
            subgroup_name=subgroup_name,
            attribute_keys=DICT_COEFF_LABELS.keys() if estimate_type == 'coeff' else DICT_WTA_LABELS.keys(),
            subgroup_categories=subgroup_info['group_categories'], estimate_type=estimate_type)

        add_to_2_axes(
            axes=axes[row_index],
            lists_of_estimates_left=list(estims_no_vaccine.values()),
            lists_of_errs_left=list(errs_no_vaccine.values()),
            lists_of_estimates_right=list(estims_vaccine.values()),
            lists_of_errs_right=list(errs_coefs_vaccine.values()),
            title_left='Vaccine Not Available',
            title_right='Vaccine Available',
            x_axis_label_left=COEFF_LABEL if estimate_type == 'coeff' else WTA_LABEL,
            x_axis_label_right=COEFF_LABEL if estimate_type == 'coeff' else WTA_LABEL,
            x_axis_range_left=coeff_x_axis_range if estimate_type == 'coeff' else wta_x_axis_range,
            x_axis_range_right=coeff_x_axis_range if estimate_type == 'coeff' else wta_x_axis_range,
            colors=subgroup_info['group_colors'],
            legend_labels=subgroup_info['legend_labels'],
            y_axis_labels=DICT_COEFF_LABELS.values() if estimate_type == 'coeff' else DICT_WTA_LABELS.values(),
            legend_loc='upper right',
            distance_between_bars=subgroup_info['dist_between_bars']
        )

        # get ticks from the left panel
        axes[row_index][1].set_yticks(axes[row_index][0].get_yticks())
        axes[row_index][1].set_yticklabels([])

    fig.tight_layout(w_pad=w_pad)
    fig.savefig('figs/one_group/coeff_wta_by_{}.png'.format(subgroup_name), dpi=300)
    plt.close(fig)


def do_matrix_of_subgroups( n_rows, n_cols,
        estimate_type, survey_scenario, subgroup_info, x_axis_range, fig_size, w_pad,
        legend_pad=None, title_pad=None, h_pad=2):

    # n_of_panels = len(subgroup_info)
    fig, ax = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=fig_size, sharex=False, sharey=True)

    # add A, B, C, labels
    for i in range(n_rows):
        for j in range(n_cols):
            ax[i, j].set_title('{})'.format(string.ascii_uppercase[i*n_cols + j]),
                               loc='left', weight='bold', fontsize=10)

    k = 0
    for i in range(n_rows):
        n_cols_in_this_row = min(n_cols, len(subgroup_info) - k)
        add_subgroups_to_row(
            axes=ax[i], survey_scenario=survey_scenario,
            subgroup_info= {key: subgroup_info[key] for key in
                            list(subgroup_info.keys())[k:k+n_cols_in_this_row]},
            estimate_type=estimate_type, x_axis_range=x_axis_range,
            legend_pad=legend_pad, title_pad=title_pad,
            show_x_axis_label=False)

        if n_cols_in_this_row < n_cols:
            for j in range(n_cols_in_this_row, n_cols):
                ax[i, j].axis('off')

        k += n_cols

    # # add x-axis label to the first row
    # fig.text(0.56 if estimate_type == 'coeff' else 0.37,
    #          0.52,
    #          COEFF_LABEL.replace("\n", " ") if estimate_type == 'coeff' else WTA_LABEL.replace("\n", " "),
    #          fontsize=12)

    fig.supxlabel(COEFF_LABEL.replace("\n", " ") if estimate_type == 'coeff' else WTA_LABEL.replace("\n", " "),
                  fontsize=11, weight='bold' , x=0.65, y=0.02)

    fig.tight_layout(w_pad=w_pad, h_pad=h_pad)
    # combine keys
    group_names = '_'.join(list(subgroup_info.keys()))
    fig.savefig('figs/matrix_of_groups/{}_{}_by_{}.png'.format(survey_scenario, estimate_type, group_names), dpi=300)