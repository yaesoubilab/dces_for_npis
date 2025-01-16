from fig_support import plot_coeffs_both


if __name__ == '__main__':

    # plot
    # plot_logistic_regression_coeffs(
    #     fig_size=(6, 11), vaccine_scenario='no_vaccine', x_range=(-2,2))
    # plot_logistic_regression_coeffs(
    #     fig_size=(6, 11), vaccine_scenario='vaccine', x_range=(-2,2))
    plot_coeffs_both(fig_size=(7, 11), x_range=(-2, 2))
