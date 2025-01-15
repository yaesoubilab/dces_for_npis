import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns



def do_correlation_analysis(X):

    # correlation matrix
    correlation_matrix = X.corr()
    correlation_matrix.to_csv('results/correlation_matrix.csv', index=True)

    # get the maximum and minimum correlation
    np.fill_diagonal(correlation_matrix.values, np.nan)
    print('Maximum correlation:', correlation_matrix.max().max())
    print('Minimum correlation:', correlation_matrix.min().min())
    print('')

    plt.figure(figsize=(15, 14))
    sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm')
    plt.title("Correlation Matrix Heatmap")
    plt.tight_layout()
    plt.savefig('figs/correlation_matrix.png')


def plot_logistic_regression_coeffs():

    # visualize
    df = pd.read_csv('results/logistic.csv')
    df = df.iloc[::-1]

    # Filter for estimates and confidence intervals
    df = df[['Unnamed: 0', 'Coef.', '[0.025', '0.975]']]
    df.columns = ['Variables', 'Estimate', 'CI_Lower', 'CI_Upper']

    # Plot estimates with confidence intervals
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.errorbar(
        x=df['Estimate'],
        y=range(len(df['Estimate'])),
        xerr=[df['Estimate'] - df['CI_Lower'], df['CI_Upper'] - df['Estimate']],
        fmt='o',
        capsize=4,
        label='Estimate'
    )

    ax.axvline(x=0, color='gray', linestyle='--', linewidth=1)  # Reference line for zero
    # ax.set_title('Logistic Regression Coefficients with Confidence Intervals')
    ax.set_xlabel('Estimate')
    ax.set_yticks(np.arange(len(df['Estimate'])))
    ax.set_yticklabels(df.iloc[:, 0].tolist(), fontsize=10)

    ax.grid(axis='x', linestyle='--', alpha=0.7)
    # ax.legend()
    fig.tight_layout()

    # Save the plot
    fig.savefig('figs/logistic_regression_ci.png', dpi=300, bbox_inches='tight')