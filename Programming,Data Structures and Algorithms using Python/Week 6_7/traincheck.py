def minimum_platform(train):
    new_train = []
    for i in train:
        row = []
        row.append(i[0])
        row.append(i[1])
        row.append(i[2])
        row[1] = int(row[1].replace(':',''))
        row[2] = int(row[2].replace(':',''))
        new_train.append(row)
    new_train = sorted(new_train, key = lambda x:x[2])
    num = 0
    for i in new_train:
        
    print(new_train)
minimum_platform([(1,'09:00','09:30'),(2,'09:00','09:20')])
    