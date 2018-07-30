# py 3.6.2 | win32(intel)
from random import *
from text import *
f = open('NLSSC.txt', 'r'); r = f.read(); sf = r.split('\n')
def init():
    choice = input(''+z0); chp = str(choice)
    if chp is "1": main(1)
    elif chp is "2": main(2)
    else:
        print(''+z1); bk(); init()
def main(mm):
    global sf
    rv = randrange(0, len(sf)-1); cu = sf[rv]; fp = cu.split(' - '); main(mm) if len(cu)<1 else None
    (main(mm) if ('[01]' in fp[0]) else None) if (mm is 1) else None
    g = fp[2].split(', '); bk(); fg = g[-1]; ts = fg[fg.find("["):fg.find("]")+1]; print(''+z4+fp[0]+z5+fp[1])
    for x in range(0, len(g)):
        p = [" "+str(x+1)+' - ']
        (p.append(g[x])) if (x<len(g)-1) else (
            (p.append((g[x])[0:(g[x]).find("[")])) if ('[' in g[x]) else (p.append(g[x])))
        print(''.join(p)); del p
    print(''+z6+ts) if len(ts)>0 else None; nd = input(''+z7)
    if nd == 'no':
        print(''+h0); main(mm)
    elif nd == 'back':
        bk(); init()
    elif nd == 'yes':
        fp[0] = '[01]'; print(''+h1);cu = fp[0]+' - '+fp[1]+' - '+fp[2];
        vi = fp[1]; di = vi[vi.find('(')+1:vi.find(')')]; dr = di.split(' ')
        if ',' in dr[1]:
            dd = list(dr[1])
            if dd[-2] == '1': dd.insert(-1, 'st')
            elif dd[-2] == '2': dd.insert(-1, 'nd')
            elif dd[-2] == '3': dd.insert(-1, 'rd')
            else: dd.insert(-1, 'th')
        r = ''; i = (dateParse(dr[0])+'%2F'+(dr[1])[0:-1]+'%2F'+dateParse(dr[2]))
        if ' N (' in (fp)[1]:
            i_ = input(''+h2)
            if '1' in i_:
                dr[1] = ''
                for x in range(0,len(dd)): dr[1] += dd[x]
                j = (dr[0]+'+'+dr[1]+'+'+dr[2])
                input(''+h3+j+']\n')
            else: input(''+h4+i+'%5D"\n')
        else:
            dr[1] = ''
            for x in range(0,len(dd)): dr[1] += dd[x]
            j = (dr[0]+'+'+dr[1]+'+'+dr[2])
            input(''+h3+j+']\n')
        for x in range(0, len(sf)): r += (sf[x]+'\n')
        j_ = input(''+h5)
        if j_ == 'yes':
            print(''+h6); f.close(); k = open('NLSSC.txt','w')
            k.truncate(); k.write(r); k.close(); bk(); k_ = input(''+h7)
            main(mm) if k_ == "yes" else quit()
        else:
            print(''+a0); main(mm)
    else:
        print(''+a1); main(mm)
def bk():
    print('\n-------------------------------------------\n')
def dateParse(v):
    dkey = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
               'October':10,'November':11,'December':12,'2013':13,'2014':14,'2015':15,'2016':16,'2017':17,'2018':18}
    if (v in dkey): return str(dkey[v])
init()
