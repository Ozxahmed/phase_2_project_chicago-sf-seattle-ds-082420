"""Adds 0s infront of the minor untill it reaches 4 characters.

The Minor is stored without any precursor 0s. This function adds those 0s.

Requires desired column (as df)
"""

def minor_pad (df):
    df["Minor"] = df["Minor"].apply(lambda x: f"{df.Minor[x]:04}")
    return series

"""Adds 0s infront of the Major untill it reaches 6 characters.

The Major is stored without any precursor 0s. This function adds those 0s.

Requires desired column (as df)
"""

def major_pad (df):
    df["Major"] = df["Major"].apply(lambda x: f"{df.Major[x]:06}")
    return series



"""Runs a left sided, 1 sample t test.

Runs a critical statistic t test to help determine statistical significance

Requires an alpha (ex:.05), a sample in an Array form (sample), and the population mean (pop_mean).
"""

def ttest_lside_1samp(alpha, sample, pop_mean):
    a = alpha
    dof = 1-len(sample)
    ci = 1-a
    critical_stat=stats.t.ppf(ci, dof)
    stat, pvalue = stats.ttest_1samp(sample, pop_mean)                                                 
    true_p=pvalue/2
    if true_p < a:
        print(f"Our P-Value of -{true_p} is greater than our Alpha of -{a}, so we reject null hypothesis")
    else:
        print(f"Our P-Value of -{true_p} is less than or equal to our Alpha of -{a}, so we fail to reject null hypothesis") 
        

"""Runs a left sided, 1 sample t test.

Runs a critical statistic t test to help determine statistical significance

Requires an alpha (ex:.05), a sample in an Array form (sample), and the population mean (pop_mean).
"""      

def ttest_rside_1samp(alpha, sample, pop_mean):
    a = alpha
    dof = 1-len(sample)
    ci = 1-a
    critical_stat = stats.t.ppf(ci, dof)
    stat, pvalue = stats.ttest_1samp(sample, pop_mean)                                                 
    true_p=pvalue/2
    if true_p < a:
        print(f"Our P-Value of {true_p} is less than our Alpha of {a}, so we reject null hypothesis")
    else:
        print(f"Our P-Value of {true_p} is greater than or equal to our Alpha of {a}, so we fail to reject null hypothesis")   

"""Runs a two sided, 1 sample t test.

Runs a critical statistic t test to help determine statistical significance.

Requires an alpha (ex:.05), a sample in an Array form (sample), and the population mean (pop_mean).
"""
        
def ttest_2side_1samp(alpha, sample, pop_mean):
    stat, pvalue = stats.ttest_1samp(a=sample, popmean=pop_mean)
    if pvalue < alpha:
        print(f"Our P-Value of {pvalue} is less than our Alpha of {alpha}, so we reject null hypothesis")
    else:
        print(f"Our P-Value of {pvalue} is greater than or equal to our Alpha of {alpha}, so we fail to reject null hypothesis")
        
"""Runs a left sided, 2 sample t test.

Runs a critical statistic t test to help determine statistical significance

Requires an alpha (ex:.05), and two distinct samples in an Array form (sample1 and sample2)
"""

def ttest_lside_2samp(alpha, sample1, sample2):
    
    a = alpha
    s1_mean = np.mean(sample1)
    s2_mean = np.mean(sample2)
    s1_var = np.var(sample1)
    s2_var = np.var(sample2)
    
    #determines welch's t or not
    if s1_var == s2_var:
        statistics, pvalue = stats.ttest_ind(sample1, sample2, equal_var=False)
    else:
        statistics, pvalue = stats.ttest_ind(sample1, sample2, equal_var=True)
        
    #determines statistical significance
    true_p = pvalue/2
    if true_p < a:
        print(f"Our P-Value of -{true_p} is greater than our Alpha of -{a}, so we reject null hypothesis")
    else:
        print(f"Our P-Value of -{true_p} is less than or equal to our Alpha of -{a}, so we fail to reject null hypothesis")
        

"""Runs a right sided, 2 sample t test.

Runs a critical statistic t test to help determine statistical significance.
Will run a welch's t test if needed.

Requires an alpha (ex:.05), and two distinct samples in an Array form (sample1 and sample2)
"""
        
def ttest_rside_2samp(alpha, sample1, sample2):
    
    a = alpha
    s1_mean = np.mean(sample1)
    s2_mean = np.mean(sample2)
    s1_var = np.var(sample1)
    s2_var = np.var(sample2)
    
    #determines welch's t or not
    if s1_var == s2_var:
        statistics, pvalue = stats.ttest_ind(sample1, sample2, equal_var=False)
    else:
        statistics, pvalue = stats.ttest_ind(sample1, sample2, equal_var=True)
        
    #determines statistical significance
    true_p = pvalue/2
    if true_p < a:
        print(f"Our P-Value of {true_p} is less than our Alpha of {a}, so we reject null hypothesis")
    else:
        print(f"Our P-Value of {true_p} is greater than or equal to our Alpha of {a}, so we fail to reject null hypothesis")       

