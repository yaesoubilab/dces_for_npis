import numpy as np


def calculate_wta_and_simulate(
        attribute_mean, attribute_std_dev,
        infection_mean, infection_std_dev,
        num_draws = 1000, alpha=0.05):

    # Step 1: Calculate WTA (or WTP) as the ratio of means
    hat_W = attribute_mean / infection_mean
    # Step 2: Simulate WTA/WTP draws and calculate confidence intervals
    wtp_differences = []
    # Repeat the process N times
    for i in range(num_draws):
        # Draw 1000 samples from N(attribute_mean, attribute_std_dev)
        attribute_samples = np.random.normal(attribute_mean, attribute_std_dev, 1)
        X_star_n = np.mean(attribute_samples)  # Take the average of the samples
        # Draw 1000 samples from N(infection_mean, infection_std_dev)
        infection_samples = np.random.normal(infection_mean, infection_std_dev, 1)
        Y_star_n = np.mean(infection_samples)  # Take the average of the samples
        # Calculate the difference: X_star_n / Y_star_n - hat_W
        d_star_n = (X_star_n / Y_star_n) - hat_W
        wtp_differences.append(d_star_n)
    # Calculate the percentiles for confidence intervals
    delta_alpha_2 = np.percentile(wtp_differences, (1 - alpha/2) * 100)
    delta_1_minus_alpha_2 = np.percentile(wtp_differences, (alpha/2) * 100)
    # Return the confidence interval
    lower_bound = hat_W - delta_alpha_2
    upper_bound = hat_W - delta_1_minus_alpha_2
    return hat_W, lower_bound, upper_bound, (upper_bound-lower_bound)/2


print('expected', -0.1 / 0.3)
results = calculate_wta_and_simulate(
    attribute_mean=0.1, attribute_std_dev=0.075/2,
    infection_mean=-0.3, infection_std_dev=0.025/2,
    num_draws=10000, alpha=0.05
)
print('estimate: {}, lower bound: {}, upper bound: {}, half width: {}'.format(*results)
)

