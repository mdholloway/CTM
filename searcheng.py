def makeInverseIndex(strlist):
  result = {}
  for (i,j) in enumerate(strlist):
    words = j.split(' ')
    for word in words:
      if word not in result:
        result[word] = set() 
      result[word].add(i+1)
  return result

def orSearch(inverseIndex, query):
  return set.union(*[inverseIndex[word] for word in query])

def andSearch(inverseIndex, query):
  return set.intersection(*[inverseIndex[word] for word in query])
