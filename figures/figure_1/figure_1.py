import numpy as np
import pylab as plt
from matplotlib.patches import Ellipse


fig=plt.figure(figsize=(22.62372, 12))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.2)
font1={'family':'Arial',
            'color'  : 'b',
            'weight' : 'normal',
            'size'   : 30,
            }

font2={'family':'Arial',
            'color'  : 'k',
            'weight' : 'normal',
            'size'   : 30,
            }
font3={'family':'Arial',
            'color'  : 'r',
            'weight' : 'normal',
            'size'   : 40,
            }

x=np.arange(.001,3,.001)

ax.plot(x,1/x,color='k',lw=3)
data=np.array([.2,2])
ax.scatter(data,1/data,s=100,color='b',zorder=100)
ax.plot(data,1/data,'b--',lw=3)
width=(12/22.62372)/(6/(3-.05))
height=1.0
circ=Ellipse((np.mean(data),np.mean(1/data)),width=width/5,height=height/5, color='b',zorder=1000)
ax.add_artist(circ)
circ=Ellipse((np.mean(data),1/np.mean(data)),width=width/5,height=height/5, color='k',zorder=1000)
ax.add_artist(circ)
ax.vlines([np.mean(data)],[1/np.mean(data)],[np.mean(1/data)],color='r',linestyle='dashed',lw=3)
ax.text(1.075,2.9,"Mean of transformations",fontdict=font1)
ax.text(.375,.6,"Transformation of mean",fontdict=font2)
ax.text(1,2,"Error",fontdict=font3,rotation=90)
ax.text(.22,1/.2,"$x_1$",fontdict=font1)
ax.text(2,.56,"$x_2$",fontdict=font1)

for item in ax.get_yticklabels():
    item.set_fontsize(15)

for item in ax.get_xticklabels():
    item.set_fontsize(15)

ax.tick_params(axis='x',length=0,width=0,direction='out',labelsize=0)
ax.tick_params(axis='y',length=0,width=0,direction='out',labelsize=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['bottom'].set_position(['outward',0])
ax.spines['left'].set_position(['outward',0])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticks(range(14))
ax.set_ylabel('Transformed Data',fontsize=40,labelpad=20)
ax.set_xlabel('Original Data',fontsize=40,labelpad=20)
ax.set_xlim(0.05,3)
ax.set_ylim(0,6)
plt.savefig('figure_1.pdf')
plt.show()
