# On numbers and games
# J. H. CONWAY
# reprinted with corrections 1977
import re
import exceptions

# use dictionary map surreal to real numbers and vesa
dali2s={}
def dali(x):
    for s in dali2s:
        if s==x:
            return dali2s[s]
    return 'unknown'

def s(x):
    for s in dali2s:
        if dali2s[s]==x:
            return s
    return 'unknown'

def add_dali(x, value):
    for s in dali2s:
        if s==x:
            return False
    dali2s[x]=value
    return True

def list_dali():
    for s in dali2s:
        print dali2s[s], s
    return True


def shorthand(raw):
    """
    Converts the written shorthand for Surreals into
    a normal Surreal object
    ex. shorthand('{0|1}')
    """
    string = str(raw)

    # Check if input is integer
    # obselete
    if string.isdigit():
        return dali(int(string))

    # Check string for the {L|R} syntax
    m = re.match(r'^{(.*)\|(.*)}$', string)
    if m and len(m.groups()) == 2:
        leftSurreals = set()
        for symbol in m.group(1).split(","):
            if symbol != "":
                leftSurreals.add(shorthand(symbol))
        rightSurreals = set()
        for symbol in m.group(2).split(","):
            if symbol != "":
                rightSurreals.add(shorthand(symbol))
        return Surreal(leftSurreals, rightSurreals)

class BadlyFormed(exceptions.Exception):
    pass

