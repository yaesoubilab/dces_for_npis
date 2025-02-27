from defenisions import *
from support.fig_support import do_fig_by_group

FIG_SIZE = (10, 6)

def do_lca_fig():

    for estimate_type in ['coeff', 'wta']:
        do_fig_by_group(
            estimate_type=estimate_type,
            group_name='LCA',
            group_categories=['class0', 'class1'],
            legend_labels=['Infection Cautious', 'Infection Averse'],
            group_colors=['#008080', '#B34D4D'],
            x_range=COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
            distance_between_bars=0.2,
            fig_size=FIG_SIZE)

def do_lca3_fig():

    for estimate_type in ['coeff', 'wta']:
        do_fig_by_group(
            estimate_type=estimate_type,
            group_name='LCA3',
            group_categories=['class0', 'class1', 'class2'],
            legend_labels=['Infection Cautious', 'Infection Averse', 'Not sure'],
            group_colors=['#008080', '#B34D4D', '#FFD700'],
            x_range=COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
            distance_between_bars=0.3,
            fig_size=FIG_SIZE)


if __name__ == '__main__':
    do_lca_fig()
    do_lca3_fig()
