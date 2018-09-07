#coding=utf-8
#windows-1252, ASCII, cp1252, GBK, ISO8859-1, ISO8859-15, JIS, UCS-2, UCS-4, UTF-8, UTF-16 and UTF-32.
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

print 'Now pseudo number is coming, it\'s prepared for Game'
# construre pseudo number, as {0|0}
star=Surreal(set([a]),set([a]))    # *

print u'* = {0|0}, \u0018={0|*} \u0019={*|0} use star, uarr, darr to name them'
#print '\u%04x \u%04x' % (ord('↑'), ord('↓')) # run in python console, result is: \u0018 \u0019, but failed in dos command
print 'verify: * + * == 0 ', (star+star)==a
print 'verify: * less than any positive and greater than any negative *<=e', star<=e, '*>=-e', star>=-e
print 'verify: * can\'t compare with zero *<=a', star<=a, '*>=a', star>=a
ss=Surreal(set([star]),set([star]))
print 'verify: {*|*} == *+* == 0', ss==star+star, ss==a
print

uarr=Surreal(set([a]),set([star])) # ↑ = {0|*} = {0| {0|0}}
darr=Surreal(set([star]),set([a])) # ↓
print u'verify: \u0018+\u0019==0', uarr+darr==a # ↑ \u0018 ↓ \u0019
print u'verify: \u0018>0>\u0019', uarr>a, a>darr
print u'\u0018 =?= 0+*', uarr==a+star
print

print u'define High order infinitesimal: \u0018* \u0018\u0018* \u0018\u0018\u0018*'
ua_star = uarr+star                   # ↑*
ua_star_alt = star+uarr               # *↑
print u'verfiy: \u0018* == *\u0018', ua_star==ua_star_alt, 'Commutative Property'
print u'verify: \u0018+* can\'t compare with zero \u0018*<=0 \u0018*>=0', ua_star<=a, ua_star>=a
print u'verify: *+\u0018 can\'t compare with zero *\u0018<=0 *\u0018>=0', ua_star_alt<=a, ua_star_alt>=a

print
u=Surreal(set([a]),set([uarr]))         # {0|↑} == {0| {0| {0|0}}} =?= ↑↑*
x1=uarr+ua_star                         # ↑↑*
x2=ua_star+uarr                         # ↑*↑
y1=uarr+ua_star_alt                     # ↑*↑
y2=ua_star_alt+uarr                     # *↑↑
print u'verify Commutative Property and Associative Property of Addition \u0018\u0018*==(\u0018*)\u0018==\u0018(*\u0018)==*\u0018\u0018', x1==x2, x2==y1, y1==y2
print u'verify: {0|\u0018}==\u0018\u0018* ==(\u0018*)\u0018 ==\u0018(*\u0018) ==\u0018*\u0018', x1==u,x2==u,y1==u,y2==u

# area of Figure2.8
#     ↑             = ↑
# u  {0|   ↑  }     = ↑↑*
# v  {0| {0|↑}}     = ↑↑↑
# w  {0| {0|{0|↑}}} = ↑↑↑*
v=Surreal(set([a]),set([u]))          # ↑↑↑   == {0| {0|↑}}
w=Surreal(set([a]),set([v]))          # ↑↑↑↑* == {0| {0| {0|↑}}}
print

print u'define \u0018\u0018 \u0018\u0018* \u0018\u0018\u0018 \u0018\u0018\u0018* \u0018\u0018\u0018\u0018 \u0018\u0018\u0018\u0018*',
import time
st=time.time()
uaua=uarr+uarr                        # ↑↑    == ?
uaua_star = uarr+ua_star              # ↑↑*   == {0|↑}
uauaua=uarr+uarr+uarr                 # ↑↑↑   == {0| {0|↑}}
uauaua_star=uarr+uaua_star            # ↑↑↑*  == ?
uauauaua=uarr+uarr+uarr+uarr          # ↑↑↑↑  == ?
uauauaua_star=uarr+uauaua_star        # ↑↑↑↑* == {0| {0| {0|↑}}}
et=time.time()
print 'cost %.2f seconds' % (et-st)