"""Runs a 2 sided, 2 sample t test.

Runs a critical statistic t test to help determine statistical significance.
Will run a welch's t test if needed.

Requires an alpha (ex:.05), and two distinct samples in an Array form (sample1 and sample2)
"""
        
def ttest_2side_2samp(alpha, sample1, sample2):
    
    a = alpha
    s1_mean = np.mean(sample1)
    s2_mean = np.mean(sample2)
    s1_var = np.var(sample1)
    s2_var = np.var(sample2)
    
    #determines welch's t or not
    if s1_var == s2_var:
        statistics, pvalue = stats.ttest_ind(sample1, sample2, equal_var=False)
    else:
        statistics, pvalue = stats.ttest_ind(sample1, sample2, equal_var=True)
        
    if pvalue < a:
        print(f"Our P-Value of {pvalue} is less than our Alpha of {a}, so we reject null hypothesis")
    else:
        print(f"Our P-Value of {pvalue} is greater than or equal to our Alpha of {a}, so we fail to reject null hypothesis")
        
"""Runs a z-test.

Runs a critical statistic t test to help determine statistical significance

Requires an alpha (ex:.05), a sample in an Array form (array), the population mean (pop_mean), and the population standard deviation (pop_std).
"""
        
def z_test (alpha, array, pop_mean, pop_std):
    a = alpha
    crit_stat = 1-a
    crit_statz = stats.norm.ppf(crit_stat)
    test_stat = (np.mean(array) - pop_mean)/(pop_std/(len(array)**.5))
    
    if crit_statz < test_stat:
        print(f"Our Critical Statistic of {crit_statz} is less than our Test Statistic of {test_stat}, so we reject null hypothesis")
    else:
        print(f"Our Critical Statistic of {crit_statz} is greater than or equal to our Test Statistic of {test_stat}, so we fail to reject null hypothesis")
        
        

"""Runs a Linear Rainbow Test.

Runs a Linear Rainbow Test, to inform us if we are violating the linear assumptions.
Where:
fsm_df = df[["indep", "dep"]].copy()
fsm = ols(formula="dep ~ indep", data=fsm_df)
fsm_results = fsm.fit()

Requires fsm_results (seen above).
"""
        
def lin_rainbow_test (fsm_results):
    rainbow_statistic, rainbow_p_value = linear_rainbow(fsm_results)
    print("Rainbow statistic:", rainbow_statistic)
    print("Rainbow p-value:", rainbow_p_value)

"""Runs several distribution nomalicy tests.

Produces three graphs, to inform us if we are violating the normal distribution assumptions.
The graphs are, a histogram, QQ plot, and histgram with best fit line.

Requires your dataframe (as data), the independent variable (as indep), and your desired number of bins (as nbins).
"""
    
def norm_hist_qq_test(data, indep, nbins):
    data = sm.datasets.longley.load(as_pandas=False)
    exog = sm.add_constant(data.exog)
    mod_fit = sm.OLS(data.endog, exog).fit()
    res = mod_fit.resid # residuals
    
    #hist
    plt.hist(indep, bins=nbins)
    
    #first QQ
    sm.qqplot(res)
    plt.show()
    
    #Probplot with line of best fit
    measurements = np.random.normal(loc = 20, scale = 5, size=100)   
    stats.probplot(res, dist="norm", plot=pylab)
    pylab.show()
    
"""Runs a Homoskedacity Test that produces the Breusch-Pagan test and a visual scatter graph.

Where:
fsm_df = df[["indep", "dep"]].copy()
fsm = ols(formula="dep ~ indep", data=fsm_df)
fsm_results = fsm.fit()

Requires the independent variable (indep), dependent variable (as dep), fsm_df (seen above), and fsm_results (seen above)
"""
    
def hscdty_brpa_test (indep, dep, fsm_df, fsm_results):
    
    #Produces visual scatter graph
    y = fsm_df[f"Predicted {dep}"]
    y_hat = fsm_results.predict()
    fig, ax = plt.subplots()
    ax.set(xlabel=f"{dep}",
        ylabel=f"Residuals (Actual - Predicted {dep})")
    ax.scatter(x=y_hat, y=y-y_hat, color="blue", alpha=0.2);
    
    #Breusch-Pagan Test:
    lm, lm_p_value, fvalue, f_p_value = het_breuschpagan(y-y_hat, fsm_df[[f"{indep}"]])
    print("Lagrange Multiplier p-value:", lm_p_value)
    print("F-statistic p-value:", f_p_value) 
        