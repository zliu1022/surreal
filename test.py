#coding=utf-8
#windows-1252, ASCII, cp1252, GBK, ISO8859-1, ISO8859-15, JIS, UCS-2, UCS-4, UTF-8, UTF-16 and UTF-32.
from surreal import *

print 'Day 0:'
a=Surreal(set(),set()) # shorthand(0) shorthand('{|}')
add_dali(a,0)
print 'a = ', a
print 'verify: a<=a and a>=a', a<=a, a>=a
print

print 'Day 1:'
b=Surreal(set(),set([a]))
r=Surreal(set([a]),set())
add_dali(b,-1)
add_dali(r,1)
print 'b = ', b
print 'r = ', r
print 'verify: b<=a, b<=r, a<=r', b<=a, b<=r, a<=r
print

print 'define operands'
print '+ : x+y = { x.leftSet+y, x+y.leftSet| x.rightSet+y, x+y.rightSet}'
x = a+a
print 'x = a+a =', x, ', x == a', x==a
x = a+r
print 'x = a+r =', x, ', a+r == r', x==r, 'Additive Identity'
x = a+b
print 'x = a+b =', x, ', a+b == b', x==b
x = r+b
print 'x = r+b =', x, ', r+b==a', x==a, 'Additive Inverse'
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
print 'a*r =', a*r, '==a', a==(a*r), 'Multiplicative Property of Zero'
print 'r*r =', r*r, '==r', r==(r*r)
print 'b*b =', b*b, '==r', r==b*b
print 'b*r =', b*r, '==b', b==b*r, 'Multiplicative Identity'
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

x=c*d
y=c+c
print 'verfiy: 2*(1/2): x = {1| }*{0|1}, x==r', x==r, 'Multiplicative Inverse'
print 'verify: 1/2+1/2: y = {0|1}+{0|1}, x==y, y==r', x==y, y==r
print

print 'Day 3:'
leftSet = set([a])
rightSet = set([c])
e=Surreal(leftSet, rightSet)
add_dali(e, 0.25)
add_dali(-e, -0.25)

leftSet = set([c])
rightSet = set([r])
f=Surreal(leftSet, rightSet)
add_dali(f, 0.75)
add_dali(-f, -0.75)

leftSet = set([r])
rightSet = set([d])
g=Surreal(leftSet, rightSet)
add_dali(g, 1.5)
add_dali(-g, -1.5)

leftSet = set([d])
rightSet = set()
h=Surreal(leftSet, rightSet)
add_dali(h, 3)
add_dali(-h, -3)
print 'e = {0|1/2} = 1/4', e
print 'f = {1/2|1} = 3/4', f
print 'g = { 1|2 } = 3/2', g
print 'h = { 2|  } = 3', h
print 'You can verify here, as 1/4+1/4==1/2, {1/2|2}==1', e+e==c, Surreal(set([c]),set([d]))==r
x=Surreal(set([c]),set([r+c]))
print 'verify: x = { 1/2, 1+1/2 }=', x==r, 'dali(x)=', dali(x)

print
print 'Surreal numbers summary:'
print 'day0:                     0,a'
print 'day1:         -1,b                       1,r'
print 'day2:    -2,       -1/2,        1/2,c          2,d'
print 'day3: -3, -3/2, -3/4, -1/4, 1/4,e  3/4,f   3/2,g  3,h'
print 'dali(c+r)', dali(c+r)
print 'dali(c+g)', dali(c+g)
print 'dali(e+f)', dali(e+f)
print 'dali(e+c)', dali(e+c)
print 'dali(e+e+e)', dali(e+e+e)
print 'Can use s function to find surreal number from real number: s(0.5)', s(0.5), 's(0.5)==c', s(0.5)==c
print

print 'simplify therom'
print 'verifying {-0.25|1} {-0.5|1} {-0.75|1} {-1|1}', \
    dali(Surreal(set([-e]),set([r]))), dali(Surreal(set([-c]),set([r]))), \
    dali(Surreal(set([-f]),set([r]))), dali(Surreal(set([b]),set([r])))
print

# You can try more verification here, it will take long time to calculate
#{1 |1 1/2} * {1/2 |1/2}
#Surreal(set([e]),set([e+r]))*(e+e)

