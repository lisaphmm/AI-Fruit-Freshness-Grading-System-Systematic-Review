import sys, json, math
sys.path.insert(0,'.')
from data import S, X
import numpy as np
from scipy import stats as st
from collections import Counter
ids=sorted(S)
n=len(ids)
def wilson(k,n,z=1.96):
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return round(100*(c-h),1), round(100*(c+h),1)
def pc(k,n=n): lo,hi=wilson(k,n); return f"{k} ({100*k/n:.1f}%, 95% CI {lo}-{hi})"
R={}
R['n']=n
R['year']=Counter(S[i]['year'] for i in ids)
R['tier']=Counter(S[i]['tier'] for i in ids)
R['task']=Counter(S[i]['task'] for i in ids)
R['fam']=Counter(S[i]['fam'] for i in ids)
dl=[i for i in ids if S[i]['fam'] in ('CNN','DET','SEG','TR','FM')]
R['dl']=len(dl)
R['mm']=sum(S[i]['mm'] for i in ids)
R['avail']=Counter(S[i]['avail'] for i in ids)
sp=Counter(('custard apple' if s=='sugar apple' else s) for i in ids for s in S[i]['species'])
R['species']=sp
R['pairings']=sum(len(S[i]['species']) for i in ids)
R['multi']=[i for i in ids if len(S[i]['species'])>1]
R['dec']=[i for i in ids if S[i]['dec']]
R['anch']=[i for i in ids if S[i]['anch']]
R['inc']=[i for i in ids if S[i]['inc']]
lv=Counter()
for i in ids:
    l=S[i]['levels']; lv['NR' if l is None else (str(l) if l<5 else '5+')]+=1
R['levels']=lv
# accuracy
A=[i for i in ids if S[i]['acc'] is not None]
acc=np.array([S[i]['acc'] for i in A])
R['nacc']=len(A)
R['med']=float(np.median(acc)); R['q1']=float(np.percentile(acc,25)); R['q3']=float(np.percentile(acc,75)); R['mn']=float(acc.min()); R['mx']=float(acc.max())
lvA=[i for i in A if S[i]['levels'] is not None]
rho,p=st.spearmanr([S[i]['levels'] for i in lvA],[S[i]['acc'] for i in lvA]); R['rho']=(round(rho,2),round(p,2),len(lvA))
def grp(i):
    l=S[i]['levels']; return '2' if l==2 else '3' if l==3 else '4' if l==4 else '5+'
g=[[S[i]['acc'] for i in lvA if grp(i)==k] for k in ['2','3','4','5+']]
R['kw_levels']=(round(st.kruskal(*g).pvalue,2),[len(x) for x in g])
tg=[[S[i]['acc'] for i in A if S[i]['tier']==t] for t in ['I','II','III']]
R['kw_tier']=(round(st.kruskal(*tg).pvalue,2),[len(x) for x in tg],[round(float(np.median(x)),1) for x in tg])
acc_dl=[S[i]["acc"] for i in A if i in dl]; acc_cl=[S[i]['acc'] for i in A if i not in dl]
R['mw']=(round(st.mannwhitneyu(acc_dl,acc_cl).pvalue,2),len(acc_dl),len(acc_cl),round(float(np.median(acc_dl)),1),round(float(np.median(acc_cl)),1))
# sensitivity: RGB only, no flag
B=[i for i in A if not S[i]['mm'] and not S[i]['flag']]
b=np.array([S[i]['acc'] for i in B]); R['sens']=(len(B),float(np.median(b)),float(np.percentile(b,25)),float(np.percentile(b,75)))
# QUADAS
dom=['D1','D2','D3','D4']
Q={i:dict(zip(['D1','D2','D3','D4','A1','A2','A3'],S[i]['qd'])) for i in ids}
def overall(q):
    ds=[q[d] for d in dom]
    return 'H' if 'H' in ds else ('L' if all(x=='L' for x in ds) else 'U')
for i in ids: Q[i]['O']=overall(Q[i])
R['qd']={k:Counter(Q[i][k] for i in ids) for k in ['D1','D2','D3','D4','O','A1','A2','A3']}
# sample size
N=[S[i]['N'] for i in ids if S[i]['N']]
R['N']=(len(N),float(np.median(N)),float(np.percentile(N,25)),float(np.percentile(N,75)),sum(x<500 for x in N),sum(x<250 for x in N),min(N))
# delta
delta=[('P015','Rotation + zoom (synthetic)',95.1,92.7),('P015','Rotation + zoom + brightness (synthetic)',95.1,90.2),
 ('P017','Apple: offline hold-out vs run-time test',99.2,96.7),('P017','Banana: offline hold-out vs run-time test',98.6,93.8),
 ('P029','Conveyor speed -50%',94.0,95.6),('P029','Conveyor speed +25%',94.0,89.6)]
dd=[round(a-b,1) for _,_,a,b in delta]
R['delta']=dd; R['dmed']=float(np.median(dd))
R['Q']=Q
json.dump({k:(dict(v) if isinstance(v,Counter) else v) for k,v in R.items() if k!='Q'},open('stats.json','w'),default=str,indent=1)
if __name__=='__main__':
    for k,v in R.items():
        if k!='Q': print(k,v)
    print(pc(R['tier']['II']+R['tier']['III']), pc(R['mm']), pc(len(R['dec'])), pc(R['task']['F']))
