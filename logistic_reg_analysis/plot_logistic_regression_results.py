from fig_support import plot_logistic_regression_coeffs


if __name__ == '__main__':

    # plot
    plot_logistic_regression_coeffs(fig_size=(6, 11), vaccine_scenario='no_vaccine')
    plot_logistic_regression_coeffs(fig_size=(6, 11), vaccine_scenario='vaccine')

