import random as r

class Player:
    def __init__(self,tile=None):
        self.actions = ['u','d','l','r']
        self.currtile = tile
        self.alpha = 0.1
        self.discount = 0.3
        self.epsilon = 0.1
        self.Q = {}
        self.states = []
        for i in range(4):
            for j in range(4):
                self.states.append((i,j))
        for state in self.states:
            temp = {}
            for action in self.actions:
                temp[action] = 0
            self.Q[state] = temp
        print (self.Q)
                
                
    def swap_tile(self,t):
        self.currtile.id = 'E'
        self.currtile = t
        self.currtile.id = 'P'
    
    def getAction(self,s):
        if r.random() < self.epsilon:
            return r.choice(['u','d','r','l'])
        else:
            return self.max_Q(getStateTupFromNo(s))[0]
    
    def max_Q(self,s):
        val = None
        act = None
        for a, q in self.Q[s].items():
            if val is None or (q > val):
                val = q
                act = a
        return act, val
    
    def inc_Q(self,s, a,inc):
        self.Q[s][a] *= 1 - self.alpha
        self.Q[s][a] += self.alpha * inc
            
    def learn(self,s,s_,r,ac):
        max_act, max_val = self.max_Q(getStateTupFromNo(s_))
        self.inc_Q(getStateTupFromNo(s), ac, r + self.discount * max_val)


def getStateTupFromNo(n):
    if n==0: return (0,0)
    if n==1: return (0,1)
    if n==2: return (0,2)
    if n==3: return (0,3)
    if n==4: return (1,0)
    if n==5: return (1,1)
    if n==6: return (1,2)
    if n==7: return (1,3)
    if n==8: return (2,0)
    if n==9: return (2,1)
    if n==10: return (2,2)
    if n==11: return (2,3)
    if n==12: return (3,0)
    if n==13: return (3,1)
    if n==14: return (3,2)
    if n==15: return (3,3)
    
