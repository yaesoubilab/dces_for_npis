import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


coef_labels = ["Crowded indoor venues closed",
              "Non-essential businesses close",
              "Masks required only in schools",
              "Masks required in public",
              "Masks required in all indoor spaces",
              "High schools close with remote learning",
              "High schools close, no remote learning",
              "All schools close with remote learning",
              "All schools close, no remote learning",
              "50% reduction in transit capacity",
              "Restricted primary care",
               "Restricted primary and optional care",
               "Number of infections"]
wta_labels = ["Crowded indoor venues closed",
             "Non-essential businesses close",
             "Masks required only in schools",
             "Masks required in public",
             "Masks required in all indoor spaces",
             "High schools close with remote learning",
             "High schools close, no remote learning",
             "All schools close with remote learning",
             "All schools close, no remote learning",
             "50% reduction in transit capacity",
             "", "", ""]

reorder_indices = [
    'Business_closures_2',
    'Business_closures_3',
    'Mask_mandates_2',
    'Mask_mandates_3',
    'Mask_mandates_4',
    'School_closures_2',
    'School_closures_3',
    'School_closures_4',
    'School_closures_5',
    'Transit_2',
    'Healthcare_restrictions_2',
    'Healthcare_restrictions_3',
    'Number_of_infections'
]