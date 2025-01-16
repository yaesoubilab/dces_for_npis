import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from defenisions import DICT_VARIABLES


def do_correlation_analysis(X, vaccine_scenario):

    # correlation matrix
    correlation_matrix = X.corr()
    correlation_matrix.to_csv(
        'results/correlation_matrix_{}.csv'.format(vaccine_scenario), index=True)

    # get the maximum and minimum correlation
    np.fill_diagonal(correlation_matrix.values, np.nan)
    print('Maximum correlation:', correlation_matrix.max().max())
    print('Minimum correlation:', correlation_matrix.min().min())
    print('')

    plt.figure(figsize=(15, 14))
    sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm')
    plt.title("Correlation Matrix Heatmap")
    plt.tight_layout()
    plt.savefig('figs/correlation_matrix_{}.png'.format(vaccine_scenario), dpi=300)

def add_coeff_to_ax(ax, estimates, ci_l, ci_u, title=None, y_labels=None, x_range=None):

    ax.errorbar(
        x=estimates,
        y=range(len(estimates)),
        xerr=[ci_l, ci_u],
        fmt='o',
        capsize=4,
        label='Estimate'
    )

    ax.axvline(x=1, color='gray', linestyle='--', linewidth=1)  # Reference line for zero
    # ax.set_title('Logistic Regression Coefficients with Confidence Intervals')
    ax.set_xlabel('Odds Ratio')
    ax.set_yticks(range(len(y_labels)))
    ax.set_yticklabels(y_labels, fontsize=10)
    ax.set_title(title)

    if y_labels is not None:
        # left align labels
        for label in ax.get_yticklabels():
            label.set_horizontalalignment('left')
        # Adjust padding between tick labels and axis
        ax.tick_params(axis='y', pad=180)

    ax.set_ylim(-1, len(y_labels))
    ax.set_xlim(x_range)

def get_odds_and_ci(vaccine_scenario):

    # Read estimates from logistic regression
    df = pd.read_csv('results/coeffs_{}.csv'.format(vaccine_scenario))
    # Reverse the order of rows
    # df = df.iloc[::-1]
    # Filter for estimates and confidence intervals
    df = df[['Unnamed: 0', 'Coef.', '[0.025', '0.975]']]
    df.columns = ['Variables', 'Estimate', 'CI_Lower', 'CI_Upper']
    df.set_index('Variables', inplace=True)

    # adjust labels to include references
    y_labels = []
    odds = []
    ci_l = []
    ci_u = []
    for var, var_details in DICT_VARIABLES.items():
        y_labels += [var_details['label']]
        for sub_label in var_details['sub labels']:
            y_labels += ['    {}'.format(sub_label)]

        odds += [np.nan]  # for the variable name
        odds += [np.nan]  # for the reference value
        ci_l += [np.nan]  # for the variable name
        ci_l += [np.nan]  # for the reference value
        ci_u += [np.nan]  # for the variable name
        ci_u += [np.nan]  # for the reference value
        for var_value in var_details['values'][1:]:
            e = np.exp(df.at['{}_{}'.format(var, var_value), 'Estimate'])
            l = np.exp(df.at['{}_{}'.format(var, var_value), 'CI_Lower'])
            u = np.exp(df.at['{}_{}'.format(var, var_value), 'CI_Upper'])
            odds += [e]
            ci_l += [e - l]
            ci_u += [u - e]

    y_labels.reverse()
    odds.reverse()
    ci_l.reverse()
    ci_u.reverse()

    return y_labels, odds, ci_l, ci_u


def plot_logistic_regression_odds(fig_size, vaccine_scenario, x_range):

    # get labels, estimates, and confidence intervals
    y_labels, odds, ci_l, ci_u = get_odds_and_ci(vaccine_scenario=vaccine_scenario)

    # Plot estimates with confidence intervals
    fig, ax = plt.subplots(1, 1, figsize=fig_size)

    add_coeff_to_ax(ax, odds, ci_l, ci_u, y_labels=y_labels, x_range=x_range)

    # ax.grid(axis='x', linestyle='--', alpha=0.7)
    # ax.legend()
    fig.tight_layout()

    # Save the plot
    fig.savefig('figs/logistic_regression_ci_{}.png'.format(vaccine_scenario), dpi=300, bbox_inches='tight')


def plot_coeffs_both(fig_size, x_range):

    # Plot estimates with confidence intervals
    fig, ax = plt.subplots(1, 2, figsize=fig_size, sharey=True)

    ax[0].set_title('A)', loc='left', weight='bold')
    ax[1].set_title('B)', loc='left', weight='bold')

    # get labels, estimates, and confidence intervals
    y_labels, estimates, ci_l, ci_u = get_odds_and_ci(vaccine_scenario='no_vaccine')
    add_coeff_to_ax(
        ax=ax[0], estimates=estimates, ci_l=ci_l, ci_u=ci_u,
        y_labels=y_labels, x_range=x_range, title='Vaccine\nNot Available')

    # get labels, estimates, and confidence intervals
    y_labels, estimates, ci_l, ci_u = get_odds_and_ci(vaccine_scenario='vaccine')
    add_coeff_to_ax(
        ax=ax[1], estimates=estimates, ci_l=ci_l, ci_u=ci_u,
        y_labels=y_labels, x_range=x_range, title='Vaccine\nAvailable')

    # ax.legend()
    fig.tight_layout()

    # Save the plot
    fig.savefig('figs/logistic_regression_ci_both.png', dpi=300, bbox_inches='tight')
