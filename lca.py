from defenisions import *
from support.fig_support import do_fig_by_group

FIG_SIZE = (10, 6)

def do_lca_fig():

    do_fig_by_group(
        estimate_type='coeff',
        group_name='LCA',
        group_categories=['class0', 'class1'],
        legend_labels=['Infection Neutral', 'Infection Averse'],
        group_colors=['#008080', '#B34D4D'],
        x_range=COEFF_X_RANGE,
        distance_between_bars=0.2,
        fig_size=FIG_SIZE)


if __name__ == '__main__':
    do_lca_fig()
