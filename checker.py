import sys,os,re


def tokenek(nev):
  f=open(nev)
  d=f.read().split()
  f.close()
  return [v.strip() for v in d if len(v.strip())>0 ] #paranoia

def testit(d,t):

  if len(d)!=len(t):
    return('length error')

  for sd,st in zip(d,t):
    akt=str
    while True:
      try:
        int(st)
        akt=int
        break
      except:
        pass

      try:
        float(st)
        akt=float
        break
      except:
        pass
      break

    try:
      akt(sd)
    except:
      return('type error')

    vt=akt(st)
    vd=akt(sd)

    while True:
      if akt==str:
        if vt!=vd:
          return('string error')
      if akt==int:
        if vt!=vd:
          return('integer error')
      if akt==float:
        if abs(vt-vd)>1e-6:
          return('float error')
      break
  return('ok')




try:
  open('main.py').close()
except:
  print('main.py not found')
  exit(1)

if not os.path.isdir('io'):
  print('io dir not found')
  exit(1)


myfiles=os.scandir('io/')
for inp in myfiles:
  if inp.is_file() and inp.name[0:2]=='in':
    print('testing {0:s} '.format(inp.name),end='')
    num=int(inp.name[2:])
    cmd='python3 main.py < io/{:s} > o'.format(inp.name)
    res=os.system(cmd)
    if res!=0:
      print('runtime error')
      continue

    outp='io/out{:d}'.format(num)
    print(testit(tokenek('o'),tokenek(outp)))
