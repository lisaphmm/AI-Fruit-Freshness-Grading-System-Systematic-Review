import sys; sys.path.insert(0,'.')
from stats import *
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8.5,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#8a8985','axes.labelcolor':'#3d3c3a','xtick.color':'#3d3c3a','ytick.color':'#3d3c3a'})
B,O,Aq,GR='#2a78d6','#eb6834','#1baf7a','#b9b8b2'
def save(f,n): f.savefig(f'../figures/{n}.png',dpi=200,bbox_inches='tight',facecolor='white'); plt.close(f)
# Fig2
yrs=sorted(R['year']); f,ax=plt.subplots(1,2,figsize=(7,2.6))
bot=np.zeros(len(yrs))
for t,col in zip(["I","II","III"],[B,O,Aq]):
    v=np.array([sum(1 for i in ids if S[i]['year']==y and S[i]['tier']==t) for y in yrs]); ax[0].bar(yrs,v,bottom=bot,color=col,label=f'Tier {t}',width=.7,edgecolor='white',linewidth=1); bot+=v
ax[0].set_title('(a) By evidence tier',loc='left',fontsize=9); ax[0].set_ylabel('Studies'); ax[0].legend(frameon=False,fontsize=7.5)
bot=np.zeros(len(yrs))
for lab,col,cond in [('Deep learning',B,lambda i:i in dl),('Classical ML',O,lambda i:i not in dl)]:
    v=np.array([sum(1 for i in ids if S[i]['year']==y and cond(i)) for y in yrs]); ax[1].bar(yrs,v,bottom=bot,color=col,label=lab,width=.7,edgecolor='white',linewidth=1); bot+=v
ax[1].set_title('(b) By model family',loc='left',fontsize=9); ax[1].legend(frameon=False,fontsize=7.5)
for a in ax: a.set_xticks(yrs); a.tick_params(axis='x',labelrotation=45)
f.tight_layout(); save(f,'fig2')
# Fig3
f,ax=plt.subplots(1,3,figsize=(7.4,3.1),gridspec_kw={'width_ratios':[1.3,1,1]})
sp_=sorted(R['species'].items(),key=lambda x:(x[1],x[0])); sp_=[x for x in sp_ if x[1]>=1]
ax[0].barh([k for k,_ in sp_],[v for _,v in sp_],color=B,height=.7); ax[0].set_title('(a) Studies per fruit',loc='left',fontsize=9); ax[0].tick_params(axis='y',labelsize=6.5)
names={'CNN':'CNN classifier','CL':'Classical ML','DET':'Object detector','SEG':'Segmentation','TR':'Swin-based','FM':'Foundation model'}
fm=sorted(R['fam'].items(),key=lambda x:x[1]); ax[1].barh([names[k] for k,_ in fm],[v for _,v in fm],color=O,height=.7); ax[1].set_title('(b) Model family',loc='left',fontsize=9)
tn={'M':'Maturity /\nripeness','Q':'Quality /\ndefect','F':'Freshness /\ndecay'}
ax[2].barh([tn[k] for k in 'MQF'],[R['task'][k] for k in 'MQF'],color=Aq,height=.7); ax[2].set_title('(c) Primary task',loc='left',fontsize=9)
f.tight_layout(); save(f,'fig3')
# Fig4
f,ax=plt.subplots(1,3,figsize=(7.4,2.9),sharey=True)
rng=np.random.default_rng(1)
def strip(a,groups,labels,color):
    for k,g in enumerate(groups):
        a.scatter(k+rng.uniform(-.15,.15,len(g)),g,s=16,color=color,alpha=.85,edgecolor='white',linewidth=.5)
        if g: a.hlines(np.median(g),k-.3,k+.3,color='#0b0b0b',lw=1.5)
    a.set_xticks(range(len(labels))); a.set_xticklabels([f'{l}\n(n={len(g)})' for l,g in zip(labels,groups)],fontsize=7)
