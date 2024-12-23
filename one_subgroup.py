from defenisions import SUBGROUP_INFO, COEFF_X_RANGE, WTA_X_RANGE
from support.fig_support import do_fig_by_group

FIG_SIZE = (10, 6)


if __name__ == '__main__':

    # dict_of_info = SUBGROUP_INFO
    dict_of_info = {key: SUBGROUP_INFO[key] for key in ['political']}

    for sub_group_name, info in dict_of_info.items():
        for estimate_type in ['coeff', 'wta']:
            do_fig_by_group(
                estimate_type=estimate_type,
                group_name=sub_group_name,
                group_categories=info['group_categories'],
                legend_labels=info['legend_labels'],
                group_colors=info['group_colors'],
                x_range= COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
                distance_between_bars=info['dist_between_bars'],
                fig_size=FIG_SIZE)
