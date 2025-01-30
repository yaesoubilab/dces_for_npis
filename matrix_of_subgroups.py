from defenisions import COEFF_X_RANGE, WTA_X_RANGE, SUBGROUP_INFO
from support.fig_support import do_matrix_of_subgroups

FIG_SIZE = (10.5, 11)
W_PAD = {'coeff': 2, 'wta': 1}
LEGEND_PAD = 1.18 # to move the legend up
TITLE_PAD = 51 # to move the title up



if __name__ == '__main__':

    dict_of_info = {key: SUBGROUP_INFO[key] for key in
                    ['age', 'gender', 'chronic', 'political',
                     'race', 'child', 'vulnerable_contact', 'residence']}

    for survey_scenario in ['no vaccine', 'vaccine']:
        for estimate_type in ['coeff', 'wta']:
            do_matrix_of_subgroups(
                n_rows=2, n_cols=4,
                estimate_type=estimate_type,
                survey_scenario=survey_scenario,
                subgroup_info=dict_of_info,
                x_axis_range=COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
                w_pad=W_PAD[estimate_type],
                fig_size=FIG_SIZE,
                legend_pad=LEGEND_PAD,
                title_pad=TITLE_PAD
            )
