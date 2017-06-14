##load data, functions, and modules
from functions import *


##performing both Student's and Welch's t-tests, and allowing for rounding uncertainty
##checking table 1, males
print 'Table 1'
print
print "Males' t tests"
print '{0:<10}{1:^20}{2:^20}'.format('','Student','Welch')

#Age
means=[45.22,43.47]
sds=[18.72,12.95]
sizes=[45,19]
min_means=[45.22-.005,43.47+.005]
max_means=[45.22+.005,43.47-.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('Age',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))

#Height
means=[177.63,181.74]
sds=[7.90,6.71]
sizes=[46,19]
min_means=[177.63+.005,181.74-.005]
max_means=[177.63-.005,181.74+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005

print '{0:<10}{1:^20}{2:^20}'.format('Height',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))

#Weight
means=[87.09,98.51]
sds=[16.88,22.23]
sizes=[45,18]
min_means=[87.09+.005,98.51-.005]
max_means=[87.09-.005,98.51+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('Weight',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))

#BMI
means=[27.62,30.00]
sds=[5.20,6.40]
sizes=[45,18]
min_means=[27.62+.005,30.00-.005]
max_means=[27.62-.005,30.00+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('BMI',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))


print
print "Females' t tests"
#Age
means=[43.68,48.18]
sds=[16.49,16.49]
sizes=[40,11]
min_means=[43.68+.005,48.18-.005]
max_means=[43.68-.005,48.18+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005

print '{0:<10}{1:^20}{2:^20}'.format('Age',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))


#Height
means=[165.84,164.68]
sds=[7.26,5.96]
sizes=[41,9]
min_means=[165.84-.005,164.68+.005]
max_means=[165.84+.005,164.68-.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('Height',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))

#Weight
means=[64.31,76.14]
sds=[10.56,12.52]
sizes=[35,7]
min_means=[64.31+.005,76.14-.005]
max_means=[64.31-.005,76.14+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('Weight',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))

#BMI
means=[23.37,28.00]
sds=[3.64,3.71]
sizes=[35,7]
min_means=[23.37+.005,28.00-.005]
max_means=[23.37-.005,28.00+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('BMI',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))



##dictionary for labels
labels={}
labels[salad]='Salad consumed'
labels[pieces]='Pizza slices consumed'
labels[overate]='I overate'
labels[felt_rushed]='I felt rushed'
labels[calories]='How many calories'
labels[physic_uncomf]='I am physically uncomfortable'


##table 2 ############################
formatting='{0:<30}{1:<15}{2:<15}{3:<15}{4:<15}{5:<11}{6:<11}{7:<15}'
print
print
print
print
print
print 'Table 2'
print '(note: at a sample size of 40 floating point errors affect Python rounding)'
print
##creating dictionaries to keep track of how many unique diners are included in the analysis
count_mf={}
count_mm={}
count_fm={}
count_ff={}
def summary_mmff(variable):
    mf=[float(i[variable]) for i in data[1:] if i[mmff]=='1' and i[variable]!='']
    mm=[float(i[variable]) for i in data[1:] if i[mmff]=='2' and i[variable]!='']
    fm=[float(i[variable]) for i in data[1:] if i[mmff]=='3' and i[variable]!='']
    ff=[float(i[variable]) for i in data[1:] if i[mmff]=='4' and i[variable]!='']
    ##updating the dictionaries with the unique identifier for the diners (the last value in each row)
    count_mf.update({i[-1]:'' for i in data[1:] if i[mmff]=='1' and i[variable]!=''})
    count_mm.update({i[-1]:'' for i in data[1:] if i[mmff]=='2' and i[variable]!=''})
    count_fm.update({i[-1]:'' for i in data[1:] if i[mmff]=='3' and i[variable]!=''})
    count_ff.update({i[-1]:'' for i in data[1:] if i[mmff]=='4' and i[variable]!=''})
    ##organizing the data into matrices for the two-way ANOVA
    n=np.matrix([[len(mf),len(mm)],[len(fm),len(ff)]])
    u=np.matrix([[np.mean(mf),np.mean(mm)],[np.mean(fm),np.mean(ff)]])
    s=np.matrix([[np.std(mf,ddof=1),np.std(mm,ddof=1)],[np.std(fm,ddof=1),np.std(ff,ddof=1)]])
    print formatting.format(labels[variable],\
                            str(round(np.mean(mf),2))+'('+str(round(np.std(mf,ddof=1),2))+')',\
                            str(round(np.mean(mm),2))+'('+str(round(np.std(mm,ddof=1),2))+')',\
                            str(round(np.mean(fm),2))+'('+str(round(np.std(fm,ddof=1),2))+')',\
                            str(round(np.mean(ff),2))+'('+str(round(np.std(ff,ddof=1),2))+')',*two_way(n,u,s))
    print formatting.format('N',len(mf),len(mm),len(fm),len(ff),'','','')


