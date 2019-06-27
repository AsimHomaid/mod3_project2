def import_data(db_name, file_df):
    """import database and put it in a dataframe"""
    import psycopg2
    import pandas as pd
    conn = psycopg2.connect("dbname='musicdb'user='flatironschool'")
    c = conn.cursor()
    c.execute(f'''select * from {db_name}''')
    file_df = pd.DataFrame(c.fetchall())
    file_df.columns = [x[0] for x in c.description]
    return file_df

def welch_t(a, b):
    
    """ Calculate Welch's t statistic for two samples. """
    numerator = a.mean() - b.mean()
    
    # “ddof = Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof, 
    #  where N represents the number of elements. By default ddof is zero.
    
    denominator = np.sqrt(a.var(ddof=1)/a.size + b.var(ddof=1)/b.size)  
    return np.abs(numerator/denominator)

def welch_df(a, b):
    
    s1 = a.var(ddof=1)
    s2 = b.var(ddof=1)
    n1 = a.size
    n2 = b.size
    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)
    return numerator/denominator

