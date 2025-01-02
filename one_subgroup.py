from defenisions import SUBGROUP_INFO, COEFF_X_RANGE, WTA_X_RANGE
from support.fig_support import do_fig_by_group, do_coeff_and_wta_of_a_subgroup

FIG_SIZE_ROW = (10, 6)
FIG_SIZE_SQUARE = (10, 10)


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
                fig_size=FIG_SIZE_ROW)

        do_coeff_and_wta_of_a_subgroup(
            subgroup_name=sub_group_name,
            subgroup_info=info,
            coeff_x_axis_range=COEFF_X_RANGE,
            wta_x_axis_range=WTA_X_RANGE,
            fig_size=FIG_SIZE_SQUARE,
            w_pad=2)