def no_overlap(l):
    lap = sorted(l, key = lambda x:x[1])
    final = []
    for i in lap:
        num = -1
        start = i[1]
        min_fin = 90
        if final == []:
            end_check = -1
        else:
            end_check = final[-1][2]
        if i[1] >= end_check:
            for j in lap:
                if j[1] == start:
                    if j[2] < min_fin:
                        min_fin = j[2]
                        num = j[0]
        for k in lap:
            if num == k[0] and k not in final:
                final.append(k)
    total_final = []
    for i in final:
        total_final.append(i[0])
    print(final)
    print(total_final)
no_overlap([(0,1,2),(1,1,3),(2,1,5),(3,3,4),(4,4,5),(5,5,8),(6,7,9),(7,10,13),(8,11,12)])