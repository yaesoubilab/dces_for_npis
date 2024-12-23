from defenisions import COEFF_X_RANGE, WTA_X_RANGE, SUBGROUP_INFO
from support.fig_support import do_row_of_subgroups

FIG_SIZE = (10, 5)
W_PAD = {'coeff': 2, 'wta': 1}




if __name__ == '__main__':

    dict_of_info = {key: SUBGROUP_INFO[key] for key in ['age', 'gender', 'political']}

    for estimate_type in ['coeff', 'wta']:
        do_row_of_subgroups(
            estimate_type=estimate_type,
            survey_scenario='no vaccine',  # 'no vaccine' or 'vaccine'
            subgroup_info=dict_of_info,
            x_axis_range=COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
            w_pad=W_PAD[estimate_type],
            fig_size=FIG_SIZE)
