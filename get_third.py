import sys

file = sys.argv[1]
second_order = []
with open(file, 'r') as subs:
    for line in subs:
        line = line.strip()
        if line.count(".") > 2:
            print(line.split(".")[-3] + "." +
                  line.split(".")[-2] + "." + line.split(".")[-1])
        elif line.count(".") == 2:
            print(line)
