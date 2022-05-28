import itertools
import pandas as pd



def read_datasets():
    data_records = pd.read_csv(r'CoffeeShopTransactions.csv')
    return data_records

def put_in_list():
    list1 = read_datasets()
    records = []
    for i in range(0, len(list1)):
        records.append([str((list1.values[i, j])) for j in range(3, 6)])
    return records

def remove_duplicates():
    list2 = put_in_list()
    for i in range(len(list2)):
        array = []
        for j in range(len(list2[i])):
            if (array.__contains__(list2[i][j])):
                continue
            else:
                array.append(list2[i][j])
        list2[i] = array
    return list2


list3 = remove_duplicates()
items = sorted([item for sublist in list3 for item in sublist])

def frequentSet_1(items, minimum_support_count):
    c1 = {i: items.count(i) for i in items}
    l1 = {}
    for key, value in c1.items():
        if value >= minimum_support_count:
            l1[key] = value

    return c1, l1

def frequentSet_2(l1, records, minimum_support_count):
    l1 = sorted(list(l1.keys()))
    L1 = list(itertools.combinations(l1, 2))
    c2 = {}
    l2 = {}
    for iter1 in L1:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count += 1
        c2[iter1] = count
    for key, value in c2.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l1, 1):
                l2[key] = value
    return c2, l2

def frequentSet_3(l2, records, minimum_support_count):
    l2 = list(l2.keys())
    L2 = sorted(list(set([item for t in l2 for item in t])))
    L2 = list(itertools.combinations(L2, 3))
    c3 = {}
    l3 = {}
    for iter1 in L2:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count += 1
        c3[iter1] = count
    for key, value in c3.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l2, 2):
                l3[key] = value

    return c3, l3


def frequentSet_4(l3, records, minimum_support_count):
    l3 = list(l3.keys())
    L3 = sorted(list(set([item for t in l3 for item in t])))
    L3 = list(itertools.combinations(L3, 4))
    c4 = {}
    l4 = {}
    for iter1 in L3:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count += 1
        c4[iter1] = count
    for key, value in c4.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l3, 3):
                l4[key] = value

    return c4, l4


def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)


def check_subset_frequency(itemset, l, n):
    if n > 1:
        subsets = list(itertools.combinations(itemset, n))
    else:
        subsets = itemset
    for iter1 in subsets:
        if not iter1 in l:
            return False
    return True



count = 100
minimum_confidence = 12
c1, l1 = frequentSet_1(items,count)
c2, l2 = frequentSet_2(l1, put_in_list(), count)
c3, l3 = frequentSet_3(l2, put_in_list(), count)
c4, l4 = frequentSet_4(l3, put_in_list(),count)
print("L1 => ", l1)
print("L2 => ", l2)
print("L3 => ", l3)
print("L4 => ", l4)
itemlist = {**l1, **l2, **l3, **l4}

def support_count(itemset, itemlist):
    return itemlist[itemset]

sets = []
for iter1 in list(l3.keys()):
    subsets = list(itertools.combinations(iter1, 2))
    sets.append(subsets)

list_l3 = list(l3.keys())
for i in range(0, len(list_l3)):
    for iter1 in sets[i]:
        a = iter1
        b = set(list_l3[i]) - set(iter1)
        confidence = (support_count(list_l3[i], itemlist)/support_count(iter1, itemlist))*100
        if (confidence >= minimum_confidence):
            print("Confidence{}->{} = ".format(a, b), confidence)

























