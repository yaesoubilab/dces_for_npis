import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

COEFF_X_RANGE = (-0.5, 0.5)
WTA_X_RANGE = (-200, 200)

SUBGROUP_INFO = {
    'age':
        {
            'title': 'Age',
            'group_categories': ['<65', '65plus'],
            'legend_labels': ['<65', '65+'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'assisted_living':
        {
            'title': 'Assisted Living',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'child':
        {
            'title': 'Have Children',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'chronic':
        {
            'title': 'Chronic Conditions',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'gender':
        {
            'title': 'Gender',
            'group_categories': ['Female', 'Male'],
            'legend_labels': ['Female', 'Male'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'political':
        {
            'title': 'Political Affiliation',
            'group_categories': ['Democrat', 'Independent', 'Republican'],
            'legend_labels': ['Democrat', 'Independent', 'Republican'],
            'group_colors': ['#2C5784', 'darkseagreen', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'race':
        {
            'title': 'Race',
            'group_categories': ['Black', 'White'],
            'legend_labels': ['Black', 'White'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'residence':
        {
            'title': 'Residence',
            'group_categories': ['Urban', 'Rural', 'Suburban'],
            'legend_labels': ['Urban', 'Rural', 'Suburban'],
            'group_colors': ['#2C5784', '#D9534F', '#FFA500'],
            'dist_between_bars': 0.2
        },
    'vaccination':
        {
            'title': 'Vaccine Status',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        },
    'vulnerable_contact':
        {
            'title': 'Vulnerable Contact',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': ['#2C5784', '#D9534F'],
            'dist_between_bars': 0.2
        }
}


DICT_COEFF_LABELS = {
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

DICT_WTA_LABELS = DICT_COEFF_LABELS.copy()
del DICT_WTA_LABELS['Number_of_infections']

