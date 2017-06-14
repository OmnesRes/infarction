from functions import *

#this script does some miscellaneous analyses that appear in the text or tables


###check frequency of groups matches article 1

counts={}
for i in data[1:]:
    counts[i[group]]=counts.get(i[group],0)+1

print sorted(zip(counts.keys(),counts.values()))


print
###check how many people with 0 pieces eaten have ratings for pizza
countlessthan1=0
countratings=0


for i in data[1:]:
    if i[pieces]!='' and float(i[pieces])<1:
        countlessthan1+=1
        if i[taste_general] or i[taste_first] or i[sat_first] or i[enj_first] or i[taste_middle]\
           or i[sat_middle] or i[enj_middle] or i[taste_last] or i[sat_last] or i[enj_last]:
            countratings+=1

print 'less than 1'
print countlessthan1
print countratings
print float(countratings)/countlessthan1

print

###check how many people with 1 pieces eaten have ratings they shouldn't
count1=0
count_1_ratings=0

for i in data[1:]:
    if i[pieces]!='' and 1<=float(i[pieces])<2:
        count1+=1
        if i[taste_middle] or i[sat_middle] or i[enj_middle] or i[taste_last] or i[sat_last] or i[enj_last]:
            count_1_ratings+=1

print '1 <= but less than 2'
print count1
print count_1_ratings
print float(count_1_ratings)/count1

print
###check how many people with 2 pieces eaten have ratings they shouldn't

count2=0
count_2_ratings=0


for i in data[1:]:
    if i[pieces]!='' and 2<=float(i[pieces])<3:
        count2+=1
        if i[taste_middle] or i[sat_middle] or i[enj_middle]:
            count_2_ratings+=1

print '2 <= but less than 3'
print count2
print count_2_ratings
print float(count_2_ratings)/count2

###check how many people with missing response for pieces have ratings

count_empty=0
count_empty_ratings=0

for i in data[1:]:
    if i[pieces]=='':
        count_empty+=1
        if i[taste_general] or i[taste_first] or i[sat_first] or i[enj_first] or i[taste_middle]\
           or i[sat_middle] or i[enj_middle] or i[taste_last] or i[sat_last] or i[enj_last]:
            count_empty_ratings+=1

print 'empty'
print count_empty
print count_empty_ratings
        
print
##check the pieces and salad eaten for diners reporting 1 or less calories

count=0

for i in data[1:]:
    if i[calories]!='':
        if float(i[calories])<=1:
            count+=1
            print i[pieces],i[salad]

print count













    