print u'{0| \u0018}          == \u0018\u0018*', u==uaua_star
print u'{0| {0|\u0018}}      =?= \u0018\u0018\u0018*', v==uauaua_star, 'strange!'
print u'{0| {0|\u0018}}      == \u0018\u0018\u0018', v==uauaua, 'interesting!'
print u'{0| {0| {0|\u0018}}} == \u0018\u0018\u0018\u0018*', w==uauauaua_star

print
print u'compare * \u0018 \u0018* \u0018\u0018 \u0018\u0018* \u0018\u0018\u0018 \u0018\u0018\u0018* \u0018\u0018\u0018\u0018 \u0018\u0018\u0018\u0018* with zero * \u0018 \u0018* \u0018\u0018 \u0018\u0018* \u0018\u0018\u0018 \u0018\u0018\u0018* \u0018\u0018\u0018\u0018'

print 'star<=0,    star>=0', star<=a, star>=a, 'can\'t compare with zero'
#print 'star<=star, star>=star', star<=star, star>=star
print

print 'uarr<=0,    uarr>=0', uarr<=a, uarr>=a
print 'uarr<=star, uarr>=star', uarr<=star, uarr>=star, 'can\'t compare with star'
#print 'uarr<=uarr, uarr>=uarr', uarr<=uarr, uarr>=uarr
print

print 'ua_star<=0,    ua_star>=0', ua_star<=a, ua_star>=a, 'can\'t compare with zero'
print 'ua_star<=star, ua_star>=star', ua_star<=star, ua_star>=star
print 'ua_star<=uarr, ua_star>=uarr', ua_star<=uarr, ua_star>=uarr, 'can\'t compare with uarr'
#print 'ua_star<=ua_star, ua_star>=ua_star', ua_star<=ua_star, ua_star>=ua_star
print

print 'uaua<=0,    uaua>=0', uaua<=a, uaua>=a
print 'uaua<=star, uaua>=star', uaua<=star, uaua>=star
print 'uaua<=uarr, uaua>=uarr', uaua<=uarr, uaua>=uarr
print 'uaua<=ua_star, uaua>=ua_star', uaua<=ua_star, uaua>=ua_star, 'can\'t compare with ua_star'
#print 'uaua<=uaua, uaua>=uaua', uaua<=uaua, uaua>=uaua
print

print 'uaua_star<=0,         uaua_star>=0', uaua_star<=a, uaua_star>=a
print 'uaua_star<=star,      uaua_star>=star', uaua_star<=star, uaua_star>=star
print 'uaua_star<=uarr,      uaua_star>=uarr', uaua_star<=uarr, uaua_star>=uarr, 'can\'t compare with uarr'
print 'uaua_star<=ua_star,   uaua_star>=ua_star', uaua_star<=ua_star, uaua_star>=ua_star
print 'uaua_star<=uaua,   uaua_star>=uaua', uaua_star<=uaua, uaua_star>=uaua
#print 'uaua_star<=uaua_star, uaua_star>=uaua_star', uaua_star<=uaua_star, uaua_star>=uaua_star
print

print 'uauaua<=0,         uauaua>=0', uauaua<=a, uauaua>=a
print 'uauaua<=star,      uauaua>=star', uauaua<=star, uauaua>=star
print 'uauaua<=uarr,      uauaua>=uarr', uauaua<=uarr, uauaua>=uarr
print 'uauaua<=ua_star,   uauaua>=ua_star', uauaua<=ua_star, uauaua>=ua_star
print 'uauaua<=uaua,   uauaua>=uaua', uauaua<=uaua, uauaua>=uaua
print 'uauaua<=uaua_star,   uauaua>=uaua_star', uauaua<=uaua_star, uauaua>=uaua_star
#print 'uauaua<=uauaua, uauaua>=uauaua', uauaua<=uauaua, uauaua>=uauaua
print

