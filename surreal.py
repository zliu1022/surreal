import re
import exceptions

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
    Surreal number
    """
    def __init__(self, leftSet, rightSet):
        # If leftSet and rightSet are any two sets of numbers,
        # and no member of leftSet>= any member of rightSet
        # then there is a number {leftSet|rightSet}
        # ps. don't check is_well_formed or not, so it can also init pseudo number
        self._is_well_formed(leftSet, rightSet)
        self.leftSet = leftSet
        self.rightSet = rightSet

    def _is_well_formed(self, leftSet, rightSet):
        if len(leftSet) == 0 or len(rightSet) == 0 : return True

        for r in rightSet:
            for l in leftSet:
                if r <= l : 
                    #print "pseudo: L %s >= R %s, broke Atom1" % (leftSet, rightSet)
                    return False
        return True

    def __len__(self):
        return 1

    def __le__(self, other):
        #We say x>=y if and only if no member in x.rightSet<=y and no member in y.leftSet>=x
        #print '+++'
        if len(self.leftSet)==0 and len(other.rightSet)==0: 
            #print 'True: leftSet and rightSet are empty'
            #print '---'
            return True

        if len(self.leftSet)!=0:
            for s in self.leftSet:
                if other <= s:
                    #print 'False: other<=self.leftSet', other, '<=', s
                    #print '---'
                    return False
                else:
                    #print 'True: other not <=self.leftSet', other, 'not<=', s
                    pass
        if len(other.rightSet)!=0:
            for s in other.rightSet:
                if s <= self:
                    #print 'False: other.rightSet<=self', s, '<=', self
                    #print '---'
                    return False
                else:
                    #print 'True: other.rightSet not <=self', s, 'not<=', self
                    pass
        #print 'True: no self.leftSet>=other and no other.rightSet<=self'
        #print '---'
        return True

    def __eq__(self, other):
        return self <= other and other <= self

    def __repr__(self):
        if len(self.leftSet)==0 and len(self.rightSet)==0:
            return 'S{ | }'
        if len(self.leftSet)==0:
            return 'S{ | %s}' % self.rightSet
        if len(self.rightSet)==0:
            return 'S{ %s| }' % self.leftSet
        return 'S{ %s | %s }' % (self.leftSet, self.rightSet)
        if hasattr(self.leftSet,'dali') and hasattr(self.rightSet,'dali'):
            if self.leftSet.dali == 'unknown' and self.rightSet.dali == 'unknown':
                return 'S{ %s | %s }' % (self.leftSet, self.rightSet)
            if self.leftSet.dali == 'unknown' and self.rightSet.dali != 'unknown':
                return 'S{ %s | %d }' % (self.leftSet, self.rightSet.dali)
            if self.leftSet.dali != 'unknown' and self.rightSet.dali == 'unknown':
                return 'S{ %d | %s }' % (self.leftSet.dali, self.rightSet)
            return 'S{ %d| %d }' % (self.leftSet.dali, self.rightSet.dali)

        if hasattr(self.leftSet,'dali') and hasattr(self.rightSet,'dali')==False:
            if self.leftSet.dali == 'unknown' :
                return 'S{ %s| }' % (self.leftSet)
            return 'S{ %d| }' % (self.leftSet.dali)

        if hasattr(self.leftSet,'dali')==False and hasattr(self.rightSet,'dali'):
            if self.rightSet.dali == 'unknown' :
                return 'S{ |%s }' % (self.rightSet)
            return 'S{ |%d }' % (self.rightSet.dali)

        if hasattr(self.leftSet,'dali')==False and hasattr(self.rightSet,'dali')==False:
            return 'S{ | }'

    def __add__(self, other):
        leftSet = set()
        rightSet = set()
        if len(self.leftSet)!=0 :
            for s in self.leftSet:
                tmp = s+other
                if len(leftSet)!=0 :
                    found=0
                    for l in leftSet:
                        if l == tmp: found=1
                    if found==0: leftSet.add(tmp)
                else:
                    leftSet.add(tmp)
        if len(other.leftSet)!=0 :
            for s in other.leftSet:
                tmp = self+s
                if len(leftSet)!=0 :
                    found=0
                    for l in leftSet:
                        if l == tmp: found=1
                    if found==0: leftSet.add(tmp)
                else:
                    leftSet.add(tmp)
        if len(self.rightSet)!=0 :
            for s in self.rightSet:
                tmp = s+other
                if len(rightSet)!=0 :
                    found=0
                    for r in rightSet:
                        if r == tmp: found=1
                    if found==0: rightSet.add(tmp)
                else:
                    rightSet.add(tmp)
        if len(other.rightSet)!=0 :
            for s in other.rightSet:
                tmp = self+s
                if len(rightSet)!=0 :
                    found=0
                    for r in rightSet:
                        if r == tmp: found=1
                    if found==0: rightSet.add(tmp)
                else:
                    rightSet.add(tmp)
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

    def __truediv__(self, other):
        return 

    def simplify(self):
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
            max=Surreal.simplify(max)
            leftSet.add(max)
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

