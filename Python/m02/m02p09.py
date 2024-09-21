#!/usr/bin/python

lines = []

lines.append(' '*12+'*'*7)
lines.append(' '*10+'*'*2+' '*7+'*'*2)
lines.append(' '*9+'*'*1+' '*11+'*'*1)
lines.append(' '*7+'*'*2+' '*13+'*'*2)
lines.append(' '*6+'*'*1+' '*17+'*'*1)
lines.append(' '*5+'*'*1+' '*19+'*'*1)
lines.append(' '*4+'*'*1+' '*21+'*'*1)
lines.append(' '*3+'*'*1+' '*23+'*'*1)
lines.append(' '*2+'*'*1+' '*25+'*'*1)
lines.append(' '*1+'*'*1+' '*27+'*'*1)

for line in lines:
    print line

print '*'*1 + '-'*29 + '*'*1 + '-'*29

lines.reverse()
for line in lines:
    print ' '*29,
    print line