print formatting.format('','Males eating','Males eating',\
                                                                        'Females eating','Females eating',\
                                                                        'F test','F test','F test')
print formatting.format('','with females','with males',\
                                                                        'with males','with females',\
                                                                        'Effect of','Effect of','Effect of')
print formatting.format('','','','','','gender','group type',\
                                                                        'gender x group')

for variable in [salad,pieces,overate,felt_rushed,calories,physic_uncomf]:
    summary_mmff(variable)

print formatting.format('Total N',len(count_mf), len(count_mm), len(count_fm), len(count_ff),'','','')

##table 3 ######################
formatting='{0:<30}{1:<20}{2:<20}{3:<20}{4:<10}'
print
print
print
print
print
print 'Table 3'
##creating dictionaries to keep track of how many unique diners are included in the analysis
count_only_male={}
count_one_male={}
count_more_males={}


def summary_male(variable):
    only_male=[float(i[variable]) for i in data[1:] if i[mmff]=='2' and i[variable]!='']
    one_male=[float(i[variable]) for i in data[1:] if i[mmff]=='1' and i[male_1]=='1' and i[variable]!='']
    more_males=[float(i[variable]) for i in data[1:] if i[mmff]=='1' and i[male_1]=='0' and i[variable]!='']
    ##updating the dictionaries with the unique identifier for the diners (the last value in each row)
    count_only_male.update({i[-1]:'' for i in data[1:] if i[mmff]=='2' and i[variable]!=''})
    count_one_male.update({i[-1]:'' for i in data[1:] if i[mmff]=='1' and i[male_1]=='1' and i[variable]!=''})
    count_more_males.update({i[-1]:'' for i in data[1:] if i[mmff]=='1' and i[male_1]=='0' and i[variable]!=''})
    f_test=one_way([np.mean(only_male),np.mean(one_male),np.mean(more_males)],\
                  [np.std(only_male,ddof=1),np.std(one_male,ddof=1),np.std(more_males,ddof=1)],\
                  [len(only_male),len(one_male),len(more_males)])
    print formatting.format(labels[variable],\
                            str(round(np.mean(only_male),2))+'('+str(round(np.std(only_male,ddof=1),2))+')',\
                            str(round(np.mean(one_male),2))+'('+str(round(np.std(one_male,ddof=1),2))+')',\
                            str(round(np.mean(more_males),2))+'('+str(round(np.std(more_males,ddof=1),2))+')',\
                            round(f_test,2))
    print formatting.format('N',len(only_male),len(one_male),len(more_males),'')


print formatting.format('','Only-male groups','Only one male in','More than one male','F test')
print formatting.format('','','mixed-sex groups','in mixed-sex groups','')

for variable in [salad,pieces,overate,felt_rushed,calories,physic_uncomf]:
    summary_male(variable)

print formatting.format('Total N',len(count_only_male),len(count_one_male),len(count_more_males),'')

