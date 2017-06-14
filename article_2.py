##load necessary functions and modules
from functions import *
from sklearn import linear_model


##reproduce the original statistics for Table 2, half-price, beginning, end, total
print 'Reproducing some of the original stats for Table 2'
print

print '$4 beginning model'
temp_overall=[] #dependent variable
temp_first=[] #predictor
for i in data[1:]:
    if i[treatment]=='1': #include all responses, even impossible ones
        if i[taste_general]!='' and i[taste_first]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_first.append(float(i[taste_first]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_first)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste first coeff= '+str(round(regr.coef_[0],2))


print
print '$4 end model'
temp_overall=[] #dependent variable
temp_last=[] #predictor
for i in data[1:]:
    if i[treatment]=='1': #include all responses, even impossible ones
        if i[taste_general]!='' and i[taste_last]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_last.append(float(i[taste_last]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_last)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste last coeff= '+str(round(regr.coef_[0],2))


temp_overall=[] #dependent variable
temp_first=[] #predictor
temp_middle=[] #predictor
temp_last=[] #predictor
print
print '$4 total model'
for i in data[1:]:
    if i[treatment]=='1': #include all responses, even impossible ones
        if i[taste_general]!='' and i[taste_first]!='' and i[taste_middle]!='' and i[taste_last]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_first.append(float(i[taste_first]))
            temp_middle.append(float(i[taste_middle]))
            temp_last.append(float(i[taste_last]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_first,temp_middle,temp_last)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste first coeff= '+str(round(regr.coef_[0],2))
print 'taste middle coeff= '+str(round(regr.coef_[1],2))
print 'taste last coeff= '+str(round(regr.coef_[2],2))
print
print
print



##Show how to provide correct statistics for Table 2, half-price, beginning
print 'Showing how to calculate correct stats for Table 2'
print
print '$4 beginning model'
temp_overall=[] #dependent variable
temp_first=[] #predictor
for i in data[1:]:
    if i[treatment]=='1' and my_filter(i,0): #exclude diners who ate no pizza or did not provide a response
        if i[taste_general]!='' and i[taste_first]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_first.append(float(i[taste_first]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_first)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste first coeff= '+str(round(regr.coef_[0],2))


print
print '$4 end model'
temp_overall=[] #dependent variable
temp_last=[] #predictor
for i in data[1:]:
    if i[treatment]=='1' and my_filter(i,1): #exclude diners who ate 1 or less pizza or did not provide a response
        if i[taste_general]!='' and i[taste_last]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_last.append(float(i[taste_last]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_last)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste last coeff= '+str(round(regr.coef_[0],2))


temp_overall=[] #dependent variable
temp_first=[] #predictor
temp_middle=[] #predictor
temp_last=[] #predictor
print
print '$4 total model'
for i in data[1:]:
    if i[treatment]=='1' and my_filter(i,2): ##exclude diners who ate 2 or less pizza or did not provide a response
        if i[taste_general]!='' and i[taste_first]!='' and i[taste_middle]!='' and i[taste_last]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_first.append(float(i[taste_first]))
            temp_middle.append(float(i[taste_middle]))
            temp_last.append(float(i[taste_last]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_first,temp_middle,temp_last)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste first coeff= '+str(round(regr.coef_[0],2))
print 'taste middle coeff= '+str(round(regr.coef_[1],2))
print 'taste last coeff= '+str(round(regr.coef_[2],2))
print
print
print



##to reproduce the STATA output the filtering function has to be changed to return True when diners did not report how much pizza they ate
def my_filter(i,lower):
    if i[pieces]!='':
        if float(i[pieces])>lower:
            return True
        else:
            return False
    else:
        return True



##Show how to reproduce STATA output for Table 2, half-price, beginning
print 'Showing how to reproduce the STATA output for Table 2'
print
print '$4 beginning model'
temp_overall=[] #dependent variable
temp_first=[] #predictor
for i in data[1:]:
    if i[treatment]=='1' and my_filter(i,0): #exclude diners who ate no pizza, include those that did not provide a response
        if i[taste_general]!='' and i[taste_first]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_first.append(float(i[taste_first]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_first)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste first coeff= '+str(round(regr.coef_[0],2))


print
print '$4 end model'
temp_overall=[] #dependent variable
temp_last=[] #predictor
for i in data[1:]:
    if i[treatment]=='1' and my_filter(i,1): #exclude diners who ate 1 or less pizza, include those that did not provide a response
        if i[taste_general]!='' and i[taste_last]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_last.append(float(i[taste_last]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_last)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste last coeff= '+str(round(regr.coef_[0],2))


temp_overall=[] #dependent variable
temp_first=[] #predictor
temp_middle=[] #predictor
temp_last=[] #predictor
print
print '$4 total model'
for i in data[1:]:
    if i[treatment]=='1' and my_filter(i,2): ##exclude diners who ate 2 or less pizza, include those that did not provide a response
        if i[taste_general]!='' and i[taste_first]!='' and i[taste_middle]!='' and i[taste_last]!='': #model can't run with missing data
            temp_overall.append(float(i[taste_general]))
            temp_first.append(float(i[taste_first]))
            temp_middle.append(float(i[taste_middle]))
            temp_last.append(float(i[taste_last]))
regr = linear_model.LinearRegression()
regr.fit(np.array(zip(temp_first,temp_middle,temp_last)),temp_overall)
print 'N= '+str(len(temp_overall))
print 'taste first coeff= '+str(round(regr.coef_[0],2))
print 'taste middle coeff= '+str(round(regr.coef_[1],2))
print 'taste last coeff= '+str(round(regr.coef_[2],2))
