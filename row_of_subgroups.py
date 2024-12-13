from support.fig_support import do_row_of_subgroups

FIG_SIZE = (10, 6)

subgroup_info = {
    'gender':
        {
            'title': 'Gender',
            'group_categories': ['Male', 'Female'],
            'legend_labels': ['Male', 'Female'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'vaccine status':
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
            survey_scenario='No Vaccine',
            subgroup_info = subgroup_info,
            fig_size=FIG_SIZE)