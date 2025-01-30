import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

COEFF_X_RANGE = (-0.5, 0.5)
WTA_X_RANGE = (-25, 225)

COEFF_LABEL = 'Coefficient Estimates'
WTA_LABEL = 'Willingness to Accept\n(Reduction in Cases Per 100 Population)'
    # 'Minimum Reduction in Cases\nPer 100 Population to Accept an NPI'
    # 'Minimum Effectiveness to be Acceptable\n (Reduction in Cases Per 100 Population)'

COLORS = ['#377eb8', '#ff7f00', '#4daf4a', '#17becf'] # blue, orange, purple, green
# COLORS = ['#17becf', '#e377c2', '#bcbd22'] # cyan, magenta, yellow

SUBGROUP_INFO = {
    'entire_pop':
        {
            'title': 'Average\nPopulation',
            'group_categories': None,
            'legend_labels': [None],
            'group_colors': ['#984ea3'],
            'dist_between_bars': 0
        },
    'age':
        {
            'title': 'Age',
            'group_categories': ['<65', '65plus'],
            'legend_labels': ['<65', '65+'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'assisted_living':
        {
            'title': 'Assisted Living',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'child':
        {
            'title': 'Have\nChildren',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'chronic':
        {
            'title': 'Chronic\nConditions',
            'group_categories': ['Yes', 'No'], #, 'Prefer not to answer'],
            'legend_labels': ['Yes', 'No'], # 'Prefer NA'],
            'group_colors': COLORS,
            'dist_between_bars': 0.3
        },
    'gender':
        {
            'title': 'Gender',
            'group_categories': ['Female', 'Male'],
            'legend_labels': ['Female', 'Male'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'education':
        {
            'title': 'Education',
            'group_categories': ['No College Degree', 'Postgraduate degree'],
            'legend_labels': ['No College Degree', 'College Degree'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'political':
        {
            'title': 'Political\nAffiliation',
            'group_categories': ['Democrat', 'Independent', 'Republican'],
            'legend_labels': ['Democrat', 'Independent', 'Republican'],
            'group_colors': COLORS,
            'dist_between_bars': 0.3
        },
    'health_insurance':
        {
            'title': 'Health Insurance',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'income':
        {
            'title': 'Income',
            'group_categories': ['<35,000', '35,000 - 75,000', '> 150,000'],
            'legend_labels': ['<35k', '35-75k', '>75k'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'news':
        {
            'title': 'News Source',
            'group_categories': ['Social media',
                                 'News apps or websites',
                                 'Radio or podcasts',
                                 'Other'],
            'legend_labels': ['Social Media', 'News Apps & Websites', 'Radio/Podcasts', 'Other'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'pregnant':
        {
            'title': 'Pregnant',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'race':
        {
            'title': 'Race',
            'group_categories': ['Black', 'White'],
            'legend_labels': ['Black', 'White'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'remote':
        {
            'title': 'Remote Work',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'residence':
        {
            'title': 'Residence',
            'group_categories': ['Urban', 'Suburban', 'Rural'],
            'legend_labels': ['Urban', 'Suburban', 'Rural'],
            'group_colors': COLORS,
            'dist_between_bars': 0.3
        },
    'vaccination':
        {
            'title': 'Vaccine\nStatus',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        },
    'vulnerable_contact':
        {
            'title': 'Vulnerable\nContact',
            'group_categories': ['Yes', 'No'],
            'legend_labels': ['Yes', 'No'],
            'group_colors': COLORS,
            'dist_between_bars': 0.2
        }
}


DICT_COEFF_LABELS = {
    'Business_closures_3':  'Non-essential businesses closed',
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


DICT_VARIABLES = {
    'Gender': {
        'label': 'Gender',
        'values': ['Female', 'Male', 'Other'],
        'sub labels': ['Female (Reference)', 'Male', 'Other']
    },
    'Hispanic': {
        'label': 'Hispanic?',
        'values': ['No', 'Yes'],
        'sub labels': ['No (Reference)', 'Yes']
    },
    'Age': {
        'label': 'Age',
        'values': ['<65', '≥ 65'],
        'sub labels': ['<65 (Reference)', '65+']
    },
    'Residence': {
        'label': 'Residence',
        'values': ['Urban', 'Suburban', 'Rural'],
        'sub labels': ['Urban (Reference)', 'Suburban', 'Rural']
    },
    'Education': {
        'label': 'Education',
        'values': ['With College Degree', 'Without College Degree'],
        'sub labels': ['With College Degree (Reference)', 'Without College Degree']
    },
    'Political': {
        'label': 'Political Affiliation',
        'values': ['Democrat', 'Independent', 'Republican'],
        'sub labels': ['Democrat (Reference)', 'Independent', 'Republican']
    },
    'News': {
        'label': 'News Source',
        'values': ['Print media (newspapers, journals)',
                   'Social media (Instagram, Facebook, X (Twitter), TikTok)',
                   'TV (including cable)',
                   'News apps or websites',
                   'Radio or podcasts',
                   'Do not read/listen/watch the news',
                   'Other'],
        'sub labels': ['Printed media (Reference)',
                       'Social Media',
                       'TV and Cable',
                       'News Apps and Websites',
                       'Radio and Podcasts',
                       'Do not read/listen/watch the news',
                       'Other']
    },
    'Income': {
        'label': 'Household Income',
        'values': ['<35,000', '$35,000 - 75,000', '$75,000 - 150,000', '> $150,000'],
        'sub labels': ['<$35,000 (Reference)', '$35,000-75,000', '$75,000-150,000', '>$150,000']
    },
    'Self_employed': {
        'label': 'Self-Employed?',
        'values': ['Yes', 'No'],
        'sub labels': ['Yes', 'No (Reference)']
    },
    'Remote': {
        'label': 'Remote Work?',
        'values': ['Yes', 'No', 'NA (studying, retired, not in paid employment)'],
        'sub labels': ['Yes', 'No', 'Not Applicable']
    },
    'Vehicle': {
        'label': 'Vehicle Ownership?',
        'values': ['No', 'Yes'],
        'sub labels': ['No (Reference)', 'Yes']
    },
    'Child': {
        'label': 'Had School-Aged Children?',
        'values': ['No', 'Yes'],
        'sub labels': ['No (Reference)', 'Yes']
    },
    'Pregnant': {
        'label': 'Pregnant?',
        'values': ['No', 'Yes'],
        'sub labels': ['No (Reference)', 'Yes']
    },
    'Health_Insurance': {
        'label': 'Health Insurance?',
        'values': ['No', 'Yes'],
        'sub labels': ['No (Reference)', 'Yes']
    },
    'Assisted_Living': {
        'label': 'Assisted Living?',
        'values': ['No', 'Yes'],
        'sub labels': ['No (Reference)', 'Yes']
    },
    'Chronic': {
        'label': 'Chronic Conditions?',
        'values': ['No', 'Yes', 'Prefer not to answer'],
        'sub labels': ['No (Reference)', 'Yes', 'Prefer not to answer']
    },
    'Vulnerable_contact': {
        'label': 'Vulnerable Contact?',
        'values': ['No', 'Yes'],
        'sub labels': ['No (Reference)', 'Yes']
    }
}

