#coding=utf-8
#windows-1252, ASCII, cp1252, GBK, ISO8859-1, ISO8859-15, JIS, UCS-2, UCS-4, UTF-8, UTF-16 and UTF-32.
from surreal import *

a=Surreal(set(),set()) # dali(0) shorthand(0) shorthand('{|}')
b=Surreal(set(),set([a]))
r=Surreal(set([a]),set())

add_dali(a,0)
add_dali(b,-1)
add_dali(r,1)

print 'Day 0:'
print 'a = ', a
print 'a<=a', a<=a
print

print 'Day 1:'
print 'b = ', b
print 'r = ', r
print 'b<=a', b<=a
print 'b<=r', b<=r
print 'a<=r', a<=r
print

print '+ :'
x = a+a
print 'x = a+a =', x, ', x == a', x==a
x = a+r
print 'x = a+r =', x, ', a+r == r', x==r
x = a+b
print 'x = a+b =', x, ', a+b == b', x==b
x = r+b
print 'x = r+b =', x, ', r+b==a', x==a
print

print '- :'
print '-a', -a, ', a==-a', a==-a
print '-b', -b, ', -b==r', -b==r
print '-r', -r, ', -r==b', -r==b
x=r-r
print 'x = r-r =', x, ', a==x', a==x
x=b-b
print 'x = b-b =', x, ', a==x', a==x
print

print '* :'
print 'a*a =', a*a, '==a', a==(a*a)
print 'a*r =', a*r, '==a', a==(a*r)
print 'r*r =', r*r, '==r', r==(r*r)
print 'b*b =', b*b, '==r', r==b*b
print 'b*r =', b*r, '==b', b==b*r
print

print 'Day 2:'
leftSet = set([a])
rightSet = set([r])
c=Surreal(leftSet, rightSet)    # {0|1},    1/2
add_dali(c, 0.5)
add_dali(-c, -0.5)

leftSet = set([r])
rightSet = set()
d=Surreal(leftSet, rightSet)     # {1|},     2
add_dali(d, 2)
add_dali(-d, -2)
print 'c = {0|1}', c
print 'd = {1|}', d
print

x=c*d
y=c+c
print 'verifying 2*(1/2) and 1/2 + 1/2'
print 'x = {1|}*{0|1} =', x
print 'y = {0|1}+{0|1} =', y
print 'x==y', x==y
print 'x==r', x==r
print

print 'Day 3:'

leftSet = set([a])
rightSet = set([c])
e=Surreal(leftSet, rightSet)
add_dali(e, 0.25)
add_dali(-e, -0.25)
print 'e = {0|1/2} = 1/4', e

leftSet = set([c])
rightSet = set([r])
f=Surreal(leftSet, rightSet)
add_dali(f, 0.75)
add_dali(-f, -0.75)
print 'f = {1/2|1} = 3/4', f

leftSet = set([r])
rightSet = set([d])
g=Surreal(leftSet, rightSet)
add_dali(g, 1.5)
add_dali(-g, -1.5)
print 'g = {1|2} = 3/2', g

leftSet = set([d])
rightSet = set()
h=Surreal(leftSet, rightSet)
add_dali(h, 3)
add_dali(-h, -3)
print 'h = {2|} = 3', h

print
print 'other ...'
x=Surreal(set([c]),set([r+c]))
print 'x = { 1/2, 1+1/2 }=', x
print 'x==r', x==r
print 'dali(x)', dali(x)

print
print '# day0:                     0,a'
print '# day1:         -1,b                       1,r'
print '# day2:    -2,       -1/2,        1/2,c          2,d'
print '# day3: -3, -3/2, -3/4, -1/4, 1/4,e  3/4,f   3/2,g  3,h'
print 'dali(c+r)', dali(c+r)
print 'dali(c+g)', dali(c+g)
print 'dali(e+f)', dali(e+f)
print 'dali(e+c)', dali(e+c)
print 'dali(e+e+e)', dali(e+e+e)
print 's(0.5)', s(0.5)


#{1 |1 1/2} * {1/2 |1/2}
#Surreal(set([e]),set([e+r]))*(e+e)

# construre pseudo number, as {0|0}
# broke Atom1 but obey Atom2
star=Surreal(set([a]),set([a]))    # ※
uarr=Surreal(set([a]),set([star])) # ↑
darr=Surreal(set([star]),set([a])) # ↓
print
print 'another Day:'
print u'* = {0|0}, \u0018={0|*} \u0019={*|0} use star, uarr, darr to name them'
print '*<=0', star<=a, '*>=0', star>=a
print u'\u0018<=0', uarr<=a, u'\u0018>=0', uarr>=a # ↑ \u0018
print u'\u0019<=0', darr<=a, u'\u0019>=0', darr>=a # ↓ \u0019
print '* + * <=0 ', (star+star)<=a, '* + * >= 0', (star+star)>=a

ua_star = uarr+star                   # ↑※
uaua_star = uarr+ua_star              # ↑↑※
uauaua_star=uarr+uaua_star            # ↑↑↑※
print
print u'\u0018*  <=0', ua_star<=a,     u'\u0018*  >=0', ua_star>=a
print u'\u0018\u0018* <=0', uaua_star<=a,   u'\u0018\u0018* >=0', uaua_star>=a
print u'\u0018\u0018\u0018*<=0', uauaua_star<=a, u' \u0018\u0018\u0018*>=0', uauaua_star>=a

da_star = darr+star                   # ↓※
dada_star = darr+da_star              # ↓↓※
dadada_star=darr+dada_star            # ↓↓↓※
print
print u'\u0019*  <=0', da_star<=a,     u'\u0019*  >=0', da_star>=a
print u'\u0019\u0019* <=0', dada_star<=a,   u'\u0019\u0019* >=0', dada_star>=a
print u'\u0019\u0019\u0019*<=0', dadada_star<=a, u'\u0019\u0019\u0019*>=0', dadada_star>=a

print u'\u0018 * <=0'
print u'\u0018'.encode('utf-8')
ch = u'\u0018'
print ch

