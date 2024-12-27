# -*- coding: utf-8 -*-
from surreal import *

a=Surreal(set(),set())           # {|}       0
b=Surreal(set(),set([a]))        # {|0}      -1
r=Surreal(set([a]),set())        # {0|}      1
c=Surreal(set([a]), set([r]))    # {0|1}     1/2
d=Surreal(set([r]), set())       # {1|}      2
e=Surreal(set([a]), set([c]))    # {0|1/2}   1/4
f=Surreal(set([c]), set([r]))    # {1/2 |1}  3/4
g=Surreal(set([r]), set([d]))    # {1|2}     3/2
h=Surreal(set([d]), set())       # {2|}      3
i=Surreal(set([h]), set())       # {3|}      4
j=Surreal(set([i]), set())       # {4|}      5
k=Surreal(set([j]), set())       # {5|}      6
l=Surreal(set([k]), set())       # {6|}      7
m=Surreal(set([l]), set())       # {7|}      8

add_dali(a,0)
add_dali(b,-1)
add_dali(r,1)
add_dali(c, 0.5)
add_dali(-c, -0.5)
add_dali(d, 2)
add_dali(-d, -2)
add_dali(e, 0.25)
add_dali(-e, -0.25)
add_dali(f, 0.75)
add_dali(-f, -0.75)
add_dali(g, 1.5)
add_dali(-g, -1.5)
add_dali(h, 3)
add_dali(-h, -3)
add_dali(i, 4)
add_dali(-i, -4)
add_dali(j, 5)
add_dali(-j, -5)
add_dali(k, 6)
add_dali(-k, -6)
add_dali(l, 7)
add_dali(-l, -7)
add_dali(m, 8)
add_dali(-m, -8)

star=Surreal(set([a]),set([a]))    # *
uarr=Surreal(set([a]),set([star])) # ↑
darr=Surreal(set([star]),set([a])) # ↓

ua_star = uarr+star                   # ↑*
uaua=uarr+uarr                        # ↑↑    == ?
uaua_star = uarr+ua_star              # ↑↑*   == {0|↑}
uauaua=uarr+uarr+uarr                 # ↑↑↑   == {0| {0|↑}}
uauaua_star=uarr+uaua_star            # ↑↑↑*  == ?
#uauauaua=uarr+uarr+uarr+uarr          # ↑↑↑↑  == ?
#uauauaua_star=uarr+uauaua_star        # ↑↑↑↑* == {0| {0| {0|↑}}}

u=Surreal(set([a]),set([uarr]))
v=Surreal(set([darr]),set([a]))

da_star = darr+star                   # ↓*
dada=darr+darr                        # ↓↓    == ?
dada_star = darr+da_star              # ↓↓*   == {↓|0}
dadada=darr+darr+darr                 # ↓↓↓   == {{0|↓}|0}
dadada_star=darr+dada_star            # ↓↓↓*  == ?

X=Surreal(set([a]),set([-r]))
Y=Surreal(set([a]),set([-d]))
Z=Surreal(set([r]),set([a]))

A=Surreal(set([Y]),set([-d]))
B=Z
C=Y
D=Surreal(set([X]),set([-d]))
E=Surreal(set([Y]),set([-h]))
F=D
G=Surreal(set([D]),set([-i]))
H=C

