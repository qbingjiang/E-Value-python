# E-Value-python
ref::
[1]Sensitivity Analysis in Observational Research: Introducing the E-Value

## calculate the e-value with its CI
    ### compute E-values for OR = 0.86 with CI: [0.75, 0.99]
    print('E-value with CI: ', cal_E_values(rr=0.86, lower=0.75, upper=0.99, whichr='or', ifrare=False) )
    >> E-value with CI: 1.369(1.076-1.577) 