print 'uauaua_star<=0,         uauaua_star>=0', uauaua_star<=a, uauaua_star>=a
print 'uauaua_star<=star,      uauaua_star>=star', uauaua_star<=star, uauaua_star>=star
print 'uauaua_star<=uarr,      uauaua_star>=uarr', uauaua_star<=uarr, uauaua_star>=uarr
print 'uauaua_star<=ua_star,   uauaua_star>=ua_star', uauaua_star<=ua_star, uauaua_star>=ua_star
print 'uauaua_star<=uaua,   uauaua_star>=uaua', uauaua_star<=uaua, uauaua_star>=uaua, 'can\'t compare with uaua'
print 'uauaua_star<=uaua_star, uauaua_star>=uaua_star', uauaua_star<=uaua_star, uauaua_star>=uaua_star
print 'uauaua_star<=uauaua, uauaua_star>=uauaua', uauaua_star<=uauaua, uauaua_star>=uauaua, 'can\'t compare with uauaua'
#print 'uauaua_star<=uauaua_star, uauaua_star>=uauaua_star', uauaua_star<=uauaua_star, uauaua_star>=uauaua_star
print

print 'uauauaua<=0,         uauauaua>=0', uauauaua<=a, uauauaua>=a
print 'uauauaua<=star,      uauauaua>=star', uauauaua<=star, uauauaua>=star
print 'uauauaua<=uarr,      uauauaua>=uarr', uauauaua<=uarr, uauauaua>=uarr
print 'uauauaua<=ua_star,   uauauaua>=ua_star', uauauaua<=ua_star, uauauaua>=ua_star
print 'uauauaua<=uaua,   uauauaua>=uaua', uauauaua<=uaua, uauauaua>=uaua
print 'uauauaua<=uaua_star, uauauaua>=uaua_star', uauauaua<=uaua_star, uauauaua>=uaua_star
print 'uauauaua<=uauaua, uauauaua>=uauaua', uauauaua<=uauaua, uauauaua>=uauaua
print 'uauauaua<=uauaua_star, uauauaua>=uauaua_star', uauauaua<=uauaua_star, uauauaua>=uauaua_star
#print 'uauauaua<=uauauaua, uauauaua>=uauauaua', uauauaua<=uauauaua, uauauaua>=uauauaua
print

print 'uauauaua_star<=0,         uauauaua_star>=0', uauauaua_star<=a, uauauaua_star>=a
print 'uauauaua_star<=star,      uauauaua_star>=star', uauauaua_star<=star, uauauaua_star>=star
print 'uauauaua_star<=uarr,      uauauaua_star>=uarr', uauauaua_star<=uarr, uauauaua_star>=uarr
print 'uauauaua_star<=ua_star,   uauauaua_star>=ua_star', uauauaua_star<=ua_star, uauauaua_star>=ua_star
print 'uauauaua_star<=uaua,   uauauaua_star>=uaua', uauauaua_star<=uaua, uauauaua_star>=uaua
print 'uauauaua_star<=uaua_star, uauauaua_star>=uaua_star', uauauaua_star<=uaua_star, uauauaua_star>=uaua_star
print 'uauauaua_star<=uauaua, uauauaua_star>=uauaua', uauauaua_star<=uauaua, uauauaua_star>=uauaua
print 'uauauaua_star<=uauaua_star, uauauaua_star>=uauaua_star', uauauaua_star<=uauaua_star, uauauaua_star>=uauaua_star
print 'uauauaua_star<=uauauaua, uauauaua_star>=uauauaua', uauauaua_star<=uauauaua, uauauaua_star>=uauauaua
#print 'uauauaua_star<=uauauaua_star, uauauaua_star>=uauauaua_star', uauauaua_star<=uauauaua_star, uauauaua_star>=uauauaua_star
print

print 'summary'
print '* can\'t compare with zero'

print u'\u0018 can\'t compare with *'
print u'\u0018* can\'t compare with zero and \u0018'

print u'\u0018\u0018 can\'t compare with \u0018*'
print u'\u0018\u0018* can\'t compare with \u0018 and \u0018\u0018'

print u'\u0018\u0018\u0018 can\'t compare with \u0018\u0018*'
print u'\u0018\u0018\u0018* can\'t compare with \u0018\u0018 and \u0018\u0018\u0018'

print u'\u0018\u0018\u0018\u0018 can\'t compare with \u0018\u0018\u0018*'
print u'\u0018\u0018\u0018\u0018* can\'t compare with \u0018\u0018\u0018 and \u0018\u0018\u0018\u0018'

print
print u'\u0018  >=0'
print u'\u0018* >=*'
print u'\u0018\u0018 >=0 >=* >=\u0018'
print u'\u0018\u0018*>=0 >=* >=\u0018*'
print u'\u0018\u0018\u0018 >=0 >=* >=\u0018 >=\u0018* >=\u0018\u0018'
print u'\u0018\u0018\u0018*>=0 >=* >=\u0018 >=\u0018* >=\u0018\u0018*'

