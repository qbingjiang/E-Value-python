import math
def cal_E_values(rr, lower=None, upper=None, whichr='or', ifrare=False): 
    '''
    calculate the e-value with its CI of 'Risk ratio, Odds ratio , hazard ratio'
    ref::
    [1]Sensitivity Analysis in Observational Research: Introducing the E-Value
    ''' 
    print(rr, lower, upper, '------>' )
    if rr>1: 
        if whichr == 'or' and not ifrare: 
            rr = math.sqrt(rr)
        if whichr == 'hr' and not ifrare:　
            rr = (1-pow(0.5, math.sqrt(rr)))/(1-pow(0.5, math.sqrt(1/rr)))
        e_value = rr + math.sqrt(rr*(rr-1)) 

        if lower and upper: 
            if whichr == 'or' and not ifrare: 
                lower = math.sqrt(lower)
                upper = math.sqrt(upper)
            if whichr == 'hr' and not ifrare:　
                lower = (1-pow(0.5, math.sqrt(lower)))/(1-pow(0.5, math.sqrt(1/lower)))
                upper = (1-pow(0.5, math.sqrt(upper)))/(1-pow(0.5, math.sqrt(1/upper)))

            if lower <= 1:
                e_value_lower = 1
                e_value_upper = upper + math.sqrt(upper*(upper-1)) 
            else:
                e_value_lower = lower + math.sqrt(lower*(lower-1)) 
                e_value_upper = upper + math.sqrt(upper*(upper-1)) 

    else: 
        rr = 1/rr
        if whichr == 'or' and not ifrare: 
            rr = math.sqrt(rr) 
        if whichr == 'hr' and not ifrare:　
            rr = (1-pow(0.5, math.sqrt(rr)))/(1-pow(0.5, math.sqrt(1/rr)))
        e_value = rr + math.sqrt(rr*(rr-1)) 

        if lower and upper: 
            lower_invert = 1/upper
            upper_invert = 1/lower
            lower = lower_invert
            upper = upper_invert
            if whichr == 'or' and not ifrare: 
                lower = math.sqrt(lower)
                upper = math.sqrt(upper)
            if whichr == 'hr' and not ifrare:　
                lower = (1-pow(0.5, math.sqrt(lower)))/(1-pow(0.5, math.sqrt(1/lower)))
                upper = (1-pow(0.5, math.sqrt(upper)))/(1-pow(0.5, math.sqrt(1/upper)))
            if lower < 1:
                e_value_lower = 1 
                e_value_upper = upper + math.sqrt(upper*(upper-1)) 
            else:
                e_value_lower = lower + math.sqrt(lower*(lower-1))  
                e_value_upper = upper + math.sqrt(upper*(upper-1)) 

    if lower and upper: 
        return round(e_value, 3), round(e_value_lower, 3), round(e_value_upper, 3)
    else: 
        return round(e_value, 3)

if __name__ == "__main__":
    ### compute E-values for OR = 0.86 with CI: [0.75, 0.99]
    a = cal_E_values(rr=0.86, lower=0.75, upper=0.99, whichr='or', ifrare=False) 
    e_value_for_table = str(a[0]) + '('+ str(a[1]) + '-' + str(a[2]) + ')'
    print("E-value with CI", e_value_for_table)
    print('\n')
