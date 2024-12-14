from defenisions import COEFF_X_RANGE, WTA_X_RANGE
from support.fig_support import do_row_of_subgroups

FIG_SIZE = (10, 6)
W_PAD = {'coeff': 3, 'wta': 1}

subgroup_info = {
    'gender':
        {
            'title': 'Gender',
            'group_categories': ['Male', 'Female'],
            'legend_labels': ['Male', 'Female'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'child':
        {
            'title': 'Have Children',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'vaccination':
        {
            'title': 'Vaccine Status',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        }
}


if __name__ == '__main__':

    for estimate_type in ['coeff', 'wta']:
        do_row_of_subgroups(
            estimate_type=estimate_type,
            survey_scenario='no vaccine',  # 'no vaccine' or 'vaccine'
            subgroup_info=subgroup_info,
            x_axis_range=COEFF_X_RANGE if estimate_type == 'coeff' else WTA_X_RANGE,
            w_pad=W_PAD[estimate_type],
            fig_size=FIG_SIZE)
