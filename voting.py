import sys

def list_dot(u, v): return sum([a*b for (a,b) in zip(u,v)])
def addn(v, w): return [x+y for (x,y) in zip(v,w)]
def divn(list, n): return [x/n for x in list]


# 2.12.1
def create_voting_dict(strlist):
    result = {}
    for row in strlist:
        data = row.split(" ")
        result[data[0]] = [ int(x) for x in data[3:] ]
    return result

# 2.12.2
def policy_compare(sen_a, sen_b, voting_dict): return list_dot(voting_dict[sen_a], voting_dict[sen_b])

# 2.12.3
def most_similar(sen, voting_dict):
    max = -sys.maxsize
    max_name = None
    for name in voting_dict:
        if sen != name:
            similarity = policy_compare(sen, name, voting_dict)
            if similarity > max:
                max = similarity
                max_name = name
    return max_name 

# 2.12.4
def least_similar(sen, voting_dict):
    min = sys.maxsize
    min_name = None
    for name in voting_dict:
        if sen != name:
            similarity = policy_compare(sen, name, voting_dict)
            if similarity < min:
                min = similarity
                min_name = name
    return min_name 
    
# 2.12.5:
# >>> voting.most_similar("Chafee", votes)
# 'Jeffords'
# >>> voting.least_similar("Santorum", votes)
# 'Feingold'

# 2.12.7
def find_average_similarity(sen, sen_set, voting_dict):
    total = 0
    count = 0
    for name in sen_set:
        if sen != name:
            total += policy_compare(sen, name, voting_dict)
            count += 1
    if count == 0:
        return 0
    else:
        return total / count

# 2.12.8
def find_average_record(sen_set, voting_dict):
    total = [0] * len(next(iter(voting_dict.values())))
    count = 0
    for name in sen_set:
        total = addn(total, voting_dict[name])
        count += 1
    if count == 0:
        return 0
    else:
        return divn(total, count)

# 2.12.9
def bitter_rivals(voting_dict):
    sen_set = voting_dict.keys()
    done = set()
    min = sys.maxsize
    rivals = ()
    for sen_a in sen_set:
        done.add(sen_a)
        for sen_b in sen_set:
            if sen_b not in done:
                similarity = policy_compare(sen_a, sen_b, voting_dict)
                if similarity < min:
                    min = similarity
                    rivals = (sen_a, sen_b)
    return rivals
