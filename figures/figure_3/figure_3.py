#must be run from command line to get the path to the data file correct
import numpy as np
import pylab as plt


import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

f=open(os.path.join(BASE_DIR,'pizzastudy.txt'))
data=[i.strip().split('\t') for i in f]

#get indexes of columns
pizza=data[0].index('pieces')


counts={}
pizza=[float(i[pizza]) for i in data[1:] if i[pizza]!='']
for i in pizza:
    counts[i]=counts.get(i,0)+1
mylist=zip(counts.keys(),counts.values())
fig=plt.figure(figsize=(22.62372, 12))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.2)

ax.bar([i[0] for i in mylist],[i[1] for i in mylist],color='b',width=.1,linewidth=1.0,align='center')

for item in ax.get_yticklabels():
    item.set_fontsize(15)

for item in ax.get_xticklabels():
    item.set_fontsize(15)

ax.tick_params(axis='x',length=0,width=0,direction='out',labelsize=25)
ax.tick_params(axis='y',length=0,width=0,direction='out',labelsize=25)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['bottom'].set_position(['outward',0])
ax.spines['left'].set_position(['outward',0])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticks(range(14))
ax.set_ylabel('Count',fontsize=40,labelpad=20)
ax.set_xlabel('Pieces of Pizza',fontsize=40,labelpad=20)
ax.set_xlim(-.15,8.15)
ax.set_ylim(0,40)
plt.savefig('figure_3.pdf')
plt.show()
