# Travis Dean - tjd2qj
# CS 3240 Homework 1
from item import Item
from collections import Counter
__author__ = 'Travis Dean'
debug = False


def prompt():
    k = int(raw_input("Enter the value of k: "))
    m = int(raw_input("Enter the number of values to be read: "))
    filename = raw_input("Data file name: ")
    # print("When entering value pairs, separate by spaces without commas.")
    return k, m, filename


def get_input(k, m, filename):
    data = read_data(filename)[:m]
    while True:
        x, y = raw_input("Enter a (X,Y) pair: ").split()
        if x == '1.0' and y == '1.0':
            print("Exiting program")
            return
        process_input(data, k, float(x), float(y))


def read_data(filename):
    # lines = open(filename).readlines()
    with open(filename) as f:
        lines = f.readlines()
    data = []
    for d in lines:
        c, x, y = d.split()
        data.append(Item(x, y, c))
    return data


def process_input(data, k, x, y):
    count = Counter()
    totals = Counter()
    d = Item(x, y)
    nearest = sorted(data, key=lambda i: i.distance(d))[:k]
    for n in nearest:
        totals[n.category] += n.distance(d)
        count[n.category] += 1
        print(str(n) + " " + str(n.distance(d)))

    winner = count.most_common(1)
    win_cat = winner[0][0]
    print("Data item (%s,%s) assigned to: %s" % (x, y, win_cat))

    for cat, total in totals.items():
        print("Average distance to %s items: %f" %
              (cat, total / count[cat]))


if __name__ == "__main__":
    if not debug:
        try:
            get_input(*prompt())
        except Exception as e:
            print('Invalid input: ' + str(e))
    else:
        get_input(3, 8, "testdata.txt")


