# Acceptability of non-pharmaceutical interventions to prevent the risk of COVID-19 infection in the United States

This repository contains the data and code to reproduce the results presented 
in the paper "Acceptability of non-pharmaceutical interventions to prevent 
the risk of COVID-19 infection in the United States".

## Description of the data and file structure

The datasets under [dce_analysis](\dce_analysis) contain the results of the discrete choice 
experiment conducted in the US between May-December 2024 to understand 
the population preference regarding nonpharmaceutical interventions (NPIs) during the COVID-19 pandemic.
The study examined four NPIs—mask mandates, reductions in public transit capacity, school closures, 
and business closures—implemented at varying intensities. 
It also considered two pandemic-related health outcomes: infection rates 
(which was modeled as a continuous outcome) and access to healthcare. 
By analyzing survey responses from a representative U.S. sample, 
we estimated the population’s disutility associated with these NPIs and
the population willingness-to-accept (WTA) increased levels of infection in the population to avoid NPIs.


The dataset includes the survey results from two survey scenarios representing the availability of effective vaccines. 
In total, 2,519 and 2,527 participants completed the surveys for ‘vaccine’ and ‘no vaccine’ 
scenarios (`study_data_vaccine.csv` and `study_data_no_vaccine.csv`, respectively). 
In addition to the DCE responses, we collected various socio-economic and demographic 
variables from the individuals, which are included in these csv files.



The script [analysis_script.ipynb](dce_analysis/analysis_script.ipynb) contains the main analysis script
to estimate the coefficients of the discrete choice model and to perform the necessary statistical analysis.
The code is implemented in Python and uses the Biogeme package for estimating discrete choice models.

The folder [figs_and_post_analyses](figs_and_post_analyses/) contains the Python scripts
to generate the figures presented in the paper.

## Code/software

We estimated the population utilities using mixed logic models in `Biogeme`
([https://biogeme.epfl.ch/](https://biogeme.epfl.ch/)). 
The code to analyze the data and generate figures is provided here: https://github.com/yaesoubilab/dces_for_npis. 


## Human subjects data

The data is collected from participants recruited by online
survey platform Qualtrics. The data is deidentified by Qualtrics before sharing with us. 
This research was reviewed and determined to be except by Yale's Internal Review Board (Case Number 2000037647). 