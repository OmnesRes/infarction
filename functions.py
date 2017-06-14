import numpy as np
from scipy.stats import f as f_stat
from scipy.stats import f_oneway


##load the data set with a list comprehension, using tab as delimiter
f=open('pizzastudy.txt')
data=[i.strip().split('\t') for i in f]

#get indexes of columns
treatment=data[0].index('treatment')
pieces=data[0].index('pieces')
group=data[0].index('group')
gender=data[0].index('gender')
slice_cond=data[0].index('slice_cond')
genderd=data[0].index('genderd')
taste_general=data[0].index('taste_general')
taste_first=data[0].index('taste_first')
sat_first=data[0].index('sat_first')
enj_first=data[0].index('enj_first')
taste_middle=data[0].index('taste_middle')
sat_middle=data[0].index('sat_middle')
enj_middle=data[0].index('enj_middle')
taste_last=data[0].index('taste_last')
sat_last=data[0].index('sat_last')
enj_last=data[0].index('enj_last')
ate_more_pizza=data[0].index('ate_more_pizza')
was_hungry=data[0].index('was_hungry')
am_hungry=data[0].index('am_hungry')
feel_guilty=data[0].index('feel_guilty')
physic_uncomf=data[0].index('physic_uncomf')
overate=data[0].index('overate')
ate_more_general=data[0].index('ate_more_general')
felt_rushed=data[0].index('felt_rushed')
mmff=data[0].index('mmff')
salad=data[0].index('salad')
calories=data[0].index('calories')
mixedgroup=data[0].index('mixedgroup')
male_1=data[0].index('male_1')
group=data[0].index('group')
ID=data[0].index('id')




##a function for recalculating the F statistic of one-way ANOVAs when only given the means, SDs, cell sizes
def one_way(means,sds,sizes):
    x=sum([u*n for u,n in zip(means,sizes)])/sum(sizes)
    sb=sum([n*(u-x)**2 for u,n in zip(means,sizes)])/(len(means)-1)
    sw=sum([(n-1)*s**2 for s,n in zip(sds,sizes)])/(sum(sizes)-len(means))
    return sb/sw

##a function for recalculating F statistics for Type 3 SS two-way ANOVAs when only given the means, cell sizes, and SDs
##cannot reproduce calculations that involve more than two levels and are unbalanced
def two_way(n,u,s):
    '''n,u, and s are numpy matrices containing floats'''
    sizes=[float(x) for b in n.tolist() for x in b]
    sds=[float(x) for b in s.tolist() for x in b]
    means=[float(x) for b in u.tolist() for x in b]
    Nh=len(sizes)**2/sum([1/i for i in sizes])
    MSw=sum([(i-1)*j**2 for i,j in zip(sizes,sds)])/(sum(sizes)-len(sizes))
    SSbc=Nh*variance(means,sum(means)/len(means))
    row_ms=[i.sum()/len(i.tolist()[0]) for i in u]
    SSr=Nh*variance(row_ms,sum(row_ms)/len(row_ms))
    col_ms=[i.sum()/len(i.tolist()[0]) for i in u.T]
    SSc=Nh*variance(col_ms,sum(col_ms)/len(col_ms))
    SSint=SSbc-SSr-SSc
    return round(SSr/MSw/(n.shape[0]-1),2),round(SSc/MSw/(n.shape[1]-1),2),round(SSint/MSw/((n.shape[0]-1)*(n.shape[1]-1)),2)

##function for calculating population variance (used in two_way)
def variance(data,u):
    return sum([(i-u)**2 for i in data])/len(data)

##a boolean for filtering diners by pieces eaten
def my_filter(i,lower):
    if i[pieces]!='':
        if float(i[pieces])>lower:
            return True
        else:
            return False
    else:
        return False

##A function for Welch's t test                         
def unequal(means,sds,sizes):
    return abs((means[0]-means[1])/(sds[0]**2/sizes[0]+sds[1]**2/sizes[1])**.5)
