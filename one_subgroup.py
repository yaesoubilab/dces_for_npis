from support.fig_support import do_fig_by_group

FIG_SIZE = (10, 6)


if __name__ == '__main__':

    for estimate_type in ['coeff', 'wta']:
        do_fig_by_group(
            estimate_type=estimate_type,
            group_name='gender',
            group_categories=['Male', 'Female'],
            group_colors = ['#2C5784', '#D9534F'],
            distance_between_bars=0.2,
            fig_size=FIG_SIZE)
