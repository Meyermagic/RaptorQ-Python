from __future__ import with_statement
import csv
import bisect


#Section 5.6, Table 2
# K' ->  (J(K'), S(K'), H(K'), W(K'))
def load_56t2():
    table_data = dict()
    with open('table_5_6_t2.txt', 'rb') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            table_data[int(row[0])] = (int(row[1]), int(row[2]), int(row[3]), int(row[4]))
    return table_data

table_2 = load_56t2()
sorted_keys = sorted(table_2.keys())

def t2_le(k):
    i = bisect.bisect_right(sorted_keys, k)
    return sorted_keys[i-1]

def J(K_):
    return table_2[K_][0]

def S(K_):
    return table_2[K_][1]

def H(K_):
    return table_2[K_][2]

def W(K_):
    return table_2[K_][3]