strip(ax[0],g,['2','3','4','5+'],B); ax[0].set_title('(a) Decision levels',loc='left',fontsize=9); ax[0].set_ylabel('Best reported accuracy (%)')
strip(ax[1],tg,['I','II','III'],O); ax[1].set_title('(b) Evidence tier',loc='left',fontsize=9)
strip(ax[2],[acc_dl,acc_cl],['Deep\nlearning','Classical\nML'],Aq); ax[2].set_title('(c) Model family',loc='left',fontsize=9)
f.tight_layout(); save(f,'fig4')
# Fig5
f,ax=plt.subplots(1,2,figsize=(7,2.7),gridspec_kw={'width_ratios':[1,1.5]})
cats=['Paired\nvalues','Compared,\nno pairs','Not\ncompared']
vals=[4,3,n-7]; ax[0].bar(cats,vals,color=[B,O,GR],width=.6); ax[0].set_title('(a) Acquisition-shift evidence',loc='left',fontsize=9); ax[0].tick_params(axis='x',labelsize=6.5)
for x,v in enumerate(vals): ax[0].text(x,v+.6,str(v),ha='center',fontsize=8)
labs=[f"{S[p]['cite'].split(' (')[0]}: {l}" for p,l,_,_ in delta]
ax[1].barh(range(6)[::-1],dd,color=[B if x>=0 else Aq for x in dd],height=.6); ax[1].set_yticks(range(6)[::-1]); ax[1].set_yticklabels(labs,fontsize=6.3)
ax[1].axvline(0,color='#52514e',lw=.8); ax[1].set_xlabel('Δ accuracy, percentage points (in-distribution − shifted)'); ax[1].set_title('(b) Paired Δ',loc='left',fontsize=9)
f.tight_layout(); save(f,'fig5')
# Fig6
f,ax=plt.subplots(1,2,figsize=(7.4,3.0))
cl={'L':Aq,'U':GR,'H':O}
def stack(a,keys,labels,title):
    for r,(k,lab) in enumerate(zip(keys,labels)):
        left=0
        for lv in 'LUH':
            v=100*R['qd'][k][lv]/n; a.barh(len(keys)-1-r,v,left=left,color=cl[lv],height=.62,edgecolor='white',linewidth=1,label={'L':'Low','U':'Unclear','H':'High'}[lv] if r==0 else None)
            if v>7: a.text(left+v/2,len(keys)-1-r,f'{v:.0f}',ha='center',va='center',fontsize=7,color='white' if lv!='U' else '#0b0b0b')
            left+=v
    a.set_yticks(range(len(keys))); a.set_yticklabels(labels[::-1],fontsize=7.5); a.set_xlim(0,100); a.set_xlabel('% of studies'); a.set_title(title,loc='left',fontsize=9)
stack(ax[0],['D1','D2','D3','D4','O'],['D1 Sample','D2 Index test','D3 Reference','D4 Flow','Overall'],'(a) Risk of bias'); ax[0].legend(frameon=False,fontsize=7,ncol=3,loc='upper center',bbox_to_anchor=(.5,-.22))
stack(ax[1],['A1','A2','A3'],['A1 Sample / setting','A2 Index test','A3 Target condition'],'(b) Applicability concerns')
f.tight_layout(); save(f,'fig6')
# Fig7
Nv=[S[i]['N'] for i in ids if S[i]['N']]
f,ax=plt.subplots(figsize=(4.6,2.6)); bins=np.logspace(1.5,5,12); ax.hist(Nv,bins=bins,color=B,edgecolor='white'); ax.set_xscale('log')
ax.axvline(np.median(Nv),color='#0b0b0b',ls='--',lw=1); ax.text(np.median(Nv)*1.08,ax.get_ylim()[1]*1.0,f'median {np.median(Nv):,.0f}',fontsize=7.5)
ax.set_xlabel('Reported sample size (original images, fruit or observations; log scale)'); ax.set_ylabel('Studies'); f.tight_layout(); save(f,'fig7')
# Fig1 PRISMA
f,ax=plt.subplots(figsize=(6.4,6.6)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,12)
def box(x,y,w,h,t,fc='#eef3fb'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.1',fc=fc,ec='#52514e',lw=.8)); ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=7.2,wrap=True)
def arr(x1,y1,x2,y2): ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color='#52514e',lw=.9))
box(.3,10.3,5.2,1.4,'Records identified from databases (n = 173)\nPubMed n = 21; Embase n = 31; Scopus n = 121')
box(.3,8.4,5.2,1.1,'Records screened by title and abstract\n(n = 168)'); box(5.9,8.4,4.0,1.1,'Duplicate records removed\n(n = 5)',fc='#f5f4f1')
box(.3,6.3,5.2,1.3,'Reports assessed against full criteria\nand extracted (n = 60)'); box(5.9,6.3,4.0,1.3,'Excluded at title/abstract\nscreening (n = 108)',fc='#f5f4f1')
box(5.9,3.0,4.0,2.5,'Excluded at full-text stage (n = 19)\nNot fruit-surface image input (n = 11)\nOutcome out of scope (n = 4)\nNo original model/metric (n = 2)\nOutside 2016–2026 (n = 2)',fc='#fdf0ea')
box(.3,3.6,5.2,1.5,'Studies included in qualitative\nsynthesis (n = 41)',fc='#e8f6f0')
box(.3,1.3,5.2,1.6,'RQ2 subset: acquisition shift compared\n(n = 7); paired accuracy/error (n = 4);\npaired accuracy usable for Δ (n = 3)',fc='#e8f6f0')
arr(2.9,10.3,2.9,9.5); arr(5.5,8.95,5.9,8.95); arr(2.9,8.4,2.9,7.6); arr(5.5,6.95,5.9,6.95); arr(2.9,6.3,2.9,5.1); arr(5.5,4.25,5.9,4.25); arr(2.9,3.6,2.9,2.9)
ax.text(.3,0.6,'Per-database split of the 60 assessed reports to be confirmed from the reference manager.',fontsize=7,style='italic',color='#52514e')
save(f,'fig1')
