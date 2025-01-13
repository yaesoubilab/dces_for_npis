from defenisions import *
from support.func_support import get_dict_estimates_and_errs_by_subgroups

FIG_SIZE = (10, 6)

def do_lca_fig():

    # get estimates and errors
    estims_no_vaccine, errs_no_vaccine = get_dict_estimates_and_errs_by_subgroups(
        survey_scenario='no vaccine',
        subgroup_name='LCA',
        attribute_keys=DICT_COEFF_LABELS.keys(),
        subgroup_categories=['class0', 'class1'],
        estimate_type='coeff')

    print(estims_no_vaccine)


if __name__ == '__main__':
    do_lca_fig()
