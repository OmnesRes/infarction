##load data, functions and modules
from functions import *


##table 1
print 'Table 1'
print '{0:<30}{1:^20}{2:^20}{3:^20}'.format('','$4 buffet','$8 buffet','F test (p value)')

#possible F statistic ranges for the Age summary stats
means=[44.16,46.08]
sds=[19.00,14.46]
sizes=[64,65]
min_means=[44.16+.005,46.08-.005]
max_means=[44.16-.005,46.08+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
min_test=one_way(min_means,min_sds,sizes)
max_test=one_way(max_means,max_sds,sizes)
print '{0:<30}{1:^20}{2:^20}{3:^20}'.format('Age','','',str(round(min_test,2))+'-'+str(round(max_test,2))+' ('+str(round(1-f_stat.cdf(max_test,1,64+65-2),2))+'-'+str(round(1-f_stat.cdf(min_test,1,64+65-2),2))+')')


#the gender percents based on the data set
counts_1={}
counts_2={}
for i in data[1:]:
    if i[treatment]=='1':
        counts_1[i[gender]]=counts_1.get(i[gender],0)+1
    else:
        counts_2[i[gender]]=counts_2.get(i[gender],0)+1

print '{0:<30}{1:^20}{2:^20}{3:^20}'.format('Gender (male percent)',round(counts_1['1']/float(counts_1['1']+counts_1['2']),3), round(counts_2['1']/float(counts_2['1']+counts_2['2']),3),'')
print '{0:<30}{1:^20}{2:^20}{3:^20}'.format('N',counts_1['1']+counts_1['2'], counts_2['1']+counts_2['2'],'')

#possible F statistic ranges for the height summary stats
means=[68.52,67.91]
sds=[3.95,3.93]
sizes=[64,63]
min_means=[68.52-.005,67.91+.005]
max_means=[68.52+.005,67.91-.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
min_test=one_way(min_means,min_sds,sizes)
max_test=one_way(max_means,max_sds,sizes)
print '{0:<30}{1:^20}{2:^20}{3:^20}'.format('Height','','',str(round(min_test,2))+'-'+str(round(max_test,2))+' ('+str(round(1-f_stat.cdf(max_test,1,64+63-2),2))+'-'+str(round(1-f_stat.cdf(min_test,1,64+63-2),2))+')')

#possible F statistic ranges for the weight summary stats
means=[180.84,182.31]
sds=[48.37,48.41]
sizes=[62,54]
min_means=[180.84+.005,182.31-.005]
max_means=[180.84-.005,182.31+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
min_test=one_way(min_means,min_sds,sizes)
max_test=one_way(max_means,max_sds,sizes)
print '{0:<30}{1:^20}{2:^20}{3:^20}'.format('Weight','','',str(round(min_test,2))+'-'+str(round(max_test,2))+' ('+str(round(1-f_stat.cdf(max_test,1,62+54-2),2))+'-'+str(round(1-f_stat.cdf(min_test,1,62+54-2),2))+')')

##dictionary for labels
labels={}
labels[group]='Number in group'
labels[was_hungry]='I was hungry when I came in'
labels[am_hungry]='I am hungry now'
labels[taste_general]='The pizza, in general, tasted really great'
labels[taste_first]='The first piece of pizza I ate tasted really great'
labels[sat_first]='The first piece of pizza I ate was very satisfying'
labels[enj_first]='The first piece of pizza I ate was very enjoyable'
labels[taste_middle]='The middle piece of pizza I ate tasted really great'
labels[sat_middle]='The middle piece of pizza I ate was very satisfying'
labels[enj_middle]='The middle piece of pizza I ate was very enjoyable'
labels[taste_last]='The last piece of pizza I ate tasted really great'
labels[sat_last]='The last piece of pizza I ate was very satisfying'
labels[enj_last]='The last piece of pizza I ate was very enjoyable'


##function for the ANOVAs
def summary_f(variable,lower='false',formatting='{0:<55}{1:^15}{2:^15}{3:^15}'):
    if lower!='false':
        treatment_1=[int(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and my_filter(i,lower)]
        treatment_2=[int(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and my_filter(i,lower)]
    else:
        treatment_1=[int(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='']
        treatment_2=[int(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='']
    result=f_oneway(treatment_1,treatment_2)
    print formatting.format(labels[variable],\
        str(round(np.mean(treatment_1),2))+' ('+str(round(np.std(treatment_1,ddof=1),2))+')',\
        str(round(np.mean(treatment_2),2))+' ('+str(round(np.std(treatment_2,ddof=1),2))+')',\
        str(round(result.statistic,2))+' ('+str(round(result.pvalue,2))+')')
    print formatting.format('N',len(treatment_1),len(treatment_2),'')


summary_f(group,formatting='{0:<30}{1:^20}{2:^20}{3:^20}')
summary_f(was_hungry,formatting='{0:<30}{1:^20}{2:^20}{3:^20}')
summary_f(am_hungry,formatting='{0:<30}{1:^20}{2:^20}{3:^20}')

print
print
print
print 'Reproducing original Table 2 statistics'
print '(note: at a sample size of 40 floating point errors affect Python rounding)'
print '{0:<55}{1:^15}{2:^15}{3:^15}'.format('','$4 buffet','$8 buffet','F test (p value)')

##reproducing response table not taking into account the pieces diners reported
for variable in [taste_general,taste_first,sat_first,enj_first,taste_middle,sat_middle,enj_middle,taste_last,\
                 sat_last,enj_last]:
    summary_f(variable)



print
print
print

##calculating statistics taking into account the pieces diners reported (will not match STATA output)
##diners who did report how many pieces are excluded
print 'Calculating correct Table 2 statistics'
print '{0:<55}{1:^15}{2:^15}{3:^15}'.format('','$4 buffet','$8 buffet','F test (p value)')
summary_f(taste_general,lower=0)
summary_f(taste_first,lower=0)
summary_f(sat_first,lower=0)
summary_f(enj_first,lower=0)
summary_f(taste_middle,lower=2)
summary_f(sat_middle,lower=2)
summary_f(enj_middle,lower=2)
summary_f(taste_last,lower=1)
summary_f(sat_last,lower=1)
summary_f(enj_last,lower=1)


##table 3
print
print
print
print

##calculating Table 3 taking into account the pieces diners reported
##will match STATA output, unclear how to reproduce the original statistics
print 'Table 3 means'
print '{0:<35}{1:^18}{2:^18}'.format('','$4','$8')
print '{0:<35}{1:^6}{2:^6}{3:^6}{4:^6}{5:^6}{6:^6}'.format('','1st','2nd','3rd','1st','2nd','3rd')
output_means=[]
output_sizes=[]
for variable in [taste_first,taste_middle,taste_last]:
    temp=[int(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and my_filter(i,2)]
    output_means.append(round(np.mean(temp),2))
    output_sizes.append(len(temp))
for variable in [taste_first,taste_middle,taste_last]:
    temp=[int(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and my_filter(i,2)]
    output_means.append(round(np.mean(temp),2))
    output_sizes.append(len(temp))
print '{0:<35}{1:^6.2f}{2:^6.2f}{3:^6.2f}{4:^6.2f}{5:^6.2f}{6:^6.2f}'.format(*['Pizza taste evaluations']+output_means)
print '{0:<35}{1:^6}{2:^6}{3:^6}{4:^6}{5:^6}{6:^6}'.format(*['N']+output_sizes)


output_means=[]
output_sizes=[]
for variable in [sat_first,sat_middle,sat_last]:
    temp=[int(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and my_filter(i,2)]
    output_means.append(round(np.mean(temp),2))
    output_sizes.append(len(temp))
for variable in [sat_first,sat_middle,sat_last]:
    temp=[int(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and my_filter(i,2)]
    output_means.append(round(np.mean(temp),2))
    output_sizes.append(len(temp))
print '{0:<35}{1:^6.2f}{2:^6.2f}{3:^6.2f}{4:^6.2f}{5:^6.2f}{6:^6.2f}'.format(*['Pizza satisfaction evaluations']+output_means)
print '{0:<35}{1:^6}{2:^6}{3:^6}{4:^6}{5:^6}{6:^6}'.format(*['N']+output_sizes)


output_means=[]
output_sizes=[]
for variable in [enj_first,enj_middle,enj_last]:
    temp=[int(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and my_filter(i,2)]
    output_means.append(round(np.mean(temp),2))
    output_sizes.append(len(temp))
for variable in [enj_first,enj_middle,enj_last]:
    temp=[int(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and my_filter(i,2)]
    output_means.append(round(np.mean(temp),2))
    output_sizes.append(len(temp))
print '{0:<35}{1:^6.2f}{2:^6.2f}{3:^6.2f}{4:^6.2f}{5:^6.2f}{6:^6.2f}'.format(*['Pizza satisfaction evaluations']+output_means)
print '{0:<35}{1:^6}{2:^6}{3:^6}{4:^6}{5:^6}{6:^6}'.format(*['N']+output_sizes)
