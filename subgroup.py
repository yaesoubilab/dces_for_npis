from support.fig_support import do_coeffs_by_group

FIG_SIZE = (10, 6)



if __name__ == '__main__':
    do_coeffs_by_group(group_name='gender',
                       group_categories=['Male', 'Female'],
                       group_colors = ['#2C5784', '#D9534F'],
                       distance_between_bars=0.3,
                       figsize=FIG_SIZE)
