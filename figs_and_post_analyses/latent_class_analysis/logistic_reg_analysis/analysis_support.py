import statsmodels.api as sm


def do_logistic_regression(X, y, vaccine_scenario):

    # fit the model
    # add intercept
    X_with_const = sm.add_constant(X)
    model = sm.Logit(y, X_with_const)
    results = model.fit()

    # Display the model summary (coefficients and confidence intervals)
    # print(results.summary())
    # export results to csv
    results.summary2().tables[1].to_csv('results/coeffs_{}.csv'.format(vaccine_scenario))
