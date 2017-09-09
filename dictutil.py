# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[keylist[x]] for x in range(len(keylist))]

def list2dict(L, keylist): return {keylist[i]:L[i] for i in range(len(L))}

def listrange2dict(L): return {x:L[x] for x in range(len(L))}
