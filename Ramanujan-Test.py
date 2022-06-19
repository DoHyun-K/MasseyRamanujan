from ramanujan.LHSHashTable import LHSHashTable
from ramanujan.constants import g_const_dict
from ramanujan.poly_domains.CartesianProductPolyDomain import CartesianProductPolyDomain
from ramanujan.enumerators.EfficientGCFEnumerator import EfficientGCFEnumerator
saved_hash = 'i_lhs_dept5'
lhs_coefs_range = 5
lhs = LHSHashTable(
   saved_hash,
   lhs_coefs_range,
   [g_const_dict['i']])
poly_search_domain = CartesianProductPolyDomain(
    2, [-5, 5],
    2, [-5, 5])


enumerator = EfficientGCFEnumerator(
    lhs,
    poly_search_domain,
    [g_const_dict['e']]
    )
result = enumerator.full_execution()
enumerator.print_results()