class Surreal(object):
    """
    number
    """
    def __init__(self, leftSet, rightSet):
        '''
          If leftSet and rightSet are any two sets of numbers,
          and no member of leftSet>= any member of rightSet
          then there is a number {leftSet|rightSet}
          ONAG, Page 4
          ps. don't check is_well_formed or not, so it can also init pseudo number
        '''
        self._is_well_formed(leftSet, rightSet)
        self.leftSet = leftSet
        self.rightSet = rightSet

    def _is_well_formed(self, leftSet, rightSet):
        if len(leftSet) == 0 or len(rightSet) == 0 : return True

        for r in rightSet:
            for l in leftSet:
                if r <= l : 
                    self.pseudo = True
                    return False
        self.pseudo = False
        return True

    def __len__(self):
        return 1

    def __le__(self, other):
        # We say x>=y if and only if no member in x.rightSet<=y and no member in y.leftSet>=x
        # and x<=y if and only if y>=x
        # ONAG, Page 4

        if len(self.leftSet)!=0:
            for s in self.leftSet:
                if s >= other:
                    #print 'False: self.leftSet>=other', s, '>=', other
                    return False
                else:
                    continue
        if len(other.rightSet)!=0:
            for s in other.rightSet:
                if self >= s:
                    #print 'False: self>=other.rightSet', self, '>=', s
                    return False
                else:
                    continue
        return True

    def __ge__(self, other):
        # We say x>=y if and only if no member in x.rightSet<=y and no member in y.leftSet>=x
        # and x<=y if and only if y>=x
        # ONAG, Page 4

        if len(self.rightSet)!=0:
            for s in self.rightSet:
                if s <= other:
                    #print 'False: self.rightSet<=other', s, '<=', other
                    return False
                else:
                    continue
        if len(other.leftSet)!=0:
            for s in other.leftSet:
                if self <= s:
                    #print 'False: self<=other.leftSet', self, '<=', s
                    return False
                else:
                    continue
        return True

    def __eq__(self, other):
        '''
          Definition of x=y, x>y, x<y
          x=y iff (x>=y and y>=x)
          x>y iff (x>=y and y not>= x)
          x<y iff y>x
          ps. We write x not<= y to mean that x<=y does not hold
          ONAG, Page 4
        '''
        return self <= other and self >= other
    def __gt__(self, other):
        return self>=other and not(other>=self)
    def __lt__(self, other):
        return other>self

    def __repr__(self):
        if len(self.leftSet)==0 and len(self.rightSet)==0:
            return 'S{ | }'
        if len(self.leftSet)==0:
            return 'S{ | %s}' % self.rightSet
        if len(self.rightSet)==0:
            return 'S{ %s| }' % self.leftSet
        return 'S{ %s | %s }' % (self.leftSet, self.rightSet)

    def __add__(self, other):
        '''
          Definition of x+y
          x+y = { x.leftSet+y, x+y.leftSet| x.rightSet+y, x+y.rightSet}
        '''
        leftSet = set()
        rightSet = set()
        if len(self.leftSet)!=0 :
            for s in self.leftSet:
                tmp = s+other
                leftSet.add(tmp)
        if len(other.leftSet)!=0 :
            for s in other.leftSet:
                tmp = self+s
                leftSet.add(tmp)
        if len(self.rightSet)!=0 :
            for s in self.rightSet:
                tmp = s+other
                rightSet.add(tmp)
        if len(other.rightSet)!=0 :
            for s in other.rightSet:
                tmp = self+s
                rightSet.add(tmp)
        #return Surreal(leftSet, rightSet)
        return Surreal.simplify(Surreal(leftSet, rightSet))

    def __neg__(self):
        leftSet = set()
        rightSet = set()
        if len(self.leftSet)!=0 :
            for s in self.leftSet:
                rightSet.add(-s)
        if len(self.rightSet)!=0 :
            for s in self.rightSet:
                leftSet.add(-s)
        return Surreal.simplify(Surreal(leftSet, rightSet))

    def __sub__(self, other):
        return (self+(-other))

    def __mul__(self, other):
        leftSet = set()
        rightSet = set()
        if len(self.leftSet)!=0 :
            for xl in self.leftSet:
                if len(other.leftSet)!=0:
                    for yl in other.leftSet:
                        s = xl*other + self*yl - xl*yl
                        found=0
                        for l in leftSet:
                            if l == s: found=1
                        if found==0: leftSet.add(s)
                if len(other.rightSet)!=0:
                    for yr in other.rightSet:
                        s = xl*other + self*yr - xl*yr
                        found=0
                        for r in rightSet:
                            if r == s: found=1
                        if found==0: rightSet.add(s)
        if len(self.rightSet)!=0 :
            for xr in self.rightSet:
                if len(other.leftSet)!=0:
                    for yl in other.leftSet:
                        s = xr*other + self*yl - xr*yl
                        found=0
                        for r in rightSet:
                            if r == s: found=1
                        if found==0: rightSet.add(s)
                if len(other.rightSet)!=0:
                    for yr in other.rightSet:
                        s = xr*other + self*yr - xr*yr
                        found=0
                        for l in leftSet:
                            if l == s: found=1
                        if found==0: leftSet.add(s)
        return Surreal.simplify(Surreal(leftSet, rightSet))

    def mul_inverse(self, num=1):
        zero = Surreal(set(),set())
        one = Surreal(set([zero]),set())

        leftSet = set()
        leftSet.add(zero)
        rightSet = set()
        for i in range(0,num):
            for v in self.leftSet:
                for l in leftSet:
                    rightSet.add((one+(v-self)*l)*Surreal.mul_inverse(v))
            for u in self.rightSet:
                for r in rightSet:
                    rightSet.add((one+(u-self)*r)*Surreal.mul_inverse(u))

            for u in self.rightSet:
                for l in leftSet:
                    leftSet.add((one+(u-self)*l)*Surreal.mul_inverse(u))
            for v in self.leftSet:
                for r in rightSet:
                    leftSet.add((one+(v-self)*r)*Surreal.mul_inverse(v))
        return Surreal(leftSet, rightSet)

    def __div__(self, other):
        # failed!
        return

    def simplify(self):
        if hasattr(self,'pseudo')==True: return self
        leftSet = set()
        rightSet = set()
        if len(self.leftSet)!=0:
            i=0
            for s in self.leftSet:
                if i == 0:
                    max=s
                    i = 1
                    continue
                if max<=s:
                    #print 's>=max'
                    max = s
            leftSet.add(Surreal.simplify(max))
        if len(self.rightSet)!=0:
            i=0
            for s in self.rightSet:
                if i == 0:
                    min=s
                    i = 1
                    continue
                if s<=min:
                    #print 's<=min'
                    min = s
            min=Surreal.simplify(min)
            rightSet.add(min)
        return Surreal(leftSet, rightSet)

