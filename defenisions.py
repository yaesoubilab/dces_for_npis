import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

WTP_X_RANGE = (-200, 200)

dict_coeff_labels = {
    'Business_closures_3':  'Non-essential businesses close',
    'Business_closures_2':  'Crowded indoor venues closed',
    'Mask_mandates_4':      'Masks required in all indoor spaces',
    'Mask_mandates_3':      'Masks required in indoor spaces\n(excluding schools)',
    'Mask_mandates_2':      'Masks required only in schools',
    'School_closures_5':    'All schools closed without remote learning',
    'School_closures_4':    'All schools closed with remote learning',
    'School_closures_3':    'High schools closed without remote learning',
    'School_closures_2':    'High schools closed with remote learning',
    'Transit_2':            '50% reduction in transit capacity',
    'Healthcare_restrictions_3': 'Restricted primary and optional care',
    'Healthcare_restrictions_2': 'Restricted primary care',
    'Number_of_infections': 'Number of infections'
}

dict_wtp_labels = dict_coeff_labels.copy()
del dict_wtp_labels['Number_of_infections']

