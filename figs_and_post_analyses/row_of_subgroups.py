from defenisions import COEFF_X_RANGE, WTA_X_RANGE, SUBGROUP_INFO
from figs_and_post_analyses.support.fig_support import do_row_of_subgroups

FIG_SIZE = (10, 6)
SURVEY_SCENARIO = 'no vaccine'  # 'no vaccine' or 'vaccine'
W_PAD = {'coeff': 2, 'wta': 1}
LEGEND_PAD = 1.15 # to move the legend up
TITLE_PAD = 51 # to move the title up


if __name__ == '__main__':

    dict_of_info = {key: SUBGROUP_INFO[key] for key in ['age', 'gender', 'political']}

    for estimate_type in ['coeff', 'wta']:
        do_row_of_subgroups(
            estimate_type=estimate_type,
            survey_scenario=SURVEY_SCENARIO,
            subgroup_info=dict_of_info,
            x_axis_range=COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
            w_pad=W_PAD[estimate_type],
            legend_pad=LEGEND_PAD,
            title_pad=TITLE_PAD,
            fig_size=FIG_SIZE)
