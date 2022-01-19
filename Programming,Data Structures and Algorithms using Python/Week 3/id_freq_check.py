'''A restaurant always prepares dishes with the most orders before others with a lesser number of orders.
Each dish in the restaurant menu has a unique integer ID.
The restaurant receives n orders in a particular time period.
The task is to find out the order of dish IDs according to which the restaurant will prepare them.
Assume that restaurant has the following unique dish IDs in its menu:
[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
Write a function DishPrepareOrder(order_list) that accepts order_list in the form of a list of dish IDs
and returns a list of dish IDs in the order in which the restaurant will prepare them.
If two or more dishes have the same number of orders,
then the dish which has a smaller ID value will be prepared first.'''

def DishPrepareOrder(l):
    d = dict()
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    sort_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    id = []
    for i in sort_dict.keys():
        id.append(i)
    for i in range(len(id)-1):
        if sort_dict[id[i]] == sort_dict[id[i+1]] and id[i] < id[i+1]:
            (id[i+1],id[i]) = (id[i],id[i+1])
    return id[::-1]
print(DishPrepareOrder([1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]))    
        