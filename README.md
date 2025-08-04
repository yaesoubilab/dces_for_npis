# Acceptability of non-pharmaceutical interventions to prevent the risk of COVID-19 infection in the United States

# Study Description
This repository contains the data and code to reproduce the results presented 
in the paper "Acceptability of non-pharmaceutical interventions to prevent 
the risk of COVID-19 infection in the United States".

This study used discrete choice experiments (DCEs) to assess the population's disutility
associated with non-pharmaceutical interventions (NPIs) during the COVID-19 pandemic.
The study examined four NPIs—mask mandates, reductions in public transit capacity, school closures, 
and business closures—implemented at varying intensities. 
It also considered two pandemic-related health outcomes: infection rates 
(which was modeled as a continuous outcome) and access to healthcare. 
By analyzing survey responses from a representative U.S. sample, 
we estimated the population’s disutility associated with these NPIs and
the population willingness-to-accept (WTA) increased levels of infection in the population to avoid NPIs.

## Data

The datasets under [data](data) contain the results of DCEs conducted in the US between May-December 2024. 
The dataset includes the survey results from two survey scenarios representing the availability of effective vaccines. 
In total, 2,519 and 2,527 participants completed the surveys for ‘vaccine’ and ‘no vaccine’ 
scenarios:  
- CSV files with prefix `DCE COVID19 No Vaccine` contain the responses for the no vaccine scenario and 
`Qualtrics_design_no_vacc_COVID-19_29_April` contains the corresponding experimental designs.
- CSV files with prefix `DCE COVID19 Vaccine` contain the responses for the vaccine scenario and 
- `Qualtrics_design_vacc_COVID-19_29_April` contains the corresponding experimental designs.

In addition to the DCE responses, we collected various socio-economic and demographic 
variables from the individuals, which are included in these csv files.

## Code

The script [analysis_script.ipynb](dce_analysis/analysis_script.ipynb) contains the main analysis script
to estimate the coefficients of mixed logic models used to analyze the data. 
The code is implemented in `Python` and uses the `Biogeme` package for estimating discrete choice models.

The folder [figs_and_post_analyses](figs_and_post_analyses/) contains the `Python` scripts
to generate the figures presented in the paper.


## Human subjects data

The data is collected from participants recruited by online
survey platform Qualtrics. The data is deidentified by Qualtrics before sharing with us. 
This research was reviewed and determined to be except by Yale's Internal Review Board (Case Number 2000037647). 
