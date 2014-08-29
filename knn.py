# Travis Dean - tjd2qj
# CS 3240 Homework 1
from item import Item
from collections import Counter
__author__ = 'Travis Dean'

def prompt():
    k = input("Enter the value of k: ")
    m = input("Enter the number of values to be read: ")
    file = raw_input("Data file name: ")
    print("When entering value pairs, separate by spaces without commas.")
    return (k,m,file)

def get_input(k = 3,m = 8, file = "testdata.txt"):
    data = read_data(file)[:m]
    done = False
    while not done:
        done = process_input(data, k)

def read_data(filename = "testdata.txt"):
    lines = open(filename).readlines()
    data = []
    for d in lines:
        c,x,y = d.split()
        data.append(Item(x,y,c))
    return data

def process_input(data, k):
    x,y = raw_input("Enter (X,Y) pairs: ").split()
    if (x == '1.0' and y == '1.0'): return True

    count = Counter()
    d = Item(x,y,"Input")
    nearest = sorted(data, key=lambda i: i.distance(d))[:k]
    for n in nearest:
        print(str(n) + " " + str(n.distance(d)))
        count[n.category] += 1

    winner = count.most_common(1)
    win_cat = winner[0][0]
    print("Data item (%s,%s) assigned to: %s" % (x,y,win_cat))
    return False





if __name__ == "__main__":
    import sys
    #prompt()
    get_input()