print u'\u0018\u0018\u0018\u0018>=0 >=* >=\u0018 >=\u0018* >=\u0018\u0018 >=\u0018\u0018* >=\u0018\u0018\u0018'
print u'\u0018\u0018\u0018\u0018*>=0 >=* >=\u0018 >=\u0018* >=\u0018\u0018 >=\u0018\u0018* >=\u0018\u0018\u0018*'
print

print u'define Low  order infinitesimal: \u0019* \u0019\u0019* \u0019\u0019\u0019*'
da_star = darr+star                   # ↓*
dada_star = darr+da_star              # ↓↓*
dadada_star=darr+dada_star            # ↓↓↓*
print 'ignore detail verify'
print

# explain Figure 2.8
# area    black     white
# *     =  *     =  *
# ↑     = -↓     =  ↑* + *
# ↑↑*   = -↓↓*   =  ↑* + ↑* + *
# ↑↑↑   = -↓↓↓   =  ↑* + ↑* + ↑* + *
# ↑↑↑↑* = -↓↓↓↓* =  ↑* + ↑* + ↑* + ↑* + *
print u'verify: \u0019+\u0018*==*', darr+ua_star==star
print u'verify: \u0018==\u0018*+*', uarr==(ua_star+star)
print u'verify: \u0018\u0018*==\u0018*+\u0018*+*', uaua_star==(ua_star+ua_star+star)
print u'verfiy: \u0018\u0018* == \u0018*+\u0018', uaua_star==(ua_star+uarr)
print u'verfiy: \u0018\u0018\u0018 == \u0018*+\u0018\u0018*', uauaua==(ua_star+uaua_star)
#print u'verify: \u0018\u0018\u0018==\u0018*+\u0018*+\u0018*+*', uauaua==(ua_star+ua_star+ua_star+star)
#print u'verify: \u0018\u0018\u0018*==\u0018*+\u0018*+\u0018*+\u0018*+*', uauaua_star==(ua_star+ua_star+ua_star+ua_star+star)
print

print 'cooling'
# Thermograph={ 2| {1|0} }
# mast value=0.25
# Game=Thermograph after cooling
# cooling
# Game={RL|RR},leftSet is Game's Result of black to move, Result=ScoreB-ScoreW
#cooling step1: {RL-1|RR-1},左边和右边均减1，递归，直到把第一个左集减为1
#cooling step2: {RL-1|RR+1},左边减1，右边加1，递归，即黑走一步减1，白走一步加1

#ex 3 point corridor { 2| {1|0} }
#cooling step1: { 1| {0|-1} }
#cooling step2: { 1-1| {0+1-1|-1+1+1} } = { 0| {0|1} }

# 3 point corridor with 1 stone: { 3| {2|0} }
#after cooling step1, { 1| {0|-2} }
#after cooling step2, { 0| {0|0}  }, because{0|*}=↑=t0

'''
a=↓ b=1/2 c=* d=-1/4 d=↓ f=-1/4 g=↑↑* h=*
sum, 1/2+(-1/4)+(-1/4)+↓+↓+↑↑*+*+* = *
1/2 >= ↑↑* >= *,↓ >= -1/4
'''
c>=uaua_star, c>=star, c>=darr, c>=-e
uaua_star>=star, uaua_star>=darr, uaua_star>=-e
star>=-e
darr>=-e
#so, x = c+(-e)+(-e)+darr+darr+uaua_star+star+star
#simplify to:
#x = darr+darr+uaua_star     # ↓↓↑↑*, may take 5 minutes to calculate
#print u'verfiy: \u0019\u0019\u0018\u0018*==*', x==star

print 'now begin tiny and miny'
print u't0: { 0|{0|0} }  , 3 point corridor with one stone, {0|*} \u0018'
print 't1: { 0|{0|-1} } , 4 point corridor with one stone, one empty'
print 't2: { 0|{0|-2} }'
print 't3: { 0|{0|-3} }'
print 't4: { 0|{0|-4} }'

