from defenisions import COEFF_X_RANGE, WTA_X_RANGE, SUBGROUP_INFO
from figs_and_post_analyses.support.fig_support import do_matrix_of_subgroups, do_row_of_subgroups

FIG_SIZE = (10, 11)
W_PAD = {'coeff': 2, 'wta': 1}
LEGEND_PAD = 1.17 # increase to move the legend up
TITLE_PAD = 51 # increase to move the title up
H_PAD = 1 # to increase distance between rows


if __name__ == '__main__':

    dict_of_info = {key: SUBGROUP_INFO[key] for key in
                    ['entire_pop', 'gender', 'race', 'child',
                     'chronic', 'vulnerable_contact', 'residence', 'political']}

    estimate_type = 'wta'
    survey_scenario = 'no vaccine'
    do_matrix_of_subgroups(
        n_rows=2, n_cols=4,
        estimate_type=estimate_type,
        survey_scenario=survey_scenario,
        subgroup_info=dict_of_info,
        x_axis_range=COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
        w_pad=W_PAD[estimate_type],
        fig_size=FIG_SIZE,
        legend_pad=LEGEND_PAD,
        title_pad=TITLE_PAD,
        h_pad=H_PAD,
    )

    dict_of_info = {key: SUBGROUP_INFO[key] for key in
                    ['entire_pop', 'child', 'race', 'gender', 'political']}

    do_row_of_subgroups(
        estimate_type=estimate_type,
        survey_scenario=survey_scenario,
        subgroup_info=dict_of_info,
        x_axis_range=COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
        w_pad=W_PAD[estimate_type],
        legend_pad=LEGEND_PAD,
        title_pad=TITLE_PAD,
        fig_size=(11 , 6))
