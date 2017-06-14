##load data, functions, and modules
from functions import *



##performing both Student's and Welch's t-tests, and allowing for rounding uncertainty
print 'Table 1'
print
print '{0:<10}{1:^20}{2:^20}'.format('','Student','Welch')
#Age
means=[43.67,44.55]
sds=[18.50,14.30]
sizes=[42,49]
min_means=[43.67+.005,44.55-.005]
max_means=[43.67-.005,44.55+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('Age',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))

#Height
means=[68.65,67.76]
sds=[3.67,3.87]
sizes=[42,42]
min_means=[68.65-.005,67.76+.005]
max_means=[68.65+.005,67.76-.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('Height',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))

#Weight
means=[178.20,178.38]
sds=[48.11,45.71]
sizes=[40,40]
min_means=[178.20+.005,178.38-.005]
max_means=[178.20-.005,178.38+.005]
min_sds=np.array(sds)+.005
max_sds=np.array(sds)-.005
print '{0:<10}{1:^20}{2:^20}'.format('Weight',str(round(one_way(min_means,min_sds,sizes)**.5,2))+' - '+\
                                     str(round(one_way(max_means,max_sds,sizes)**.5,2)),\
                                     str(round(unequal(min_means,min_sds,sizes),2))+' - '+\
                                     str(round(unequal(max_means,max_sds,sizes),2)))



##dictionary for labels
labels={}
labels[ate_more_pizza]='I ate more pizza than I should have'
labels[feel_guilty]='I feel guilty about how much I ate'
labels[physic_uncomf]='I am physically uncomfortable'
labels[overate]='I overate'
labels[ate_more_general]='I ate more than I should have'


###########Table 2
formatting='{0:<40}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}{7:<15}'
print
print
print
print
print 'Table 2'
print 'Note: the other effects are not shown here as the unweighted-means solution is\
 not accurate with more than two levels.'
print 'If you want to reproduce those values I would recommend using ezanova in R'

count_one_4={}
count_two_4={}
count_three_4={}
count_one_8={}
count_two_8={}
count_three_8={}

def summary_slices(variable):
    one_4=[float(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='1']
    two_4=[float(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='2']
    three_4=[float(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='3']
    one_8=[float(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='1']
    two_8=[float(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='2']
    three_8=[float(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='3']

    count_one_4.update({i[-1]:'' for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='1'})
    count_two_4.update({i[-1]:'' for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='2'})
    count_three_4.update({i[-1]:'' for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='3'})
    count_one_8.update({i[-1]:'' for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='1'})
    count_two_8.update({i[-1]:'' for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='2'})
    count_three_8.update({i[-1]:'' for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='3'})
    n=np.matrix([[float(len(one_4)),float(len(two_4)),float(len(three_4))],[float(len(one_8)),float(len(two_8)),float(len(three_8))]])
    u=np.matrix([[np.mean(one_4),np.mean(two_4),np.mean(three_4)],[np.mean(one_8),np.mean(two_8),np.mean(three_8)]])
    s=np.matrix([[np.std(one_4,ddof=1),np.std(two_4,ddof=1),np.std(three_4,ddof=1)],\
                 [np.std(one_8,ddof=1),np.std(two_8,ddof=1),np.std(three_8,ddof=1)]])


    
    print formatting.format(labels[variable],\
                            str(round(np.mean(one_4),2))+'('+str(round(np.std(one_4,ddof=1),2))+')',\
                            str(round(np.mean(two_4),2))+'('+str(round(np.std(two_4,ddof=1),2))+')',\
                            str(round(np.mean(three_4),2))+'('+str(round(np.std(three_4,ddof=1),2))+')',\
                            str(round(np.mean(one_8),2))+'('+str(round(np.std(one_8,ddof=1),2))+')',\
                            str(round(np.mean(two_8),2))+'('+str(round(np.std(two_8,ddof=1),2))+')',\
                            str(round(np.mean(three_8),2))+'('+str(round(np.std(three_8,ddof=1),2))+')',\
                                                                  two_way(n,u,s)[0])
          
    print formatting.format('N',len(one_4),len(two_4),len(three_4),len(one_8),len(two_8),len(three_8),'')



print formatting.format('','$4','','','8$','','','F statistics')
print formatting.format('','One piece','Two pieces','Three pieces','One piece','Two pieces','Three pieces','Effect of')
print formatting.format('','','','','','','','price')


for variable in [ate_more_pizza, feel_guilty, physic_uncomf, overate, ate_more_general]:
    summary_slices(variable)

print formatting.format('Total N',len(count_one_4),len(count_two_4),len(count_three_4),len(count_one_8),len(count_two_8),len(count_three_8),'')



##########Table 3
formatting='{0:<40}{1:<12}{2:<12}{3:<8}{4:<12}{5:<12}{6:<8}{7:<12}{8:<12}{9:<8}'
def table_3_summary(variable):
    one_4=[float(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='1']
    two_4=[float(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='2']
    three_4=[float(i[variable]) for i in data[1:] if i[treatment]=='1' and i[variable]!='' and i[slice_cond]=='3']
    one_8=[float(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='1']
    two_8=[float(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='2']
    three_8=[float(i[variable]) for i in data[1:] if i[treatment]=='2' and i[variable]!='' and i[slice_cond]=='3']
    print formatting.format(labels[variable],\
                            str(round(np.mean(one_4),2))+'('+str(round(np.std(one_4,ddof=1),2))+')',\
                            str(round(np.mean(one_8),2))+'('+str(round(np.std(one_8,ddof=1),2))+')',\
                            round(one_way([np.mean(one_4),np.mean(one_8)],\
                                          [np.std(one_4,ddof=1),np.std(one_8,ddof=1)],\
                                          [len(one_4),len(one_8)]),2),\
                            str(round(np.mean(two_4),2))+'('+str(round(np.std(two_4,ddof=1),2))+')',\
                            str(round(np.mean(two_8),2))+'('+str(round(np.std(two_8,ddof=1),2))+')',\
                            round(one_way([np.mean(two_4),np.mean(two_8)],\
                                          [np.std(two_4,ddof=1),np.std(two_8,ddof=1)],\
                                          [len(two_4),len(two_8)]),2),\
                            str(round(np.mean(three_4),2))+'('+str(round(np.std(three_4,ddof=1),2))+')',\
                            str(round(np.mean(three_8),2))+'('+str(round(np.std(three_8,ddof=1),2))+')',\
                            round(one_way([np.mean(three_4),np.mean(three_8)],\
                                          [np.std(three_4,ddof=1),np.std(three_8,ddof=1)],\
                                          [len(three_4),len(three_8)]),2))
    print formatting.format('N',len(one_4),len(one_8),'',len(two_4),len(two_8),'',len(three_4),len(three_8),'')


print
print
print
print
print "Table 3"
print formatting.format('','1 Piece','','','2 Pieces','','','3 Pieces','','')
print formatting.format('','$4','$8','F test','$4','$8','F test','$4','$8','F test')
for variable in [ate_more_pizza, feel_guilty, physic_uncomf, overate, ate_more_general]:
    table_3_summary(variable)