t0=uarr
t1=Surreal(set([a]), set([Surreal(set([a]),set([-r]))]))
t2=Surreal(set([a]), set([Surreal(set([a]),set([-d]))]))
t3=Surreal(set([a]), set([Surreal(set([a]),set([-h]))]))
t4=Surreal(set([a]), set([Surreal(set([a]),set([-i]))]))
print 'verify: t0>=t1>=t2>=t3>=t4>=0', t0>=t1, t1>=t2, t2>=t3, t3>=t4, t4>=a

x=uarr+t2
y=uarr-t2
print u'verify: \u0018+t2>=\u0018-t2 \u0018+t2>=0 \u0018-t2>=0', x>=y, x>=a, y>=a

print
print 'low order tiny and miny'
print 'means one more step can reach tiny or miny'
print u't0_0  { 0|{0|0}}  == t0 == uarr'
print u't0_1: { 0| 0| {0|0}}'
print u't0_2: { 0| 0| 0| {0|0}}'
print u't0_3: { 0| 0| 0| 0| {0|0}}'
t0_0=t0
t0_1=Surreal(set([a]), set([t0_0]))
t0_2=Surreal(set([a]), set([t0_1]))
t0_3=Surreal(set([a]), set([t0_2]))
t1_0=t1
t1_1=Surreal(set([a]), set([t1_0]))
t1_2=Surreal(set([a]), set([t1_1]))
t1_3=Surreal(set([a]), set([t1_2]))
t2_0=t2
t2_1=Surreal(set([a]), set([t2_0]))
t2_2=Surreal(set([a]), set([t2_1]))
t2_3=Surreal(set([a]), set([t2_2]))
print u't0_0==uarr t0_1==uaua_star, t0_2==uauaua, t0_3==uauauaua_star t0 is same as \u0018 \u0018\u0018* \u0018\u0018\u0018 \u0018\u0018\u0018\u0018*'

'''print u'走三步才能到达微量x，此类棋形比微量x要大，也比走一步到达微量x大，但相邻阶次无法比较 此类棋形比箭头↑要小（高阶无穷小）'
'''
print 'all t2, can\t compare with neighbour >=low order, ex t2_3>=t2_1, t2_3>=t2_0 can\'t compare with t2_2'
t2_3>=t2_1, t2_3>=t2_0, t2_3>=t2_2, t2_3<=t2_2

t2_3>=t0_0, t2_3>=t0_1, t2_3>=t0_2, t2_3<=t0_2, t2_3<=t0_3
t2_3>=t1_0, t2_3>=t1_1, t2_3>=t1_2, t2_3<=t1_2, t2_3<=t1_3

t1_0>=t0_0, t1_0>=t0_1, t1_0>=t0_2, t1_0>=t0_3
t1_1>=t0_0, t1_1>=t0_1, t1_1>=t0_2, t1_1>=t0_3
t1_2>=t0_0, t1_2>=t0_1, t1_2>=t0_2, t1_2>=t0_3
t1_3>=t0_0, t1_3>=t0_1, t1_3>=t0_2, t1_3>=t0_3

t2_0>=t0_0, t2_0>=t0_1, t2_0>=t0_2, t2_0>=t0_3
t2_1>=t0_0, t2_1>=t0_1, t2_1>=t0_2, t2_1>=t0_3
t2_2>=t0_0, t2_2>=t0_1, t2_2>=t0_2, t2_2>=t0_3
t2_3>=t0_0, t2_3>=t0_1, t2_3>=t0_2, t2_3>=t0_3

t2_0>=t1_0, t2_0>=t1_1, t2_0>=t1_2, t2_0>=t1_3
t2_1>=t1_0, t2_1>=t1_1, t2_1>=t1_2, t2_1>=t1_3
t2_2>=t1_0, t2_2>=t1_1, t2_2>=t1_2, t2_2>=t1_3
t2_3>=t1_0, t2_3>=t1_1, t2_3>=t1_2, t2_3>=t1_3

print u'verify: uarr>=t0_1>=t0_2>=t0_3>=t1', uarr>=t0_1, t0_1>=t0_2, t0_2>=t0_3, t0_3>=t1
print u'verify: uarr>=t1_1>=t1_2>=t1_3>=t1', uarr>=t0_1, t1_1>=t1_2, t1_2>=t1_3, t1_3>=t1
