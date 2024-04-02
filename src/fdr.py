

from scipy.stats import rankdata, false_discovery_control


def cal_p_vals_rank(p_vals: list) -> list:
    """
    p_vals: list of p-values. No NaN values.

    Learn from https://stackoverflow.com/questions/25185205/calculating-adjusted-p-values-in-python
    Use sci rankdata(method=min) to rank the p-values.
    Return the ranked p-values.
    """
    ranked_p_values = rankdata(p_vals, method="min")

    return ranked_p_values

def cal_fdr(p_vals: list) -> list:
    """
    p_vals: list of p-values. No NaN values.

    Calculate the FDR of the p-values using false_discovery_control (Benjamini-Hochberg method).
    Return the FDR of the p-values.
    """
    fdr = false_discovery_control(p_vals, method='bh')

    return fdr