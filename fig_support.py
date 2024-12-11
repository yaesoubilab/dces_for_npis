import numpy as np


def add_to_ax(ax,
              lists_of_estimates,
              lists_of_ci,
              x_axis_label,
              colors, labels, y_axis_labels=None):

    # number of lists
    n = len(lists_of_estimates)

    for i, this_list in enumerate(lists_of_estimates):
        ax.errorbar(this_list,
                    np.arange(len(this_list)),
                    xerr=lists_of_ci[i],
                    fmt='o', color=colors[i], ecolor=colors[i], capsize=5, alpha=0.7,
                    label=labels[i])

    ax.set_xlabel(x_axis_label, fontsize=14)
    if y_axis_labels is not None:
        ax.set_yticks(np.arange(len(y_axis_labels)))
        ax.set_yticklabels(y_axis_labels, fontsize=10)

    ax.axvline(x=0, color='black', linestyle='-', linewidth=1.3)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()