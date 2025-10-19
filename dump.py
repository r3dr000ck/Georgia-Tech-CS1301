def f(d):
    ret = {}
    for i in d:
        for j in d[i]:
            if j[0] in ret:
                ret[j[0]] += j[1]
            else:
                ret[j[0]] = j[1]
    return ret

movieVotes = {"Josh": [("Coco", 8), ("Knives Out", 9)],"Paige": [("Halloweentown", 5), ("Coco", 8)],"Arushi": [("Mystic Pizza", 7), ("Knives Out", 9),("Coco", 8)]}
print(f(movieVotes))