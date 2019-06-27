def welch_t(a, b):
    import numpy as np
    """ Calculate Welch's t statistic for two samples. """
    """ a and b inputs are series"""

    numerator = a.mean() - b.mean()
    
    # “ddof = Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof, 
    #  where N represents the number of elements. By default ddof is zero.
    
    denominator = np.sqrt(a.var(ddof=1)/a.size + b.var(ddof=1)/b.size)
    
    return np.abs(numerator/denominator)


def welch_df(a, b):
    import numpy as np
    """ Calculate the effective degrees of freedom for two samples. """
    """ a and b inputs are series"""
    
    s1 = a.var(ddof=1) 
    s2 = b.var(ddof=1)
    n1 = a.size
    n2 = b.size
    
    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)
    
    return numerator/denominator


def p_value(a, b, two_sided=False):
    from scipy import stats
    import numpy as np
    """ Calculate the p value of the samples"""    
    """ a and b inputs are series"""

    t = welch_t(a, b)
    df = welch_df(a, b)
    
    p = 1-stats.t.cdf(np.abs(t), df)
    
    if two_sided:
        return 2*p
    else:
        return p

def compare_p_value_and_alpha(p_value, alpha):
    if p_value > alpha:
        print("Based on the alpha value we've set, we cannot reject the null hypothesis")
    else:
        print("Based on the alpha value we've set, we can reject the null hypothesis and accept the alternative hypothesis")