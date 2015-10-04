from __future__ import print_function
import os
import sys
import glob
import pylab as pl
import numpy as np

myvars = ['total', 'percent', 'employed', 'stipend']


def finddata(strg=None):
    if not strg:
        return glob.glob('*male*.dat')
    return glob.glob('*%s*'%strg)


def readdata(files):
    nf = len(files)
    alldata={'female' : {}, 'male' : {}}
    for fl in files:
        gender = 'male'
        if 'female' in fl:
            gender = 'female'
        thisfl = np.array(open(fl, 'r').readlines())
        education={}
        i=0
        for thisl in thisfl:
            if not thisl[0].isdigit() and not thisl.split('  ')[0] in education.values():
                education[i] = thisl.split('  ')[0]
                i=i+1
        agekeys = set([thisl.split('  ')[0] for thisl in thisfl if thisl[0].isdigit()])
        edkey = set([thisl.split('  ')[0] for thisl in thisfl if not thisl[0].isdigit()])
        #print (edkey, education)
        for k in agekeys:
            alldata[gender][k] = {}
            for kk in edkey:
                alldata[gender][k][kk] = {'total': None, 'percent': None, 'percent_employed': None, 'stipend': None}
        for l in thisfl:
            lsplit = l.split('  ')
            #lsplit.remove(' ')
            #print ("here1", lsplit, [i for i in range(len(lsplit)) if not lsplit[i] == '' ])
            indeces = [i for i in range(len(lsplit)) if not lsplit[i] == '' ]
            lsplit = np.array(lsplit)[indeces]
            #print ("here2", lsplit)
            k1 = lsplit[0]
            if k1 in agekeys: ak = k1
            elif k1 in edkey:
                #print (lsplit)
                alldata[gender][ak][k1]['total'] = float(lsplit[1].replace(',',''))
                alldata[gender][ak][k1]['percent'] = float(lsplit[2])
                alldata[gender][ak][k1]['employed'] = float(lsplit[5].replace(',',''))
                alldata[gender][ak][k1]['stipend'] = float(lsplit[7].replace('$','').replace(',',''))

    #print (alldata[gender][ak][k1]['employed'])
    return (alldata, education)

def chisq(data, error, model):
    print ("data", data, "model", model, "er", error)
    return sum(((data - model)**2)/error**2)

def dofchisq(data, error, model, dof):
    return sum(((data - model)**2)/error**2)/dof

def fitdata(x, y, e, c = 1.0, ax = None):
    #print (y, e)
    fit1 = np.polyfit(x, y, 1)
    fit2 = np.polyfit(x, y, 2)
    #print (ax)
    if ax:
        tmpx=np.linspace(min(x), max(x), 100)
        ax.plot(tmpx, np.poly1d(fit1)(tmpx)*c, 'k--')
        ax.plot(tmpx, np.poly1d(fit2)(tmpx)*c, 'k-.')
    chisq1 = chisq(y, e, np.poly1d(fit1)(x))
    chisq2 = chisq(y, e, np.poly1d(fit2)(x))
    dofchisq1 = dofchisq(y, e, np.poly1d(fit1)(x), len(y)-1)
    dofchisq2 = dofchisq(y, e, np.poly1d(fit2)(x), len(y)-2)
    return chisq1/len(x), chisq2/len(x), dofchisq1/len(x), dofchisq2/len(x), fit1, fit2

def best(c, fit1, fit2):
    if c<0: return "linear model is better: y = %.2f + %.2fx"%(fit1[0], fit1[1])
    if c>0: return "quadratic model is better: y = %.2f + %.2fx + %2fx^2"%(fit2[0], fit2[1], fit2[2])

def plotdata(mydata, education, fitme=False):
    for k in mydata:
        print (k)
        fig = pl.figure(figsize=(15,10))
        fig.suptitle(k)
        for i,v in enumerate(myvars):
            ax=fig.add_subplot(2,2,i)
            for age in mydata[k]:
                #print (education.keys(), [mydata[k][age][education[e]] for e in education.keys()])
                ax.plot(education.keys(), np.array([mydata[k][age][education[e]][v] for e in education.keys()]),
                        'o', label=age.replace(' years','').replace(' to ','-'))
                yhere = np.array([mydata[k][age][education[e]][v] for e in education.keys()]).astype(float)
                ax.errorbar(education.keys(), yhere,
                                    np.sqrt(yhere),
                                    fmt = '.')
                #print (yhere/sum(yhere))
                if fitme:
                    allchisq = fitdata(education.keys(),  yhere/sum(yhere),
                        np.sqrt(yhere)/sum(yhere), c = sum(yhere), ax = ax)
                    chisq = allchisq[:2]
                    dofchisq = allchisq[2:]
                    if v == 'stipend' or v == 'employed':
                        print (k, 'age:', age.replace(' years','').replace(' to ','-'),
                            'variable: ', v, ' %.2f'%(chisq[0]-chisq[1]), best(chisq[0]-chisq[1], allchisq[-2], allchisq[-1]),
                            ' %.2f'%(dofchisq[0]-dofchisq[1]), best(dofchisq[0]-dofchisq[1], allchisq[-2], allchisq[-1]))
            ax.set_xlabel('education level')
            ax.set_ylabel(v)
            ax.legend(ncol=4, numpoints=1)
        pl.show()



if __name__ == '__main__':
    fls = finddata()
    dt, education = readdata(fls)
    plotdata(dt, education, fitme = True)